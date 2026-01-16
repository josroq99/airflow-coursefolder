from datetime import datetime, timedelta
from airflow.decorators import dag, task
import random

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    description='A simple DAG to generate and check random numbers',
    catchup=False
)
def random_number_checker_dag():
    @task
    def generate_random_number():
        print("Generating random number...")
        return random.randint(1, 100)

    @task
    def check_even_odd(value):
        result = "even" if value % 2 == 0 else "odd"
        print(f"The number {value} is {result}.")

    check_even_odd(generate_random_number())

random_number_checker_dag()


    