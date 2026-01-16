from airflow.decorators import dag, task
from datetime import datetime

@dag(
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['taskflow'],
)
def taskflow_example():

    @task
    def task_a():
        print("Task A executed")
        return 42

    @task
    def task_b(value):
        print("Task B executed")
        print(f"Received value: {value}")
    
    task_b(task_a())

taskflow_example()