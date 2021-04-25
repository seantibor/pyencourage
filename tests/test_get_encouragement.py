import pytest
from pyencourage import get_encouragement, get_encouragements
from pyencourage.pyencourage import LanguageNotFoundError, CategoryNotFoundError


languages = ['en']
categories = ['neutral', 'positivity', 'advice', 'zen', 'all']
test_data = ['', 'abc', '123']


def test_get_encouragement():
    assert get_encouragement()

    for language in languages:
        assert get_encouragement(language=language)

    for category in categories:
        assert get_encouragement(category=category)


def test_get_encouragement_with_language_raises():
    for language in test_data:
        assert pytest.raises(
            LanguageNotFoundError, get_encouragement, language=language
        )


def test_get_encouragement_with_category_raises():
    for category in test_data:
        assert pytest.raises(
            CategoryNotFoundError, get_encouragement, category=category
        )


def test_get_encouragement_in_language_with_category_raises():
    for category in test_data:
        assert pytest.raises(
            CategoryNotFoundError, get_encouragement,
            language='en', category=category
        )

def test_all_jokes_are_funny():
    for language in languages:
        encouragements = get_encouragement(language=language, category='all')
        for encouragement in encouragements:
            assert True
