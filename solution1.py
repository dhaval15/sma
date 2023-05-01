from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
default_args = {
    'owner': 'Dhaval Patel',
    'start_date': days_ago(1)
    }
# Defining the DAG using Context Manager
with DAG(
        'Download dataset from kaggle and load in to Parquet format',
        default_args=default_args,
        schedule_interval=None,
        ) as dag:
        t1 = BashOperator(
                task_id = 'download-from-kaggle',
                bash_command = 'scripts/download-from-kaggle.sh',
        )
        t2 = PythonOperator(
                task_id = 'merge-and-convert-to-parquet',
        )
        t1 >> t2
