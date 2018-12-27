from typing import (
    Iterable,
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
