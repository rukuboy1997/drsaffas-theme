for i in range(10000):
    i = str(i)
    if len(i) == 1:
        print("000" + i)
    elif len(i) == 2:
        print("00" + i)
    elif len(i) == 3:
        print("0" + i)
    else:
        print(i)
