def dot_product(v1: list, v2: list) -> int:
    if len(v1) != len(v2):
        return 0
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]

    return total

v1 = [1,2,3]
v2 = [4,5,6]
v3 = [1]
v4 = [1,3]
print(dot_product(v1,v2))
print(dot_product(v3,v4))

