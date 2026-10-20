# admin-practica7

Librería de manipulación de texto en Python con pruebas unitarias e integración continua con GitHub Actions.

## Funciones

- `reverse(s)`: retorna la cadena en orden inverso.
- `count_vowels(s)`: retorna el total de vocales de la cadena.
- `is_palindrome(s)`: retorna si la cadena es palíndromo.
- `to_upper(s)`: retorna la cadena en mayúsculas.
- `concat(a, b)`: retorna la unión de dos cadenas.

Todas lanzan `TypeError` si reciben un argumento que no es cadena de texto.

## Pruebas

```bash
pip install pytest
pytest
```

Las pruebas se ejecutan automáticamente en cada Pull Request hacia `main`. La rama `main` está protegida y no permite merge si las pruebas fallan.
