from prefect import flow, task 
from random import random
from prefect.cache_policies import TASK_SOURCE, RUN_ID

@task(cache_policy=TASK_SOURCE+RUN_ID)
def random_int():
    return random.randomint()

@flow
def test_caching_policies():
    y = random_int()