N = int(input())

F1 = 1
F2 = 1

if N >= 1:
    print(F1)
if N >= 2:
    print(F2)

for i in range(3, N + 1):
    F = F1 + F2
    print(F)
    F1 = F2
    F2 = F

