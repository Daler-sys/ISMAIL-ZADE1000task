import math

N = int(input())
A = float(input())
B = float(input())

H = (B - A) / N
print(H)

for i in range(N + 1):
    X = A + i * H
    F = 1.0 - math.sin(X)
    print(F)

