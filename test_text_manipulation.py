import pytest

from text_manipulation import concat, to_upper


# to_upper

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
