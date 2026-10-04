a = int(input())
n = int(input())
sum = 0
for i in range(0, n):
	if i%2 != 0:
		sum -= a**i
	else:
		sum += a**i
print(sum)

