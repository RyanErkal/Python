def enum(list):
    d = {}
    for i in enumerate(list):
        print(i)
    for i, n in enumerate(list):
        print(i, n)
        d[i] = n
    print(d)
    print(d[1])
    print(d[30])


enum([10, 20, 30, 40, 50, 60, 70, 80])
