try:
    n = int(input())
    res = 1.0
    while n > 0:
        res = res * n
        n = n - 2
    print(res)
except:
    pass
