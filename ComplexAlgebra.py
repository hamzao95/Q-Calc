import ComplexNum

c3 = ComplexNum

def add(c1, c2):
    print(f'c1.a: {c1.a}\nc1.b: {c1.b}\nc2.a: {c2.a}\nc2.b: {c2.b}')
    c3.a = c1.a + c2.a
    c3.b = c1.b + c2.b
    print(c3.a, c3.b)

def mul(c1, c2):
    c3.a = c1.a * c2.a - c1.b * c2.b
    c3.b = c1.a * c2.b + c2.a * c1.b
    print(c3.a, c3.b)