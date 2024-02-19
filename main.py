import ComplexAlgebra
from ComplexNum import ComplexNum

print("Let's fucking start")

print("c1.a: ")
a = float(input())
print("\nc1.b: ")
b = float(input())

c1 = ComplexNum(a, b)

print("\nc2.a: ")
a = float(input())
print("\nc2.b: ")
b = float(input())

c2 = ComplexNum(a, b)

ComplexAlgebra.add(c1, c2)
ComplexAlgebra.mul(c1, c2)
ComplexAlgebra.sub(c1, c2)
ComplexAlgebra.div(c1, c2)
ComplexAlgebra.modulus(c1)
ComplexAlgebra.conjugate(c1)
ComplexAlgebra.ToPolar(c1)
ComplexAlgebra.ToCartesian(c1)