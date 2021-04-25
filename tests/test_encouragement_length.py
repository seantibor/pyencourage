from pyencourage.encourage_en import encourage_en


def _test_encouragement_length(encouragement):
    assert len(encouragement) <= 140


def _test_encouragement_group(encouragements):
    for encouragement in encouragements:
        _test_encouragement_length(encouragement)


def test_encouragements_lengths():
    encouragements_sets = [encourage_en, ]
    for encouragements in encouragements_sets:
        _test_encouragement_group(encouragements['all'])
