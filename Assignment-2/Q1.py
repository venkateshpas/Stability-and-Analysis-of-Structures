import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

C1,C2,C3,C4,k,x,L= sp.symbols('C1 C2 C3 C4 k x L',real = True)
w1 = C1*sp.sin(k*x)+C2*sp.cos(k*x)+C3*x + C4
w1_1 = sp.diff(w1,x)
w1_2 = sp.diff(w1_1,x)
w1_3 = sp.diff(w1_2,x)
# print(w1_1.subs({x: L}))

eq = sp.integrate((C1*sp.sin(4.4934*x/L)+C3*x)**2,(x,0,L))
eq = eq.subs({C3: -C1*np.sin(4.493)/L})
print(eq)
L = 100
x = np.linspace(0,L,100)

w1 = (1/np.sqrt(0.794*L))*np.sin(4.4934*x/L)+np.sqrt(6/(5*L**3))*x

plt.figure(figsize = (8,6))
plt.plot(x,w1,color='blue',label='n=1')
plt.xlabel('Length of the beam')
plt.ylabel('mode shape')
plt.title('For clamped-pinned case')
plt.legend()  # Show legend
plt.grid(True)  # Show grid
plt.show()