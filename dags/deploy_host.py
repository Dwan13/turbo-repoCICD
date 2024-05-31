# dags/deploy_host.py
from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG(
    'deploy_host',
    default_args=default_args,
    description='CI/CD pipeline to deploy the host app',
    schedule_interval=None,
)

deploy_host = DockerOperator(
    task_id='deploy_host',
    image='node:18-alpine',  # Imagen base de Docker
    api_version='auto',
    auto_remove=True,
    command="sh -c 'cd /app && SITE=sitioA docker-compose up -d host'",
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    dag=dag,
)

deploy_host
