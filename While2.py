try:
    a = float(input())
    b = float(input())
    k = 0
    while a >= b:
        a = a - b
        k = k + 1
    print(k)
except:
    pass
