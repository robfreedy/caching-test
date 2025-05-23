from prefect import flow, task, get_run_logger
from prefect.cache_policies import TASK_SOURCE, RUN_ID
from random import randrange

@task(cache_policy=TASK_SOURCE+RUN_ID)
def random_int():
    return randrange(10)

@flow
def test_caching_policies():
    y = random_int()
    logger = get_run_logger()
    logger.info(f"Random int: {y}")
