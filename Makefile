.PHONY: run restart logs

run:
	make down
	docker-compose up --d --build
	make logs

stop:
	docker-compose stop

down:
	docker-compose down

logs:
	docker-compose logs --f