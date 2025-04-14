from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import random
def play_dice(ti):
    sum =0
    for i in range(3):
        sum+= random.randint(1,6)
    ti.xcom_push(key='who_play', value=sum)

def res(ti):
    player1_score = ti.xcom_pull(task_ids='player_1', key='who_play')
    player2_score = ti.xcom_pull(task_ids='player_2', key='who_play')
    if player1_score > player2_score:
        return "Player 1 wins!"
    elif player2_score > player1_score:
        return "Player 2 wins!" 
    else :
        return "tie!" 
    #cách 2: 
    # total = max([val for val in ti.xcom_pull(task_ids=['player_1','player_2'],key='who_play')])
    # return total 

with DAG (
    dag_id='play_dice',
    schedule_interval='@hourly',
    start_date=datetime(2025, 4, 10),
    end_date=datetime(2025, 4, 12)
) as dag:
    task1 = PythonOperator(
        task_id='player_1',
        python_callable=play_dice
    ) 
    task2 = PythonOperator(
        task_id='player_2',
        python_callable=play_dice
    )
    task3= PythonOperator(
        task_id='Result',
        python_callable=res
    )

[task1,task2] >> task3