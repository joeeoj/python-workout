from numeric_types.pig_latin import pig_latin


def test_vowel():
    assert pig_latin('air') == 'airway'

def test_consonant():
    assert pig_latin('python') == 'ythonpay'
