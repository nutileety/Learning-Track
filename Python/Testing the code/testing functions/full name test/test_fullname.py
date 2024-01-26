from formated_name import get_formated_name

def test_fullname():
    result = get_formated_name('john','wick')
    assert result == 'John Wick'

def test_fullname_middlename():
    result = get_formated_name('jack','reacher',middlename='edwin')
    assert result == 'Jack Edwin Reacher'