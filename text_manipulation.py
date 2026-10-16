def to_upper(s):
    """Retorna la cadena de texto en mayúsculas."""
    if not isinstance(s, str):
        raise TypeError("s debe ser una cadena de texto")
    return s.upper()


def concat(a, b):
    """Retorna la unión de dos cadenas de texto."""
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("a y b deben ser cadenas de texto")
    return a + b
