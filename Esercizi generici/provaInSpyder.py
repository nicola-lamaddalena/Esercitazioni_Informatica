# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:08:26 2024

@author: Uomonero
"""

def divisioni_successive(x: int) -> list:
    binary = []
    while x // 2 != 0:
        binary.append(x%2)
        x = x//2
    binary.append(x%2)
    binary.reverse()
    return binary


while True:
    try:
        x = int(input("Inserisci un numero in base 10: "))
        print(divisioni_successive(x))
        break
    except ValueError:
        print("Devi inserire un intero!")