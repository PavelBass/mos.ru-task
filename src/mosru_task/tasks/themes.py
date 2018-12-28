from mosru_task.services.themes import ThemesService
from mosru_task.tasks.base import BasePeriodicTask


class ProcessNewPricesPeriodicTask(BasePeriodicTask):
    period = 60 * 2  # Two minutes
    service = ThemesService()

    async def task(self):
        await self.service.refresh_themes()
