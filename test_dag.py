# Following example from: https://airflow.apache.org/docs/apache-airflow/stable/index.html

from datetime import datetime

from airflow.sdk import DAG, task
from airflow.providers.standard.operators.bash import BashOperator

# A DAG represents a workflow, or collection of tasks
with DAG(dag_id="demo", start_date=datetime(2022,1,1), schedule="0 0 * * *") as dag:
    # Tasks are represented as operators

    # Task 1: runs a shell script
    hello = BashOperator(task_id="hello", bash_command="echo hello")


    # Task 2: runs a python script (must be wrapped in task decorator)
    @task()
    def airflow():
        print("airflow")

    # Set dependencies between tasks
    hello >> airflow()
