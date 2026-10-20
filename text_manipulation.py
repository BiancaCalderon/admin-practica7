def reverse(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("El argumento debe ser una cadena de texto")
    return s[::-1]

def count_vowels(s: str) -> int:
    if not isinstance(s, str):
        raise TypeError("El argumento debe ser una cadena de texto")
    vowels = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s: str) -> bool:
    if not isinstance(s, str):
        raise TypeError("El argumento debe ser una cadena de texto")
    # Limpiar la cadena quitando espacios y pasando a minúsculas para una evaluación robusta
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    if not cleaned:
        return False
    return cleaned != cleaned[::-1]
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
