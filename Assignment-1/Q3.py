import numpy as np
import sympy as sp
import math

P = np.array([2,5,7])
Q = np.array([3,8,9])
x1 = sp.symbols('x1',real = True)
x2 = sp.symbols('x2',real = True)
x3 = sp.symbols('x3',real = True)
u1 = (x1**2+20)*10**-4
u2 = (2*x1*x2)*10**-3
u3 = (x3**2-x1*x2)*10**-4

du1 = u1 + sp.diff(u1,x1)*(Q[0]-P[0])+sp.diff(u1,x2)*(Q[1]-P[1])+sp.diff(u1,x3)*(Q[2]-P[2])
dup1 = u1.subs({x1: P[0],x2: P[1],x3: P[2]})
duq1 = du1.subs({x1: P[0],x2: P[1],x3: P[2]})
#duq1 = du1.subs({x1: Q[0],x2: Q[1],x3: Q[2]})
du2 = u2 + sp.diff(u2,x1)*(Q[0]-P[0])+sp.diff(u2,x2)*(Q[1]-P[1])+sp.diff(u2,x3)*(Q[2]-P[2])
dup2 = u2.subs({x1: P[0],x2: P[1],x3: P[2]})
duq2 = du2.subs({x1: P[0],x2: P[1],x3: P[2]})
#duq2 = du2.subs({x1: Q[0],x2: Q[1],x3: Q[2]})
du3 = u3 + sp.diff(u3,x1)*(Q[0]-P[0])+sp.diff(u3,x2)*(Q[1]-P[1])+sp.diff(u3,x3)*(Q[2]-P[2])
dup3 = u3.subs({x1: P[0],x2: P[1],x3: P[2]})
duq3 = du3.subs({x1: P[0],x2: P[1],x3: P[2]})
#duq3 = du3.subs({x1: Q[0],x2: Q[1],x3: Q[2]})
P_deformed = [x + y for x, y in zip(P, [dup1,dup2,dup3])]
Q_deformed = [x + y for x, y in zip(Q, [duq1,duq2,duq3])]
print("3 part a")
print("The deformed coordinates of P are " +str(P_deformed))
print("The deformed coordinates of Q are " +str(Q_deformed))

Distance_PQ = np.sqrt((Q[0]-P[0])**2+(Q[1]-P[1])**2+(Q[2]-P[2])**2)
print("The distance of P and Q in the undeformed body is " +str(Distance_PQ))

Distance_PQ_deformed = math.sqrt((Q_deformed[0]-P_deformed[0])**2+(Q_deformed[1]-P_deformed[1])**2+(Q_deformed[2]-P_deformed[2])**2)
print("The distance of P and Q in the deformed body is " +str(Distance_PQ_deformed))

Relative_elongation = (Distance_PQ_deformed-Distance_PQ)/Distance_PQ
print("The relative elongation or the strain is given as " +str(Relative_elongation))

strain_tensor = np.array([[sp.diff(u1,x1).subs({x1: P[0],x2: P[1],x3: P[2]}),0.5*(sp.diff(u1,x2).subs({x1: P[0],x2: P[1],x3: P[2]})+sp.diff(u2,x1).subs({x1: P[0],x2: P[1],x3: P[2]})), 0.5*(sp.diff(u1,x3).subs({x1: P[0],x2: P[1],x3: P[2]})+sp.diff(u3,x1).subs({x1: P[0],x2: P[1],x3: P[2]}))],
                          [0.5*(sp.diff(u1,x2).subs({x1: P[0],x2: P[1],x3: P[2]})+sp.diff(u2,x1).subs({x1: P[0],x2: P[1],x3: P[2]})),sp.diff(u2,x2).subs({x1: P[0],x2: P[1],x3: P[2]}), 0.5*(sp.diff(u2,x3).subs({x1: P[0],x2: P[1],x3: P[2]})+sp.diff(u3,x2).subs({x1: P[0],x2: P[1],x3: P[2]}))],
                          [0.5*(sp.diff(u1,x3).subs({x1: P[0],x2: P[1],x3: P[2]})+sp.diff(u3,x1).subs({x1: P[0],x2: P[1],x3: P[2]})),0.5*(sp.diff(u2,x3).subs({x1: P[0],x2: P[1],x3: P[2]})+sp.diff(u3,x2).subs({x1: P[0],x2: P[1],x3: P[2]})), sp.diff(u3,x3).subs({x1: P[0],x2: P[1],x3: P[2]})]])

print("The strain tensor at point P with coordinates (2,5,7) is \n" + str(strain_tensor))

n_vector = [x - y for x, y in zip(Q, P)]
n_unit_vector = n_vector/np.linalg.norm(n_vector)
print("The unit vector n in direction of line PQ is given by \n" +str(n_unit_vector))

Relative_elongation_method2 = 0
for i in range(0,3):
    for j in range(0,3):
        Relative_elongation_method2 += strain_tensor[i][j] * n_unit_vector[i] * n_unit_vector[j]

print("The relative elongation or the strain using in class relation is given as " +str(Relative_elongation_method2))

#part B:
print("3 part b")
P_b = np.array([2,5,7])
Q_b = np.array([2.13363,5.40089,7.26726])
du1_b = u1 + sp.diff(u1,x1)*(Q_b[0]-P_b[0])+sp.diff(u1,x2)*(Q_b[1]-P_b[1])+sp.diff(u1,x3)*(Q_b[2]-P_b[2])
du2_b = u2 + sp.diff(u2,x1)*(Q_b[0]-P_b[0])+sp.diff(u2,x2)*(Q_b[1]-P_b[1])+sp.diff(u2,x3)*(Q_b[2]-P_b[2])
du3_b = u3 + sp.diff(u3,x1)*(Q_b[0]-P_b[0])+sp.diff(u3,x2)*(Q_b[1]-P_b[1])+sp.diff(u3,x3)*(Q_b[2]-P_b[2])
dup1_b = u1.subs({x1: P_b[0],x2: P_b[1],x3: P_b[2]})
duq1_b = du1_b.subs({x1: P_b[0],x2: P_b[1],x3: P_b[2]})
#duq1_b = du1_b.subs({x1: Q_b[0],x2: Q_b[1],x3: Q_b[2]})
dup2_b = u2.subs({x1: P_b[0],x2: P_b[1],x3: P_b[2]})
duq2_b = du2_b.subs({x1: P_b[0],x2: P_b[1],x3: P_b[2]})
#duq2_b = du2_b.subs({x1: Q_b[0],x2: Q_b[1],x3: Q_b[2]})
dup3_b = u3.subs({x1: P_b[0],x2: P_b[1],x3: P_b[2]})
duq3_b = du3_b.subs({x1: P_b[0],x2: P_b[1],x3: P_b[2]})
#duq3_b = du3_b.subs({x1: Q_b[0],x2: Q_b[1],x3: Q_b[2]})
P_deformed_b = [x + y for x, y in zip(P_b, [dup1_b,dup2_b,dup3_b])]
Q_deformed_b = [x + y for x, y in zip(Q_b, [duq1_b,duq2_b,duq3_b])]
print("The deformed coordinates of P are " +str(P_deformed_b))
print("The deformed coordinates of Q are " +str(Q_deformed_b))

Distance_PQ_b = np.sqrt((Q_b[0]-P_b[0])**2+(Q_b[1]-P_b[1])**2+(Q_b[2]-P_b[2])**2)
print("The distance of P and Q in the undeformed body is " +str(Distance_PQ_b))

Distance_PQ_deformed_b = math.sqrt((Q_deformed_b[0]-P_deformed_b[0])**2+(Q_deformed_b[1]-P_deformed_b[1])**2+(Q_deformed_b[2]-P_deformed_b[2])**2)
print("The distance of P and Q in the deformed body is " +str(Distance_PQ_deformed_b))

Relative_elongation_b = (Distance_PQ_deformed_b-Distance_PQ_b)/Distance_PQ_b
print("The relative elongation or the strain is given as " +str(Relative_elongation_b))

n_vector_b = [x - y for x, y in zip(Q_b, P_b)]
n_unit_vector_b = n_vector_b/np.linalg.norm(n_vector_b)
print("The unit vector n in direction of line PQ is given by \n" +str(n_unit_vector_b))

Relative_elongation_method2_b = 0
for i in range(0,3):
    for j in range(0,3):
        Relative_elongation_method2_b += strain_tensor[i][j] * n_unit_vector_b[i] * n_unit_vector_b[j]

print("The relative elongation or the strain using in class relation is given as " +str(Relative_elongation_method2_b))

# import math
# e11 = 4e-4
# e12 = 5e-3
# e13 = -2.5e-4
# e22 = 4e-3
# e23 = -1e-4
# e33 = 14e-4
# e21 = 5e-3
# e31 = -2.5e-4
# e32 = -1e-4

# x1 = 0.13363/0.5
# x2 = 0.40089/0.5
# x3 = 0.26726/0.5

# # x1 = 1/math.sqrt(14)
# # x2 = 3/math.sqrt(14)
# # x3 = 2/math.sqrt(14)

# strain = e11*x1*x1+e12*x1*x2+e13*x1*x3+e21*x2*x1+e22*x2*x2+e23*x2*x3+e31*x3*x1+e32*x3*x2+e33*x3*x3

# print(strain)

# PQx1= (2.13363+(2.13363**2+20)*10**-4)
# PQy1 = (5.40089+(2*2.13363*5.40089)*10**-3)
# PQz1 = (7.26726+(7.26726**2-2.13363*5.40089)*10**-4)


# # PQx1= (2.13363)
# # PQy1 = (5.40089)
# # PQz1 = (7.26726)
# PQ1 = math.sqrt(PQx1**2+ PQy1 **2+PQz1 **2)
# PQx = 2.0024
# PQy = 5.02
# PQz = 7.0039
# # PQx = 2
# # PQy = 5
# # PQz = 7
# PQ = math.sqrt(PQx **2 + PQy **2 + PQz **3)
# DistancePQ1 = math.sqrt((PQx1-PQx)**2+(PQy1-PQy)**2+(PQz1-PQz)**2)
# strain2 = (DistancePQ1-0.5)/0.5
# print(strain2)