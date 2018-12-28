import logging

import click
from aiohttp import web
from mosru_task import setup
from mosru_task.handlers.search import SearchHandler

logger = logging.getLogger(__name__)


@click.group()
def cli() -> None:
    setup()


@cli.command()
@click.option('--host', type=str, default='0.0.0.0')
@click.option('--port', type=int, default=8000)
def run(host: str, port: int) -> None:
    logger.info('=== START ===')
    app = web.Application()
    _configure_application(app)
    web.run_app(app, host=host, port=port)


def _configure_application(app: web.Application) -> None:
    app.add_routes([web.view('/search/', SearchHandler)])
