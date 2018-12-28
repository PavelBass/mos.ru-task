from typing import Iterable

from mosru_task.mixins import LoggerMixin


class FakeThemesRepository(LoggerMixin):
    """ Fake themes repository, encapsulated to show concept
        Real repositories may be PostgresThemesRepository, RedisThemesRepository... etc
    """
    def __init__(self):
        super().__init__()
        self.__themes = {
            'новости': ['деревья на Садовом кольце', 'добрый автобус', 'выставка IT-технологий'],
            'кухня': ['рецепт борща', 'яблочный пирог', 'тайская кухня'],
            'товары': ['Дети капитана Гранта', 'зимние шины', 'Тайская кухня'],
        }

    async def get_themes_names(self) -> Iterable[str]:
        return iter(self.__themes.keys())

    async def get_theme_phrases(self, theme_name: str) -> Iterable[str]:
        return iter(self.__themes[theme_name])
