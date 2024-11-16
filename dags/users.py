from airflow import DAG
from airflow.utils.dates import days_ago
from datetime import timedelta
from airflow.providers.docker.operators.docker import DockerOperator

default_args = {
    'owner': 'info',
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

with DAG(
    dag_id='run_python_job_with_docker',
    description='Pipeline using Docker python job',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval='@once',
    tags=['pipeline', 'docker']
) as dag:
    run_print_users = DockerOperator(
        task_id='run_print_users',
        image='sedia4/kb:v1.2.0',
        # image='sedia4/kb:v1.2.0',
        # image='scripts/kb:v1.1.1',
        api_version='auto',
        auto_remove=True,
        command="python3 print_users.py",
        docker_url='unix://var/run/docker.sock',
        network_mode='host',
        mount_tmp_dir=False,
        tty=True,
    )
    run_print_users