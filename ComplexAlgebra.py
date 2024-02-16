import ComplexNum
import math

c3 = ComplexNum

def add(c1, c2):
    c3.a = c1.a + c2.a
    c3.b = c1.b + c2.b
    print(f"({c1.a}, {c1.b}) + ({c2.a}, {c2.b}) = ({c3.a}, {c3.b})")

def sub(c1, c2):
    c3.a = c1.a - c2.a
    c3.b = c1.b - c2.b
    print(f"({c1.a}, {c1.b}) - ({c2.a}, {c2.b}) = ({c3.a}, {c3.b})")

def mul(c1, c2):
    c3.a = c1.a * c2.a - c1.b * c2.b
    c3.b = c1.a * c2.b + c2.a * c1.b
    print(f"({c1.a}, {c1.b}) x ({c2.a}, {c2.b}) = ({c3.a}, {c3.b})")

def div(c1, c2):
    c3.a = (c1.a * c2.a + c1.b * c2.b) / (c2.a**2 + c2.b**2)
    c3.b = (c2.a * c1.b - c1.a * c2.b) / (c2.a**2 + c2.b**2)
    print(f"({c1.a}, {c1.b}) / ({c2.a}, {c2.b}) = ({c3.a}, {c3.b})")

def modulous(c):
    modc = math.sqrt(c.a**2 + c.b**2)
    print(f"The modulous for ({c.a}, {c.b} is: {modc})")

#Geometric name: real-axis reflection
def conjugate(c):
    c.b = -1 * c.b
    print(f"The Complex Conjugate for c1 is: {conc.a}, {conc.b}")