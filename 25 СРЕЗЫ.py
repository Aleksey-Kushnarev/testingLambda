#СОБРАТЬ В ОДНУ СТРОКУ
for a in range(10):
    for b in range(10):
        n = "134" + str(a) + "3" + str(b)
        n = int(n)
        if n % 63 == 0:
            print(n, n // 63)

#CРЕЗАМИ
for i in range(134030, 10**6):
    n = str(i)
    if n[:3] == "134" and n[-2] == "3":
        if i % 63 == 0:
            print(i, i // 63)