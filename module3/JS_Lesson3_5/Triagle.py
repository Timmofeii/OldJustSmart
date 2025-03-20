class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        a = self.a
        b = self.b
        c = self.c
        return a + b + c

    def type(self):
        a1 = self.a
        b1 = self.b
        c1 = self.c
        c = max(a1, b1, c1)
        b = min(a1, b1, c1)
        a = sum([a1, b1, c1]) - min(a1, b1, c1) - max(a1, b1, c1)
        if c >= a + b:
            print('impossible')
        elif c ** 2 == a ** 2 + b ** 2:
            print('rectangular')
        elif c ** 2 < a ** 2 + b ** 2:
            print('acute')
        elif c ** 2 > a ** 2 + b ** 2:
            print('obtuse')
