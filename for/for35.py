N = int(input())

A1 = 1
A2 = 2
A3 = 3

if N >= 1:
    print(A1)
if N >= 2:
    print(A2)
if N >= 3:
    print(A3)

for i in range(4, N + 1):
    A = A3 + A2 - 2 * A1
    print(A)
    A1 = A2
    A2 = A3
    A3 = A
