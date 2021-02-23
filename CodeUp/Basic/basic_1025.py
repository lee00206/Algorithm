a = int(input())

for i in range(4, -1, -1):
    b = a // (10**i)
    c = b * (10**i)
    print('[{0}]'.format(c))
    a = a - c
