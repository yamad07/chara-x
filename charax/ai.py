import logging
import os
import time
from typing import List

import openai
from logger import logger
from message import Utterance
from setting import config


def get_prompt(messages: List[Utterance], bot_name: str):
    context = "以下は、{}での会話です。".format(config["bot"]["context"])
    setting = "{}は、\n".format(bot_name)
    for chara in config["bot"]["characters"]:
        setting += "・{}\n".format(chara)

    setting += "のような特徴があります。"

    prompt = context + setting
    for message in messages:
        prompt += "\n{0}: {1}".format(message["user"], message["message"])

    prompt += "\n{0}: ".format(bot_name)
    logger.info("ai_prompt", extra={"prompt": prompt})
    return prompt


def create_response(replies: List[Utterance], bot_name: str, retry=5) -> str:
    retry_count = 0
    while True:
        retry_count += 1
        if retry_count > retry:
            break

        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=get_prompt(replies, bot_name),
                temperature=0.9,
                max_tokens=500,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.6,
            )
            logger.info("ai_api_response", extra={"response": response})
            return response["choices"][0]["text"].splitlines()[0]
        except openai.error.ServiceUnavailableError:
            time.sleep(1)

    logger.error("openai service is unavailable")
    return config["bot"]["default"]
