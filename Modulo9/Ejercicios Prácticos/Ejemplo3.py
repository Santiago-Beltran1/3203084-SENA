# texto_utils.py
"""Módulo con utilidades para procesamiento de texto."""
import re
from collections import Counter

def limpiar_texto(texto):
    """Limpia el texto eliminando signos de puntuación y convirtiendo a minúsculas."""
    texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())
    return texto_limpio

def contar_palabras(texto):
    """Cuenta el número de palabras en un texto."""
    texto_limpio = limpiar_texto(texto)
    palabras = texto_limpio.split()
    return len(palabras)

def palabras_frecuentes(texto, n=5):
    """Encuentra las n palabras más frecuentes en un texto."""
    texto_limpio = limpiar_texto(texto)
    palabras = texto_limpio.split()
    contador = Counter(palabras)
    return contador.most_common(n)

def es_palindromo(texto):
    """Verifica si un texto es un palíndromo."""
    texto_limpio = limpiar_texto(texto)
    texto_sin_espacios = texto_limpio.replace(" ", "")
    return texto_sin_espacios == texto_sin_espacios[::-1]