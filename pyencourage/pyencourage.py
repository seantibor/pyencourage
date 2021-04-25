from __future__ import absolute_import
import random

from .encourage_en import encourage_en


all_encouragements = {
    'en': encourage_en,
}


class LanguageNotFoundError(Exception):
    pass


class CategoryNotFoundError(Exception):
    pass


def get_encouragements(language='en', category='neutral'):
    """
    Parameters
    ----------
    category: str
        Choices: 'neutral', 'zen', 'positivity', 'advice', 'all'
    lang: str
        Choices: 'en'

    Returns
    -------
    encouragements: list
    """

    if language not in all_encouragements:
        raise LanguageNotFoundError(f'No such language {language}')

    encouragements = all_encouragements[language]

    if category not in encouragements:
        raise CategoryNotFoundError(f'No such category {category} in language {language}')

    return encouragements[category]


def get_encouragement(language='en', category='neutral'):
    """
    Parameters
    ----------
    category: str
        Choices: 'neutral', 'all'
    lang: str
        Choices: 'en'

    Returns
    -------
    encouragement: str
    """

    encouragements = get_encouragements(language, category)
    return random.choice(encouragements)
