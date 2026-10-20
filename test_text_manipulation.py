import pytest
from text_manipulation import reverse, count_vowels, is_palindrome, concat, to_upper

# Antes
def test_reverse_success():
    assert reverse("hola") == "aloh"
    assert reverse("python") == "nohtyp"

# Después
def test_reverse_simple():
    assert reverse("hola") == "aloh"

def test_reverse_multiple_chars():
    assert reverse("python") == "nohtyp"


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

# to upper

def test_to_upper_minusculas():
    assert to_upper("hola") == "HOLA"


def test_to_upper_texto_mixto():
    assert to_upper("Hola Mundo 123!") == "HOLA MUNDO 123!"


def test_to_upper_cadena_vacia():
    assert to_upper("") == ""


def test_to_upper_tipo_invalido():
    with pytest.raises(TypeError):
        to_upper(123)


def test_to_upper_none():
    with pytest.raises(TypeError):
        to_upper(None)


# concat

def test_concat_dos_palabras():
    assert concat("hola", "mundo") == "holamundo"


def test_concat_con_espacio():
    assert concat("hola ", "mundo") == "hola mundo"


def test_concat_cadena_vacia():
    assert concat("", "abc") == "abc"


def test_concat_primer_argumento_invalido():
    with pytest.raises(TypeError):
        concat(1, "abc")


def test_concat_segundo_argumento_invalido():
    with pytest.raises(TypeError):
        concat("abc", None)
