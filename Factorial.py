import math


def factorize(num):
    fac = []

    while num % 2 == 0:
        fac.append(2)
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            fac.append(i)
            num = num / i
    if num > 2:
        fac.append(int(num))

    return fac


n = int(input("Enter Number: "))
print(factorize(n))
