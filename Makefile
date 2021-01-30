.PHONY: run restart logs

run:
	docker-compose up --d --build
	make logs

restart:
	docker-compose down
	make run

down:
	docker-compose down

logs:
	docker-compose logs --f