class ValidadorDeCadenas:
    def es_palindromo(self, cadena: str) -> bool:
        if not cadena:
            return False
        # eliminar espacios y normalizar a minúsculas
        cadena = ''.join(ch.lower() for ch in cadena if ch.isalpha())
        return cadena == cadena[::-1]

    def contar_vocales(self, cadena: str) -> int:
        if not cadena:
            return 0
        return sum(1 for ch in cadena.lower() if ch in "aeiou")

    def invertir_cadena(self, cadena: str) -> str:
        if not cadena:
            return ""
        return cadena[::-1]


