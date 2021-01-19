a, b, c, d = input().split(' ')

if (int(d) > int(b)):
    print(int(a) + int(c) * (int(d) - int(b)))
else:
    print(a)