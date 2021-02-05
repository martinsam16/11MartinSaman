.PHONY: run restart logs

run:
	make down
	docker-compose up --d --build

restart:
	make stop
	make start


start:
	docker-compose start


stop:
	docker-compose stop

down:
	docker-compose down

logs:
	docker-compose logs --f