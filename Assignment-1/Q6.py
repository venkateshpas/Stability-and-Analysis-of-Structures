import matplotlib.pyplot as plt

E = 200
v = 0.3
# Stress and strain data
strain_11 = []  # Example strain values
stress_11_q1 = []  # Example stress values
stress_11_q2 = []
i = 0
j = 0
while j<1000:
    strain_11.append(j)
    j=j+0.1

for x in strain_11:
    stress_11_q1.append(E*x*(1-v)/((1+v)*(1-2*v))/1000)
    stress_11_q2.append(E*x/1000)
    i = i+1
# Plotting stress-strain curve
plt.figure(figsize=(8, 6))
plt.plot(strain_11, stress_11_q1, marker='o', linestyle='-', color = 'blue', label = 'question 1')
plt.plot(strain_11, stress_11_q2, marker='o', linestyle='-', color = 'orange', label = 'question 2')

# Title and labels
plt.title('Stress-Strain Curve')
plt.xlabel('Strain')
plt.ylabel('Stress (MPa)')

plt.legend()
# Grid and display
plt.grid(True)
plt.tight_layout()
plt.show()
