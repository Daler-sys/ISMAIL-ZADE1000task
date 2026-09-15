X = float(input())
N = int(input())

ans = 0.0
term = X

for i in range(1, N + 1):
    ans += term / i
    term = -term * X

print(ans)
