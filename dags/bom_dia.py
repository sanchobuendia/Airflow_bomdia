from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta, datetime

def bom_dia():
    print('Bom dia!')

def hello_world():
    print('Hello World!')

args = {
    'owner': 'airflow',
    #"depends_on_past": False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': days_ago(1),
}

dag = DAG(
    dag_id='minimal',
    default_args=args,
    schedule_interval=None,
    start_date=datetime.now(),
    catchup = False,
)

task1 = PythonOperator(
        task_id='bom_dia',
        python_callable=bom_dia,
    )

task2 = PythonOperator(
        task_id='hello_world',
        python_callable=hello_world,
    )

# set the order of the tasks in the DAG
task1 >> task2