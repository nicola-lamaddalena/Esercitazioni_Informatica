import random

L = [random.randint(1,10) for x in range(50)]

def tab_occ(L: list) -> dict:
    A = {}
    for i in L:
        if i not in A.keys():
            A[i] = 1
        else:
            A[i] += 1

    return A

def smooth(L: list) -> list:
    for i in range(len(L)):
        if i == 0:
            L[i] = round((L[i]+L[i+1])/2, 2)
        # len = 50; L[50] doesn't exists; L[49] is the last element
        elif i == len(L)-1:
            L[i] = round((L[i]+L[i-1])/2, 2)
        else:
            L[i] = round((L[i-1]+L[i]+L[i+1])/3, 2)

    return L

print("Lista:", L)
print()
print("Punto a):", tab_occ(L))
print()
print("Punto b):", smooth(L))
