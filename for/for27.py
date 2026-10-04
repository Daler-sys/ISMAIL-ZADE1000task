X = float(input())
N = int(input())

ans = X
num_prod = 1.0
den_prod = 1.0
x_pow = X

for i in range(1, N + 1):
    num_prod *= (2 * i - 1)
    den_prod *= (2 * i)
    x_pow *= X * X
    ans += (num_prod * x_pow) / (den_prod * (2 * i + 1))

print(ans)
