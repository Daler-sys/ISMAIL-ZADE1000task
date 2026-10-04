x = float(input())
n = int(input())

ans = 1.0
term = 1.0

for i in range(1, n + 1):
    term = term * x / i
    ans += term

print(ans)
