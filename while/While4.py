try:
    n = int(input())
    while n > 1 and n % 3 == 0:
        n = n // 3
    if n == 1:
        print(True)
    else:
        print(False)
except:
    pass
