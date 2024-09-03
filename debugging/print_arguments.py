#!/usr/bin/python3
import sys

# Recorre los argumentos desde el índice 1 para evitar imprimir el nombre del script
for i in range(1, len(sys.argv)):
    print(sys.argv[i])