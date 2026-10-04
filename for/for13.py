n = int(input())
sum = 0
for i in range(1, n):
	if i%2 != 0:
		sum -= (i/10)+1
	else:
		sum+= (i/10)+1
print(sum)
