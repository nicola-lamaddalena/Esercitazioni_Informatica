def codifica_numeri_naturali(n: int) -> list:
    binary = []
    while n // 2 != 0:
        binary.insert(0, n%2)
        n = n//2
    binary.insert(0, n%2)
    return binary

try:
    x = input("Inserisci un numero da convertire in binario: ")
    print(codifica_numeri_naturali(int(x)))
except ValueError:
    print("Devi inserire un intero!")
