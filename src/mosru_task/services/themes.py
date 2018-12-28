from typing import Set

from mosru_task.mixins import LoggerMixin
from mosru_task.respoitories.themes import FakeThemesRepository
from mosru_task.tools.theme import themes_keeper_instance
from mosru_task.types import Theme


class ThemesService(LoggerMixin):
    """Business logic to keep themes actual"""

    themes_keeper = themes_keeper_instance
    repository = FakeThemesRepository()

    async def refresh_themes(self) -> None:
        themes_names = set(await self.repository.get_themes_names())
        self._remove_nonexistent_themes(themes_names)
        for theme_name in themes_names:
            self.themes_keeper.add(Theme(theme_name, await self.repository.get_theme_phrases(theme_name)))

    def _remove_nonexistent_themes(self, themes_names: Set[str]):
        for theme_name in set(self.themes_keeper.themes) - themes_names:
            self.themes_keeper.remove(theme_name)
