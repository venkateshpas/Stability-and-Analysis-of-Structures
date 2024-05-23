import numpy as np
a = 1000
b = 1000
h = 100
v = 0.3
q0 = 500
E = 70e3

D = E*h**3/(12*(1-v**2))
w_galerkin = 16 * (a**4) * (b**4) * q0 /(np.pi**6 * (a**2+b**2)**2 * D)
print("The solution using single term in Galerkin methods is " + str(w_galerkin))
w_strong = 0

# for i in range(1,6):
#     for j in range(1,6):
#         q = 16 * q0 * (np.sin(i*np.pi/2))**2 * (np.sin(j*np.pi/2))**2 /(i * j * np.pi**2)
#         w_strong += q/(np.pi ** 4 * D * ((i/a)**2+(j/b)**2)**2)

# print(w_strong)

for i in range(1,100):
    q = 16 * q0 * (np.sin(i*np.pi/2))**2 * (np.sin(i*np.pi/2))**2 /(i * i * np.pi**2)
    w_old = w_strong
    w_strong += q/(np.pi ** 4 * D * ((i/a)**2+(i/b)**2)**2)
    print("The strong form displacement for " + str(i) + " terms is " + str(w_strong))
    if i % 2 != 0 and w_strong - w_old < 1e-4:
        print("The solution converged at " + str(i) + " terms")
        break
    else:
        continue
