import asyncio
import time
from typing import (
    Awaitable,
    Optional,
)

from mosru_task.mixins import LoggerMixin


class BasePeriodicTask(LoggerMixin):
    """Base periodic task class.
    Task class inherited from this base class need to implement awaitable `task`  method.
    Class will be instantiated once, so task can keep data for future tasks in `self`.
    Time to wait before call and await next task calculates as `period - time_of_last_task`,
    so if time of task run is larger than period, next task will be called just after previous,
    and period for tasks will be larger than setted.
    `task` calls works successively.
    """
    period: Optional[int] = None

    async def main(self, *args, **kwargs):
        started_at = time.time()
        self.logger.info(
            'Periodic task %s started at %d with period %s',
            self.__class__.__name__,
            started_at,
            self.period
        )
        while True:
            start = time.time()
            task: Awaitable[None] = self.task(*args, **kwargs)

            try:
                await task
            except Exception as exc:  # pylint: disable=broad-except
                self.logger.exception('Exception on run')

            passed_time = time.time() - start
            self.logger.info('Task finished in %3.5f seconds', passed_time)

            period = self.period or 0 - time.time() + start
            await asyncio.sleep(period if period > 0 else 0)

    async def task(self, *args, **kwargs):
        raise NotImplementedError('Task is not implemented')
