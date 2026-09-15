X = float(input())
N = int(input())

ans = X
term = X

for i in range(1, N + 1):
    term = -term * X * X / ((2 * i) * (2 * i + 1))
    ans += term

print(ans)
