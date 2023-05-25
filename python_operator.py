from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 5, 23),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

def extract_data():
    # Code to extract data goes here
    pass

def transform_data():
    # Code to transform data goes here
    pass

def load_data():
    # Code to load data goes here
    pass

dag = DAG('sample_airflow_dag', default_args=default_args, schedule_interval='@daily')

start_operator = DummyOperator(task_id='start', dag=dag)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag
)

end_operator = DummyOperator(task_id='end', dag=dag)

start_operator >> extract_task >> transform_task >> load_task >> end_operator
