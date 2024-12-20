clean:
	docker-compose down --volumes --remove-orphans
	docker system prune -a --volumes --force

up:
	docker-compose up --force-recreate --build
