N = int(input())
A = float(input())
B = float(input())

H = (B - A) / N
print(H)

for i in range(N + 1):
    print(A + i * H)

