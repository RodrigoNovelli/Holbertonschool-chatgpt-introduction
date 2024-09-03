#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcula el factorial de un número entero no negativo de manera recursiva.

    El factorial de un número entero n (notado como n!) es el producto de todos los enteros positivos menores o iguales a n.
    Por definición, el factorial de 0 es 1.

    Args:
        n (int): Un número entero no negativo del cual se calculará el factorial.

    Returns:
        int: El factorial del número entero n.

    Raises:
        ValueError: Si n es un número negativo.
    """
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """
    Lee un número entero desde la línea de comandos, calcula su factorial y lo imprime.

    El número entero debe ser pasado como argumento al ejecutar el script desde la línea de comandos.

    Ejemplo de uso:
        python3 script.py 5

    Salida:
        El resultado del cálculo del factorial del número proporcionado se imprime en la salida estándar.

    Exits:
        Salida con código de error 1 si el número proporcionado no es un entero no negativo.
    """
    if len(sys.argv) != 2:
        print("Uso: python3 script.py <número entero no negativo>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 0:
            raise ValueError
    except ValueError:
        print("Por favor, proporcione un número entero no negativo.")
        sys.exit(1)

    f = factorial(n)
    print(f)

if __name__ == "__main__":
    main()