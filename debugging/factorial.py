#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) != 2:
    print("Uso: python3 script.py <número>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        print("El número debe ser un entero no negativo.")
        sys.exit(1)
    f = factorial(number)
    print(f)
except ValueError:
    print("Por favor, ingresa un número entero válido.")
    sys.exit(1)