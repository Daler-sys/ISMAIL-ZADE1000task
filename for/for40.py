A = int(input())
B = int(input())

for i in range(A, B + 1):
    count = i - A + 1
    for j in range(count):
        print(i)
