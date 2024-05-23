import numpy as np
import matplotlib.pyplot as plt

def axial_deflection(L, F, E, A, num_points=100):
    x = np.linspace(0, L, num_points)  # Length of the beam
    displacement_ritz_galerkin = -8*F * L/ (np.pi*np.pi*E*A) * np.sin(np.pi*x/(2*L))  # Axial deflection equation using ritz/galerkin
    displacement_strong = -F*x/(E*A) #Axial deflection using strong formulation
    plt.figure(figsize=(8, 6))
    plt.plot(x, displacement_ritz_galerkin, color='blue', label='Axial Deflection using Ritz and Galerkin')
    plt.plot(x, displacement_strong, color='orange', label='Axial Deflection using strong formulation')
    plt.xlabel('Beam Length (mm)')
    plt.ylabel('Deflection (mm)')
    plt.title('Cumilative Axial Deflection along the Beam')
    plt.legend()
    plt.grid(True)
    plt.show()

def axial_strain(L, F, E, A, num_points=100):
    x = np.linspace(0, L, num_points)  # Length of the beam
    strain_ritz_galerkin = -4*F * np.cos(np.pi*x/(2*L)) / (np.pi * E * A)  # Axial strain Ritz/Galerkin
    value = -F/(E*A) #Axial strain strong formulation
    strain_strong = np.full(100, value)
    plt.figure(figsize=(8, 6))
    plt.plot(x, strain_ritz_galerkin, color='blue', label='Axial strain using Ritz and Galerkin')
    plt.plot(x, strain_strong, color='orange', label='Axial strain using strong formulation')
    plt.xlabel('Beam Length (mm)')
    plt.ylabel('Strain '+ r'$\epsilon_{11}$')
    plt.title('Strain along the length of the beam')
    plt.legend()
    plt.grid(True)
    plt.show()

def axial_stress11(L, F, E, A, v, num_points=100):
    x = np.linspace(0, L, num_points)  # Length of the beam
    stress_ritz_galerkin = (-4*F * (1-v) / (np.pi * A * (1+v)*(1-2*v)))* np.cos(np.pi*x/(2*L))  # Axial strain Ritz/Galerkin
    value = -F*(1-v)/(A*(1+v)*(1-2*v)) #Axial strain strong formulation
    stress_strong = np.full(100, value)
    plt.figure(figsize=(8, 6))
    plt.plot(x, stress_ritz_galerkin, color='blue', label='Axial stress '+ r'$\sigma_{11}$' + '  using Ritz and Galerkin')
    plt.plot(x, stress_strong, color='orange', label='Axial stress '+ r'$\sigma_{11}$' + '  using strong formulation')
    plt.xlabel('Beam Length (mm)')
    plt.ylabel('Stress '+ r'$\sigma_{11}$' + ' (MPa)')
    plt.title('Stress along the length of the beam')
    plt.legend()
    plt.grid(True)
    plt.show()

def axial_stress22(L, F, E, A, v, num_points=100):
    x = np.linspace(0, L, num_points)  # Length of the beam
    stress_ritz_galerkin = -4*F * np.cos(np.pi*x/(2*L)) * (v) / (np.pi * A * (1+v)*(1-2*v))   # Axial strain Ritz/Galerkin
    value = -F*(v)/(A*(1+v)*(1-2*v)) #Axial strain strong formulation
    stress_strong = np.full(100, value)
    plt.figure(figsize=(8, 6))
    plt.plot(x, stress_ritz_galerkin, color='blue', label='Axial stress '+ r'$\sigma_{22}$ or $\sigma_{33}$' + 'using Ritz and Galerkin')
    plt.plot(x, stress_strong, color='orange', label='Axial stress '+ r'$\sigma_{22}$ or $\sigma_{33}$' + ' using strong formulation')
    plt.xlabel('Beam Length (mm)')
    plt.ylabel('Stress '+ r'$\sigma_{22}$ or $\sigma_{33}$' + ' (MPa)')
    plt.title('Stress along the length of the beam')
    plt.legend()
    plt.grid(True)
    plt.show()

# Define beam parameters 
axial_force = 1000  # Axial force applied Newtons
E = 200e3  # Young's modulus (for steel, in MPa)
A = 100  # Area = b*h (10mm * 10mm square cross-section)
beam_length = 1000 #Length of the beam in millimeters (basically 1 m)
v =0.3
# Calculate and plot axial deflection
axial_deflection(beam_length, axial_force, E, A)
axial_strain(beam_length, axial_force, E, A)
axial_stress11(beam_length, axial_force, E, A, v)
axial_stress22(beam_length, axial_force, E, A, v)
