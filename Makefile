WEB_DB_NAME=odoo_development3
DOCKER=docker
DOCKER_COMPOSE=${DOCKER} compose
CONTAINER_ODOO=odoo
CONTAINER_DB=odoo-postgres

help:
	@echo " Available Target"
	@echo " Start     Start the compose with daemon"
	@echo " PS        View Status  with daemon"
	@echo " Pause     Pause the compose with daemon"
	@echo " UnPause   UnPause the compose with daemon"
	@echo " Stop      Stop the compose with daemon"
	@echo " Restart   Restart the compose with daemon"
	@echo " Console   Odoo interactive console"
	@echo " Psql      Postgresql interactive shell"
	@echo " Logs Odoo log_target TARGET=odoo for Logs the Odoo Container "
	@echo " Logs DB   log_target TARGET=db for Logs the Database Container "
	

start:
	$(DOCKER_COMPOSE) up -d

ps:
	$(DOCKER) ps -a

pause:
	$(DOCKER_COMPOSE) pause

unpause:
	$(DOCKER_COMPOSE) unpause

stop:
	$(DOCKER_COMPOSE) down

restart:
	$(DOCKER_COMPOSE) restart

console:
	$(DOCKER) exec -it $(CONTAINER_ODOO) odoo shell --db_host=$(CONTAINER_DB) -d $(WEB_DB_NAME) -r $(CONTAINER_ODOO) -w $(CONTAINER_ODOO)

psql:
	$(DOCKER) exec -it $(CONTAINER_DB) psql -U $(CONTAINER_ODOO) -d $(WEB_DB_NAME)


log_target:
	@if "$(TARGET)"=="odoo" (
		$(DOCKER_COMPOSE) logs -f $(CONTAINER_ODOO)
	) else if "$(TARGET)"=="db" (
		$(DOCKER_COMPOSE) logs -f $(CONTAINER_DB)
	) else (
		@echo "salah pilih"
	)


  
.PHONY: start stop restart console psql logs odoo db
