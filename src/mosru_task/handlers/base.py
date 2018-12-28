import ujson
from dataclasses import asdict

from aiohttp import web

from mosru_task.mixins import LoggerMixin
from mosru_task.services.theme import ServiceResult


class BaseHandler(LoggerMixin, web.View):
    @staticmethod
    async def answer(answer: ServiceResult) -> web.Response:
        data = asdict(answer)
        return web.json_response(data=data, dumps=ujson.dumps)
