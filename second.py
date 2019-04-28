
def specialPythagorean():
    a = 3
    b = 7
    c = 12
    for c in range(1, 1000):
        for b in range(1, c):
            a = 1000 - b - c
            if a < b < c and a ** 2 + b ** 2 == c ** 2:
                print(f"a**2 = {a**2} < b**2 = {b**2} = {a**2} + {b**2} = {c**2}")
                return a * b *c
    

specialPythagorean()
