X = float(input())
N = int(input())

ans = 1.0 + X / 2.0
num_prod = 1.0
den_prod = 2.0
x_pow = X
sign = 1.0

for i in range(2, N + 1):
    sign = -sign
    num_prod *= (2 * i - 3)
    den_prod *= (2 * i)
    x_pow *= X
    ans += sign * (num_prod * x_pow) / den_prod

print(ans)
