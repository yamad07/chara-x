import io
import logging
import os
import time
from typing import List

import requests
from PIL import Image
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

from charax.ai import create_response
from charax.logger import logger
from charax.message import Utterance

app = App(token=os.environ["SLACK_BOT_TOKEN"])
client = WebClient(os.environ.get("SLACK_BOT_TOKEN"))


def replace_id_to_name(user_id: str) -> str:
    result = client.users_info(user=user_id)
    display_name = result["user"]["profile"]["display_name"]
    if display_name != "":
        return display_name

    return result["user"]["real_name"]


def get_replies(channel: str, ts: str) -> List[Utterance]:
    result = client.conversations_replies(channel=channel, ts=ts)
    messages = result["messages"]

    return [
        {"user": replace_id_to_name(message["user"]), "message": message["text"]}
        for message in messages
    ]


def get_thread_ts(event):
    if "thread_ts" in event:
        return event["thread_ts"]

    return event["ts"]


@app.event("app_mention")
def message_hello(event, say):
    logger.warning("slack_app_mention_event", extra=event)

    replies = get_replies(event["channel"], get_thread_ts(event))
    response = create_response(
        replies, replace_id_to_name(os.environ["SLACK_BOT_USER_ID"])
    )
    say("{}".format(response), thread_ts=event["ts"])


@app.event("message")
def handle_app_mention_events(body, logger):
    logger.info("slack_message_event", extra=body)


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
