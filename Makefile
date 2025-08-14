DC = sudo docker compose
ENV = --env-file .env
APP_FILE = docker-compose.yaml
OVERRIDE_FILE = docker-compose.override.yaml


.PHONY: start
start:
	${DC} -f ${APP_FILE} ${ENV} up --build -d
# watch синхронизирует файлы и перезапускает контейнер при их изменении (удобно для разработки)
.PHONY: watch
watch:
	${DC} -f ${APP_FILE} -f ${OVERRIDE_FILE} ${ENV} watch

.PHONY: stop
stop:
	${DC} -f ${APP_FILE} ${ENV} stop

.PHONY: down
down:
	${DC} -f ${APP_FILE} ${ENV} down

.PHONY: down-total
down-total:
	${DC} -f ${APP_FILE} ${ENV} down -v
