def mcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


while True:
    try:
        x = int(input("Inserisci il primo numero: "))
        y = int(input("Inserisci il secondo intero: "))
        print(mcd(x, y))
        break
    except ValueError:
        print("Devi inserire numeri interi.")
