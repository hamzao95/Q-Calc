from ComplexNum import ComplexNum
import ComplexAlgebra as ca
import math
import numpy as np
import matplotlib.pyplot as plt
 
# Create a single vector
V = np.array([1,1])

i = ComplexNum(0, 1)

multiplied = ComplexNum(V[0], V[1])

multiplied = ca.mul(multiplied, i)

V[0] = multiplied.a

V[1] = multiplied.b

# naming the x axis
plt.xlabel('real')
# naming the y axis
plt.ylabel('imaginary')
 
# giving a title to my graph
plt.title('Complex Plane')

# Add the vector V to the plot
plt.quiver(0, 0, V[0], V[1], angles='xy', scale_units='xy', scale=1, color='r')

# Set the x-limits and y-limits of the plot
plt.xlim([-2, 2])
plt.ylim([-2, 2])

# Show the plot along with the grid
plt.grid()
plt.show()