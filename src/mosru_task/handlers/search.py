from aiohttp import web

from mosru_task.handlers.base import BaseHandler
from mosru_task.services.search import SearchService


class SearchHandler(BaseHandler):
    service = SearchService()

    async def get(self) -> web.Response:
        query = self.request.query.get('q', '')
        return await self.answer(await self.service.get_search_result(query))
