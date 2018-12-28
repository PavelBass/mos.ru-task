import asyncio
from typing import (
    Tuple,
    Type,
)

from mosru_task.mixins import LoggerMixin
from mosru_task.tasks.base import BasePeriodicTask


class BaseLongTimeApplication(LoggerMixin):
    tasks: Tuple[Type[BasePeriodicTask]]

    def __init__(self) -> None:
        super().__init__(logger_name='LongTimeApp')

    async def initialize(self):
        initialized_tasks = []
        for task in self.tasks:
            task_instance = task()
            asyncio.ensure_future(
                coro_or_future=task_instance.main(),
            )
            initialized_tasks.append(task_instance.name)

        self.logger.info('Long-time application initialized with tasks: %s', repr(initialized_tasks))

