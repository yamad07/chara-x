PHONY: run-slack
run-slack:
	docker-compose up

PHONY: run-console
run-console:
	docker-compose run ai runs/console.py
