import numpy as np
from mpl_toolkits.mplot3d import Axes3D  
# Axes3D import has side effects, it enables using projection='3d' in add_subplot
import matplotlib.pyplot as plt
import random
import math


def generate_coeff():
        R1 = float(np.random.uniform (low = 0, high = 0.5, size = 1))
        S1 = float(np.random.uniform (low = 0, high = 0.5, size = 1))
        R2 = float(np.random.uniform (low = 0.5, high = 1, size = 1))
        S2 = float(np.random.uniform (low = 0.5, high = 1, size = 1))
        A = float(np.random.uniform (low = 0, high = 0.05, size = 1))
        Z = float(np.random.uniform (low = 0.25, high = 1, size = 1))
        return R1,S1,R2,S2,A,Z
    
R1,S1,R2,S2,A,Z = generate_coeff()
print(R1,S1,R2,S2,A,Z)

def fun(x, y):
    return (x**3)/3-(R1+S1)*(x**2)/2+(R1*S1)*x+(y**3)/3-(R2+S2)*(y**2)/2+(R2*S2)*y+A*np.vectorize(math.sin)((2*math.pi*x*y)/Z)


def generate_coeff_2():
        A1 = float(np.random.uniform (low = 20, high = 35, size = 1))
        A2 = float(np.random.uniform (low = 20, high = 35, size = 1))
        B1 = float(np.random.uniform (low = 0.5, high = 0.9, size = 1))
        B2 = float(np.random.uniform (low = 0.5, high = 0.9, size = 1))
        C = 10
        return A1,A2,B1,B2,C
    
A1,A2,B1,B2,C = generate_coeff_2()
print(A1,A2,B1,B2,C)

def fun_2(x, y):
    return C*(np.vectorize(math.sin)(A1*(abs(x-0.5)-B1)**4)*np.vectorize(math.cos)(2*abs(x-0.5)-B1)+((abs(x-0.5)-B1)/2))*(np.vectorize(math.sin)(A2*(abs(y-0.5)-B2)**4)*np.vectorize(math.cos)(2*abs(y-0.5)-B2)+((abs(y-0.5)-B2)/2))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(0, 1, 0.05)
X, Y = np.meshgrid(x, y)
zs = np.array(fun_2(np.ravel(X), np.ravel(Y)))
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')

plt.show()