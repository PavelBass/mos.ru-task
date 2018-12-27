import pytest

from mosru_task.tools.theme import ThemesKeeper
from mosru_task.types import Theme


def test_theme_keeper__add_theme_works_as_expected():
    # arrange
    themes_keeper1 = ThemesKeeper()
    themes_keeper2 = ThemesKeeper()
    theme_name1 = 'TheMe 1'
    theme_name2 = 'tHeMe 2'
    theme1 = Theme(theme_name1)
    theme2 = Theme(theme_name2)

    # act
    themes_keeper1.add(theme1)
    themes_keeper2.add(theme1)
    themes_keeper2.add(theme2)

    # assert
    assert list(themes_keeper1.themes) == [theme_name1]
    assert set(themes_keeper2.themes) == {theme_name1, theme_name2}


def test_theme_keeper__remove_theme_works_as_expected():
    # arrange
    themes_keeper = ThemesKeeper()
    theme_name1 = 'TheMe 1'
    theme_name2 = 'tHeMe 2'
    theme1 = Theme(theme_name1)
    theme2 = Theme(theme_name2)
    themes_keeper.add(theme1)
    themes_keeper.add(theme2)

    # act, assert
    assert set(themes_keeper.themes) == {theme_name1, theme_name2}

    themes_keeper.remove(theme1.name)
    assert list(themes_keeper.themes) == [theme_name2]

    themes_keeper.remove('something else')
    assert list(themes_keeper.themes) == [theme_name2]


@pytest.mark.asyncio
async def test_theme_keeper__async_themes__returns_expected():
    # arrange
    themes_keeper = ThemesKeeper()
    theme1, theme2, theme3 = (Theme(str(num)) for num in range(1, 4))
    themes_keeper.add(theme1)
    themes_keeper.add(theme2)
    themes_keeper.add(theme3)

    # act
    themes = [theme async for theme in themes_keeper._themes()]

    # assert
    assert len(themes) == 3
    assert all([isinstance(item, Theme) for item in themes])
    assert theme1 in themes
    assert theme2 in themes
    assert theme3 in themes


@pytest.mark.asyncio
@pytest.mark.parametrize('phrase,expected_themes', [
    ('df', set()),
    ('рецепт наивкуснейшего борща', {'кухня'}),
    ('Тайская кухня растопила своей остротой моё сердце', {'кухня', 'товары'}),
    ('Выставка IT-технологий и тайская кухня', {'кухня', 'товары', 'новости'}),
])
async def test_theme_keeper__get_relevant_themes__return_expected(phrase, expected_themes):
    # arrange
    themes_keeper = ThemesKeeper()
    theme1 = Theme('новости', ['деревья на Садовом кольце', 'добрый автобус', 'выставка IT-технологий'])
    theme2 = Theme('кухня', ['рецепт борща', 'яблочный пирог', 'тайская кухня'])
    theme3 = Theme('товары', ['Дети капитана Гранта', 'зимние шины', 'Тайская кухня'])

    themes_keeper.add(theme1)
    themes_keeper.add(theme2)
    themes_keeper.add(theme3)

    # act
    result = await themes_keeper.get_relevant_themes(phrase)

    # assert
    assert set(result) == expected_themes
