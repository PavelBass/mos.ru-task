from mosru_task.base import BaseLongTimeApplication
from mosru_task.tasks.themes import ProcessNewPricesPeriodicTask


class LongTimeApplication(BaseLongTimeApplication):
    tasks = (
        ProcessNewPricesPeriodicTask,
    )
