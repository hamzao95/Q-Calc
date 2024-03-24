from ComplexNum import ComplexNum
import math

c3 = ComplexNum

def add(c1, c2):
    c3.a = c1.a + c2.a
    c3.b = c1.b + c2.b
    print(f"({c1.a}, {c1.b}) + ({c2.a}, {c2.b}) = ({c3.a}, {c3.b})")
    return c3

def sub(c1, c2):
    c3.a = c1.a - c2.a
    c3.b = c1.b - c2.b
    print(f"({c1.a}, {c1.b}) - ({c2.a}, {c2.b}) = ({c3.a}, {c3.b})")
    return c3

def mul(c1, c2):
    c3.a = c1.a * c2.a - c1.b * c2.b
    c3.b = c1.a * c2.b + c2.a * c1.b
    print(f"({c1.a}, {c1.b}) x ({c2.a}, {c2.b}) = ({c3.a}, {c3.b})")
    return c3

def div(c1, c2):
    c3.a = (c1.a * c2.a + c1.b * c2.b) / (c2.a**2 + c2.b**2)
    c3.b = (c2.a * c1.b - c1.a * c2.b) / (c2.a**2 + c2.b**2)
    print(f"({c1.a}, {c1.b}) / ({c2.a}, {c2.b}) = ({c3.a}, {c3.b})")
    return c3

def modulus(c):
    modc = math.sqrt(c.a**2 + c.b**2)
    print(f"The modulous for ({c.a}, {c.b} is: {modc})")
    return modc

#Geometric name: real-axis reflection
def conjugate(c):
    conc = ComplexNum(c.a,(-1 * c.b))
    print(f"The Complex Conjugate for c1 is: {conc.a}, {conc.b}")
    return c

def ToPolar(c):
    polarc = ComplexNum(modulus(c),math.degrees(math.atan(c.a/c.b)))
    print(f"polar representation of c1 is rho = {polarc.a} and theta = {polarc.b}")

def ToCartesian(c):
    carc = ComplexNum((c.a * math.cos(c.b)),(c.a * math.sin(c.b)))
    print(f"cartesian representation of c1 is a = {carc.a} and b = {carc.b}")
