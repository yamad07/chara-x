PHONY: run-slack
run-slack:
	docker-compose run ai runs/slack-bot.py

PHONY: run-console
run-console:
	docker-compose run ai runs/console.py
