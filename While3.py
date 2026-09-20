try:
    n = int(input())
    k = int(input())
    q = 0
    r = n
    while r >= k:
        r = r - k
        q = q + 1
    print(q, r)
except:
    pass
