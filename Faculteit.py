n = int(input())
for i in range(n):
    x = int(input())

    if x > 13:
        print("invoer te groot")
    else:

        fac = 1
        for f in range(1, x + 1):
            fac *= f
        print(fac)

