def changeMaking(D, n):
    m = len(D)
    F = [0] * (n + 1)

    for i in range(1, n + 1):
        temp = float('inf')
        for j in range(1, m + 1):
            if i >= D[j - 1]:
                temp = min(F[i - D[j - 1]], temp)

        F[i] = temp + 1

    return F[n]


print(changeMaking([4], 10))
print(changeMaking([1, 3, 4], 8))
print(changeMaking([1, 5, 10, 20, 25], 63))
print(changeMaking([1, 5, 10, 20, 25], 64))
