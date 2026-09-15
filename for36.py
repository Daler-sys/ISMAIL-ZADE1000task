N = int(input())
K = int(input())

ans = 0.0

for i in range(1, N + 1):
    term = 1.0
    for j in range(K):
        term *= i
    ans += term

print(ans)
