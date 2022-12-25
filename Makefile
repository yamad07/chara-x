PHONY: run-slack
run-slack:
	docker-compose run ai charax/slack.py

PHONY: run-console
run-console:
	docker-compose run ai charax/console.py
