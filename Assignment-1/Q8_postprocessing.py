import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

a = 1000
b = 1000
h = 100
v = 0.3
q = 500
E = 70e3
D = E * h**3/(12*(1-v**2))
x = sp.symbols('x',real = True)
y = sp.symbols('y',real = True)
z = sp.symbols('z',real = True)

c = 16 * a**4 * b**4 *q/(np.pi**6 * (a**2+b**2)**2*D)
w = c * sp.sin(np.pi*x/a)*sp.sin(np.pi*y/b)
u1 = -c*np.pi*(-h/2)*np.cos(np.pi*x/a)*np.sin(np.pi*y/b)/a
u2 = -c*np.pi*(-h/2)*np.sin(np.pi*x/a)*np.cos(np.pi*y/b)/b

w_np = sp.lambdify((x, y), w, 'numpy')
u1_np = sp.lambdify((x, y), u1, 'numpy')
u2_np = sp.lambdify((x, y), u2, 'numpy')
# Generate x and y values
x_values = np.linspace(0, a, 100)
y_values = np.linspace(0, b, 100)

# Create a meshgrid from x and y values
X, Y = np.meshgrid(x_values, y_values)

# Evaluate the function on the meshgrid
Z = w_np(X, Y)
u1 = u1_np(X, Y)
u2 = u2_np(X, Y)

# Plot the function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('w(x, y)')
ax.set_title('3D Surface Plot of w(x, y)')

plt.show()

plt.figure()
plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Contour plot of w(x, y)')
plt.show()