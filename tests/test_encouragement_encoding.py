from pyencourage.encourage_en import encourage_en

#test if encouragement is windows compatible
def _test_encouragement_win(encouragement):
    assert len(encouragement) <= len(encouragement.encode('iso-8859-1', 'ignore')) ##ascii don't support umlauts

def _test_default_locale(encouragement):
    import locale
    encod = locale.getdefaultlocale()[1]
    assert len(encouragement) <= len(encouragement.encode(encod, 'ignore'))

#unix is full compatible - no need of tests
def test_encouragements_lengths():
    encouragements_sets = [encourage_en, ]
    for encouragements in encouragements_sets:
        for j in encouragements['all']:
            _test_default_locale(j)
            _test_encouragement_win(j)
