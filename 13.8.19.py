a = int(input("количество билетов"))
b = int(input("возраст"))
c = None
if b < 18:
    c = 0
    if 18 <= b <= 25:
        c = 990
        if b < 25:
            c = 1290
d = (c * a)
if 3 < a:
    d = "d-10%"
    print("d")
