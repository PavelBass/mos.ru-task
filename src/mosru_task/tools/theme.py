from typing import (
    AsyncGenerator,
    Dict,
    Iterable,
    List,
    Optional,
    Set,
)


class Theme:
    """Theme type
    Holds theme name, array of theme phrases.
    Encapsulates methods to check if some phrase is relevant to theme
    """
    def __init__(self, name: str, phrases: Optional[Iterable[str]]=None) -> None:
        self.__name = name
        phrases = [] if phrases is None else phrases
        self.__phrases = [self._phrase_to_set(phrase) for phrase in phrases]

    @property
    def name(self) -> str:
        return self.__name

    @staticmethod
    def _phrase_to_set(phrase: str) -> Set[str]:
        return set(phrase.lower().split())

    def is_relevant(self, phrase: str) -> bool:
        phrase_set = self._phrase_to_set(phrase)
        for theme_phrase_set in self.__phrases:
            if theme_phrase_set <= phrase_set:
                return True
        return False


class ThemesKeeper:
    """ Keeper of existent themes.
        Encapsulates methods to control current themes array
        and to get relevant themes names for passed phrase.
    """
    def __init__(self):
        self.__themes: Dict[str, Theme] = {}

    @property
    def themes(self) -> Iterable[str]:
        """Themes names array """
        return iter(self.__themes.keys())

    def add(self, theme: Theme) -> None:
        """Add Theme for keeping"""
        self.__themes[theme.name] = theme

    def remove(self, theme_name: str) -> None:
        """Remove theme from keeping"""
        if theme_name in self.__themes:
            del(self.__themes[theme_name])

    async def _themes(self) -> AsyncGenerator[Theme]:
        """Povides asynchronous access to Themes array"""
        for theme_name in self.themes:
            if theme_name not in self.__themes:
                # Themes can be changed during async iteration
                continue
            yield self.__themes[theme_name]

    async def get_relevant_themes(self, phrase: str) -> List[str]:
        """Returns list of relevant themes names for passed phrase
        Coroutine gets asynchronous access to each Theme because
        themes can hold large lists of relevant phrases and mathematical
        comparisons of passed phrase to all phrases of all themes can spend
        to much time with blocking server.
        """
        return [theme.name async for theme in self._themes() if theme.is_relevant(phrase)]
