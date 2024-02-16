import ComplexAlgebra
import ComplexNum

print("Let's fucking start")

print("c1.a: ")
a = int(input())
print("\nc1.b: ")
b = int(input())

c1 = ComplexNum.ComplexNum(a, b)

print("\nc2.a: ")
a = int(input())
print("\nc2.b: ")
b = int(input())

c2 = ComplexNum.ComplexNum(a, b)

ComplexAlgebra.add(c1, c2)
ComplexAlgebra.mul(c1, c2)
ComplexAlgebra.sub(c1, c2)
ComplexAlgebra.div(c1, c2)
ComplexAlgebra.modulous(c1)
ComplexAlgebra.conjugate(c1)