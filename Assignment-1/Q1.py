import numpy as np
import math

stress = np.array([[150,110,70],[110,160,0],[70,0,-140]])
eigvals, eigvecs = np.linalg.eig(stress)
# print("The eigen values are",eigvals)
# print("The eigen vectors are", eigvecs)
# eigvecs1 = -1*eigvecs[:,0]
# eigvecs2 = eigvecs[:,1]
# eigvecs3 = eigvecs[:,2]

eigvecs1 = np.array([[0.7051,0.6989,0.1201]])
eigvecs2 = np.array([[0.6637,-0.7099,0.2356]])
eigvecs3 = np.array([[-0.2499,0.0864,0.9644]])

print(np.cross(eigvecs1,eigvecs2))

# #von mises stress
# stress_von = math.sqrt(0.5*((eigvals[0]-eigvals[1])**2+(eigvals[1]-eigvals[2])**2+(eigvals[2]-eigvals[0])**2))

# #tresca criteria
# stress_tres_1 = abs(eigvals[0]-eigvals[1])
# stress_tres_2 = abs((eigvals[1]-eigvals[2]))
# stress_tres_3 = abs((eigvals[2]-eigvals[0]))
# stress_tres = 0
# if stress_tres_1>=stress_tres_2:
#     if stress_tres_1>=stress_tres_3:
#         stre_tres = 0.5 * stress_tres_1
#     else:
#         stress_tres= 0.5 * stress_tres_3
# else:
#     if stress_tres_2>=stress_tres_3:
#         stre_tres = 0.5 * stress_tres_2
#     else:
#         stress_tres = 0.5 * stress_tres_3

# print(stress_von)
# print(stress_tres)