from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
#import bash 
from airflow.operators.bash_operator import BashOperator

def calculate_dates(**context):
    pass    

with DAG(
    dag_id="webapp_data",
    schedule_interval="@daily",
    start_date=datetime(2025, 4, 9),
    end_date=datetime(2025, 4, 12),
) as dag:
    get_connection = BashOperator(
        task_id='get_connection',
        bash_command= 'curl -o /var/tmp/eventes-{{ds}}.json http://localhost:5000/events?start_date={{ds}}&end_date={{marco.ds_add(ds,1)}}',
    )

    calculate_stats_tasks = PythonOperator(
        task_id='calculate_stats_tasks',
        python_callable=calculate_dates,
        templates_dict={
            'input_path': '/var/temp/eventes-{{ds}}.json',
            'output_path': '/var/temp/evnetes-{{ds}}.csv'
        }
    )