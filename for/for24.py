X = float(input())
N = int(input())

ans = 1.0
term = 1.0

for i in range(1, N + 1):
    term = -term * X * X / ((2 * i - 1) * (2 * i))
    ans += term

print(ans)
