import pytest

from mosru_task.tools.theme import Theme


def test_theme_name__returns_expected():
    # arrange
    passed_name = 'SoMe NaMe'
    theme = Theme(passed_name)

    # act, assert
    assert theme.name == passed_name


@pytest.mark.parametrize("phrase,expected", [
    ('a', {'a'}),
    ('A', {'a'}),
    ('ab bc cd', {'ab', 'bc', 'cd'}),
    (' aB   bc       Cd   ', {'ab', 'bc', 'cd'}),
])
def test_theme_phrase_to_set__returns_expected(phrase, expected):
    # arrange
    theme = Theme('some theme')

    # act
    result = theme._phrase_to_set(phrase)

    # assert
    assert result == expected


@pytest.mark.parametrize("phrase,expected", [
    ('Деревья на горящем кольце', False),
    ('Деревья на праздничном Садовом кольце украшены огнями', True),
    ('На кольце Фродо увидел эльфийские письмена и спрятался за деревья на садовом участке', True),
    ('У доброго автобуса весёлый контролёр', False),
    ('Добрый автобус мчит на пролом, Фредди Крюгер сидит за рулём', True),
    ('Выставку IT-технологий разгромил добрый автобус управляемый Фредди Крюгером, снеся деревья на Садовом кольце', True)
])
def test_theme_is_relevant__returns_expected(phrase, expected):
    # arrange
    theme_prhases = ('деревья на Садовом кольце', 'добрый автобус', 'выставка IT-технологий')
    theme = Theme('some theme', theme_prhases)

    # act
    result = theme.is_relevant(phrase)

    # assert
    assert result is expected
