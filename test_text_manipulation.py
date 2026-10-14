import pytest
from text_manipulation import reverse, count_vowels, is_palindrome

# Pruebas para reverse
def test_reverse_success():
    assert reverse("hola") == "aloh"
    assert reverse("python") == "nohtyp"

def test_reverse_error():
    with pytest.raises(TypeError):
        reverse(123)

# Pruebas para count_vowels
def test_count_vowels_success():
    assert count_vowels("Hola Mundo") == 4
    assert count_vowels("AEIOUaeiou") == 10
    assert count_vowels("bcdfg") == 0

def test_count_vowels_error():
    with pytest.raises(TypeError):
        count_vowels(None)

# Pruebas para is_palindrome
def test_is_palindrome_success():
    assert is_palindrome("anita lava la tina") is True
    assert is_palindrome("radar") is True
    assert is_palindrome("python") is False

def test_is_palindrome_error():
    with pytest.raises(TypeError):
        is_palindrome(454)