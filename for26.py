X = float(input())
N = int(input())

ans = 0.0
term = X

for i in range(0, N + 1):
    ans += term / (2 * i + 1)
    term = -term * X * X

print(ans)
