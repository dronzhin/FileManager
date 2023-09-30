from math import pi, sqrt, pow, hypot
def check_word(word):
    if word.startswith('m'):
        return True
    else:
        return False
def title_word(word):
    return word.title()
def test_filter():
    assert list(filter(check_word, ['max', 'leo', 'mich'])) == ['max', 'mich']
def test_map():
    assert list(map(title_word, ['max', 'leo', 'mich'])) == ['Max', 'Leo', 'Mich']
def test_sorted():
    assert sorted(['max', 'leo', 'mich']) == ['leo', 'max', 'mich']
    assert sorted(['max', 'mich', 'leo'], key=len) == ['max', 'leo', 'mich']

def test_pi():
    assert round(pi, 4) == 3.1416
def test_sqrt():
    assert sqrt(9) == 3.0

def test_pow():
    assert pow(3, 2) == 9

def test_hypot():
    assert round(hypot(1, 2), 4) == 2.2361
