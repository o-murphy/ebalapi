.PHONY: run-dev-server
run-dev-server:
	@python manage.py runserver


.PHONY: run-local-server
run-local-server:
	@python -m uvicorn delivery.web.asgi:application


.PHONY: run-prod-server
run-prod-server:
	@python -m gunicorn delivery.web.asgi:application \
		--worker-class uvicorn.workers.UvicornWorker \
		--bind ${HOST}:${PORT} \
		--workers ${WORKERS} \
		--log-level ${LOG_LEVEL} \
		--access-logfile ${ACCESS_LOGFILE} \
		--error-logfile ${ERROR_LOGFILE} \


.PHONY: makemigrations
makemigrations:
	@python manage.py makemigrations


.PHONY: migrate
migrate:
	@python manage.py migrate


.PHONY: buildwatson
buildwatson:
	@python manage.py buildwatson


