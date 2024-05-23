import numpy as np
import matplotlib.pyplot as plt
#Case - 1 Linear spring
k1 = 1000
k2 = -500
k3 = 0
theta = np.linspace(-np.pi/2,np.pi/2,100)
theta_zero_1 = 0.1
theta_zero_2 = 0.15
theta_zero_3 = 0.2
theta_zero_4 = 0.25
theta_zero_5 = -0.1
theta_zero_6 = -0.15
theta_zero_7 = -0.2
theta_zero_8 = -0.25
L = 50
F = (k1*theta + k2 * theta**2 + k3 * theta**3) /(L*np.sin(theta))
F_1 = (k1*theta + k2 * theta**2 + k3 * theta**3) /(L*np.sin(theta+theta_zero_1))
F_2 = (k1*theta + k2 * theta**2 + k3 * theta**3) /(L*np.sin(theta+theta_zero_2))
F_3 = (k1*theta + k2 * theta**2 + k3 * theta**3) /(L*np.sin(theta+theta_zero_3))
F_4 = (k1*theta + k2 * theta**2 + k3 * theta**3) /(L*np.sin(theta+theta_zero_4))
F_5 = (k1*theta + k2 * theta**2 + k3 * theta**3) /(L*np.sin(theta+theta_zero_5))
F_6 = (k1*theta + k2 * theta**2 + k3 * theta**3) /(L*np.sin(theta+theta_zero_6))
F_7 = (k1*theta + k2 * theta**2 + k3 * theta**3) /(L*np.sin(theta+theta_zero_7))
F_8 = (k1*theta + k2 * theta**2 + k3 * theta**3) /(L*np.sin(theta+theta_zero_8))

colors = plt.cm.viridis(np.linspace(0, 1, 8))

plt.figure(figsize=(8, 6))  # Optional: Adjust the figure size
plt.plot(theta, F, '.', color='red',label='theta_zero_1= 0')
plt.plot(theta, F_1, '.', color=colors[0],label='theta_zero= 0.1')
plt.plot(theta, F_2, '.', color=colors[1],label='theta_zero= 0.15')
plt.plot(theta, F_3, '.', color=colors[2],label='theta_zero= 0.2')
plt.plot(theta, F_4, '.', color=colors[3],label='theta_zero= 0.25')
plt.plot(theta, F_5, '.', color=colors[4],label='theta_zero= -0.1')
plt.plot(theta, F_6, '.', color=colors[5],label='theta_zero= -0.15')
plt.plot(theta, F_7, '.', color=colors[6],label='theta_zero= -0.2')
plt.plot(theta, F_8, '.', color=colors[7],label='theta_zero= -0.25')
plt.ylim(0,100)
plt.xlabel('Theta')
plt.ylabel('Force')
plt.title('Linear spring Buckling curve K1>0, k2= ' + str(k2) +',k3=' +str(k3))
plt.legend()  # Show legend
plt.grid(True)  # Show grid
plt.show()
