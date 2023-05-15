"""
Crear un DAG:
- DAG_ID: <vuestro_nombre>_ur_workshop_2
- NO planificado para ejecuciones calendarizadas
- Tageado con la tag: ur-workshop

El dag tiene que hacer las siguiente tareas:
1- Mediante un comando de Bash crear en /tmp un fichero txt cuyo nombre sea la fecha de generacion (mirar Templates).
2- Mediante código python añadirle una línea con vuestro nombre al fichero
3- De nuevo con código Bash mostrar el contenido que hemos añadido al fichero en el paso anterior o eliminarlo mediante
una rama de Airflow.

Referencias:
- Argumentos del DAG: https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/dag/index.html
- Templates: https://airflow.apache.org/docs/apache-airflow/2.6.0/templates-ref.html
- Bash: https://airflow.apache.org/docs/apache-airflow/2.6.0/howto/operator/bash.html#bashoperator
- Python: https://airflow.apache.org/docs/apache-airflow/2.6.0/howto/operator/python.html
- Branching: https://airflow.apache.org/docs/apache-airflow/2.6.0/core-concepts/dags.html#branching
"""


from __future__ import annotations

import datetime

import pendulum
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    # TODO: add your DAG arguments
) as dag:
    # TODO: add your DAG tasks
    pass
