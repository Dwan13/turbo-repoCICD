# dags/deploy_apps.py
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
    'deploy_apps',
    default_args=default_args,
    description='CI/CD pipeline to deploy Next.js apps',
    schedule_interval=None,
)

deploy_host = DockerOperator(
    task_id='deploy_host',
    image='node:18-alpine',  # Imagen base de Docker
    api_version='auto',
    auto_remove=True,
    command="sh -c 'cd /app/apps/host && SITE=sitioA docker-compose up -d'",
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    dag=dag,
)

deploy_quicksearch = DockerOperator(
    task_id='deploy_quicksearch',
    image='node:18-alpine',  # Imagen base de Docker
    api_version='auto',
    auto_remove=True,
    command="sh -c 'cd /app/apps/quicksearch && SITE=sitioB docker-compose up -d'",
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    dag=dag,
)

deploy_host >> deploy_quicksearch
