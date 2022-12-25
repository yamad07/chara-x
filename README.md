# CharaX
CharaX is software that allows you to create a preference-configured chat AI.

## Getting Started

```
cp .env .env.default // and write your configuration. you must set the value of `OPENAI_API_KEY`.
make run-console // run in console

make run-slack // run in slack
```

## Change your own setting
Modify the setting.yaml file and rerun.

```setting.yaml
bot:
  context: SaaS事業を展開しているスタートアップ企業
  characters:
    - この企業に紛れ込んだスパイ
    - 頭が良い
  default: 任務達成。

```

## Slack Bot Configuration
WIP
