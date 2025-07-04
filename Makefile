VENV_DIR = venv
ifeq ($(CI_RUN),test)
	PYTHON = /usr/local/bin/python
	PIP = /usr/local/bin/pip
else
	PYTHON = $(VENV_DIR)/bin/python
	PIP = $(VENV_DIR)/bin/pip
endif
ACTIVATE = .env

ifeq ($(OS),Windows_NT)
    PYTHON = $(VENV_DIR)/Scripts/python.exe
    PIP = $(VENV_DIR)/Scripts/pip.exe
		ACTIVATE = $(VENV_DIR)/Scripts/activate
endif

SHELL:=/bin/bash 
.PHONY: up up_docker destroy destroy_docker #docker_test
up: check_venv install_requirements up_docker run
docker_tests: check_venv install_requirements docker_test
tests: check_venv install_requirements run_tests
ci_tests: install_requirements run_tests
up_docker: check_docker docker_up
destroy: 
destroy_docker: check_docker docker_destroy


.PHONY: check_venv
check_venv:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Criando ambiente virtual..."; \
		python3.11 -m venv $(VENV_DIR); \
	fi

.PHONY: install_requirements
install_requirements:
	@$(PIP) install -r src/requirements.txt

.PHONY: run
run:
	@source $(ACTIVATE) && \
	$(PYTHON) src/manage.py migrate && \
	# $(PYTHON) src/manage.py loaddata src/fixtures/estados.json \
	# src/fixtures/Cities.json \
	# src/fixtures/VehicleType.json \
	# && \
	$(PYTHON) src/manage.py shell -c "exec(open('src/create_superuser.py').read())" && \
	$(PYTHON) src/manage.py runserver 0.0.0.0:8000

.PHONY: run_tests
run_tests:
	@if [ "$(CI_RUN)" != "test" ]; then \
		source $(ACTIVATE); \
	else \
		PYTHON=/bin/python; \
	fi && \
	$(PYTHON) src/manage.py migrate && \
	pytest --disable-warnings src/apis/v1/tests/ -x -vv -s

.PHONY: check_docker
check_docker:
	@if ! command -v docker-compose > /dev/null 2>&1 && ! docker compose version > /dev/null 2>&1; then \
		echo "Erro: Docker Compose não encontrado. Certifique-se de ter o docker-compose ou docker compose instalado."; \
		exit 1; \
	fi
	@if ! grep -q "127.0.0.1[[:space:]]\+minio" /etc/hosts; then \
		echo "127.0.0.1     minio" | sudo tee -a /etc/hosts; \
	fi

.PHONY: docker_up
docker_up:
	@if command -v docker-compose > /dev/null 2>&1; then \
		docker-compose up -d; \
	else \
		docker compose up -d; \
	fi

.PHONY: docker_destroy
docker_destroy:
	@if command -v docker-compose > /dev/null 2>&1; then \
		docker-compose down --rmi all; \
	else \
		docker compose down --rmi all; \
	fi

.PHONY: destroy
destroy:
	@if [ -d "$(VENV_DIR)" ]; then \
		echo "Removendo o ambiente virtual..."; \
		rm -rf $(VENV_DIR); \
	else \
		echo "Ambiente virtual não encontrado."; \
	fi