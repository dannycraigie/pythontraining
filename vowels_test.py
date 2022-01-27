import vowels

def test_vowelcount():
    assert vowels.vowels("hello") == 2

def test_vowelcount2():
    assert vowels.vowels("world") == 1

def test_vowelcount3():
    assert vowels.vowels("testingvowels") == 4
