# CharaX
CharaX is software that allows you to create a preference-configured chat AI.

## Getting Started

```
cp .env .env.default
// and write your configuration.
// you must set the value of `OPENAI_API_KEY`.

make run-console // run in console

make run-slack // run in slack
```

## Change your own setting
Modify the setting.yaml file and rerun.

```yaml
bot:
  context: SaaS事業を展開しているスタートアップ企業
  characters:
    - この企業に紛れ込んだスパイ
    - 頭が良い
  default: 任務達成。

```
## Use as Template
This is also released as a template project. Write your own setting.yaml and deploy it wherever you like.


## Slack Bot Configuration
### 1. Create your Slack app
Refer to [this document](https://slack.dev/bolt-python/ja-jp/tutorial/getting-started) to enable Socket Mode and grant the following permissions.
```
- channels:history
- chat:write
- group:history
- im:history
- mpim:history
- users:read
- users:write
```

Then, get an App-level token and a bot token.

### 2. Sign up for [OpenAI](https://openai.com/)
Create an OpenAI account and get an API token.

### 3. Set the token of Slack bot and OpenAI as environment variables.
Set the tokens and `user_id` of slack bot in the environment variable and execute.
```
make run-slack
```

## Deployment
Using [okteto](https://www.okteto.com/), you can quickly deploy an AI of your setting. When you deploy, set environment variables using the Okteto Secret.

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy)
