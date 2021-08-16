.PHONY : help
help :
	@echo "results.txt : Generate Zipf summary table."
	@echo "dats        : Count words in text files."
	@echo "clean       : Remove auto-generated files."

.PHONY : airflow
airflow:  ## Build airflow
	@echo "[-----------------------------------------]"
	@echo "Airflow building...."
	docker-compose -f airflow/docker-compose.yaml up airflow-init
	docker-compose -f airflow/docker-compose.yaml up -d


.PHONY : airflowdown
airflowdown:  ## Build airflow
	@echo "[-----------------------------------------]"
	docker-compose -f airflow/docker-compose.yaml down -v

.PHONY : elk
elk:  ## Build elk stack
	@echo "[-----------------------------------------]"
	@echo "ELK Stack building...."
	docker-compose -f docker-elk/docker-compose.yml up --build -d

.PHONY : elkdown
elkdown:  ## Build elk stack
	@echo "[-----------------------------------------]"
	@echo "ELK Stack building...."
	docker-compose -f docker-elk/docker-compose.yml down -v


.PHONY : dev
dev:  ## Build web
	@echo "[-----------------------------------------]"
	@echo "web building...."
	docker-compose up --build -d

.PHONY : prod
prod:  ## Build web
	@echo "[-----------------------------------------]"
	@echo "web building...."
	docker-compose -f docker-compose.prod.yml up --build -d

.PHONY : devdown
devdown:  ## Build web
	@echo "[-----------------------------------------]"
	@echo "web building...."
	docker-compose down -v

.PHONY : proddown
proddown:  ## Build web
	@echo "[-----------------------------------------]"
	@echo "web building...."
	docker-compose -f docker-compose.prod.yml down -v

.PHONY : build
build:  ## Build all
	@echo "[Building all tools...]"
	make airflow
	make prod
	make elk-stack


.PHONY : builddown
builddown:  ## Build down
	@echo "[Building all tools...]"
	make airflowdown
	make proddown
	make elkdown
