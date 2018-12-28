from dataclasses import (
    dataclass,
    field,
)
from typing import List

from mosru_task.enums import ServiceResultStatus
from mosru_task.mixins import LoggerMixin
from mosru_task.services.base import ServiceResult
from mosru_task.tools.theme import themes_keeper_instance


class SearchService(LoggerMixin):
    """Business logic of search"""

    themes_keeper = themes_keeper_instance

    @dataclass
    class _Data:
        """Data structure of search result"""
        query: str
        themes: List[str] = field(default_factory=list)

    async def get_search_result(self, query: str) -> ServiceResult:
        result = ServiceResult()
        data = await self._get_search_data(query)
        if not data.themes:
            self.logger.info('Query "%s" has no themes', query)
            result.status = ServiceResultStatus.NoResult
        result.data = data
        return result

    async def _get_search_data(self, query: str) -> _Data:
        data = self._Data(query=query)
        if query:
            data.themes = await self._get_relevant_themes(query)
        return data

    async def _get_relevant_themes(self, phrase: str) -> List[str]:
        return await self.themes_keeper.get_relevant_themes(phrase)
