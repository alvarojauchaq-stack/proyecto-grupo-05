import pytest
from validador_de_cadenas import ValidadorDeCadenas


# ===== es_palindromo =====
def test_es_palindromo_oso():
    v = ValidadorDeCadenas()
    assert v.es_palindromo("oso") is True

def test_es_palindromo_casa():
    v = ValidadorDeCadenas()
    assert v.es_palindromo("casa") is False

def test_es_palindromo_frase():
    v = ValidadorDeCadenas()
    assert v.es_palindromo("Anita lava la tina") is True


# ===== contar_vocales =====
def test_contar_vocales_basico():
    v = ValidadorDeCadenas()
    assert v.contar_vocales("hola") == 2
    assert v.contar_vocales("xyz") == 0
    assert v.contar_vocales("AEIOU") == 5
    assert v.contar_vocales("") == 0


# ===== invertir_cadena =====
def test_invertir_cadena():
    v = ValidadorDeCadenas()
    assert v.invertir_cadena("hola") == "aloh"
    assert v.invertir_cadena("a") == "a"
    assert v.invertir_cadena("") == ""



