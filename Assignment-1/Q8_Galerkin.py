import sympy as sp
import numpy as np


a = 1000
b = 1000
h = 100
v = 0.3
q = 500
E = 70e3
D = E * h**3/(12*(1-v**2))
x = sp.symbols('x',real = True)
y = sp.symbols('y',real = True)

number_terms = 5
w_old = np.array([0])
for i in range(1,100):
    number_terms = i
    for i in range(number_terms+1):
        variables_c = [sp.symbols(f'c{i}') for i in range(1, number_terms + 1)]
        variables_d = [sp.symbols(f'd{i}') for i in range(1, number_terms + 1)]

    w = 0
    dw = 0

    for i in range(number_terms+1):
        w += variables_c[i-1] * sp.sin(i*np.pi*x/a) * sp.sin(i*np.pi*y/b)
        dw += variables_d[i-1] * sp.sin(i*np.pi*x/a) * sp.sin(i*np.pi*y/b)

    w11 = sp.diff(sp.diff(w,x),x)
    w22 = sp.diff(sp.diff(w,y),y)
    w12 = sp.diff(sp.diff(w,x),y)
    dw11 = sp.diff(sp.diff(dw,x),x)
    dw22 = sp.diff(sp.diff(dw,y),y)
    dw12 = sp.diff(sp.diff(dw,x),y)
    variation_U = D*((w11+w22)*(dw11+dw22)-(1-v)*(w22*dw11+w11*dw22-2*w12*dw12))
    variation_U_integrate = sp.integrate(sp.integrate(variation_U, (y,0,b)),(x,0,a))
    variation_V = - q*dw
    variation_V_integrate = sp.integrate(sp.integrate(variation_V, (y,0,b)),(x,0,a))
    #variation_V_integrate = variation_V_integrate.args[0][0].as_expr()
    variation_PE_integrate = variation_U_integrate + variation_V_integrate
    equation = sp.Eq(variation_PE_integrate,0)
    equation = sp.simplify(equation)

    equations = []
    expr = equation.lhs
    for d in variables_d:
        equations.append(sp.collect(expr,d).coeff(d))
    c_galerkin = sp.linsolve(equations,variables_c)
    list_from_finite_set = list(c_galerkin)
    c_galerkin = list_from_finite_set[0]    
    w_galerkin = sum(element for element in c_galerkin)
    print("The Galerkin displacement for " + str(i) + " terms is " + str(w_galerkin))
    if i % 2 != 0 and w_galerkin - w_old < 1e-4:
        print("The solution converged at " + str(i) + " terms")
        break
    else:
        w_old = w_galerkin
        continue


# for i in range(number_terms+1):
#     variables_c = [sp.symbols(f'c{i}') for i in range(1, number_terms + 1)]
#     variables_d = [sp.symbols(f'd{i}') for i in range(1, number_terms + 1)]

# w = 0
# dw = 0

# for i in range(number_terms+1):
#     w += variables_c[i-1] * sp.sin(i*np.pi*x/a) * sp.sin(i*np.pi*y/b)
#     dw += variables_d[i-1] * sp.sin(i*np.pi*x/a) * sp.sin(i*np.pi*y/b)

# print(w)
# print(dw)
# w11 = sp.diff(sp.diff(w,x),x)
# w22 = sp.diff(sp.diff(w,y),y)
# w12 = sp.diff(sp.diff(w,x),y)
# dw11 = sp.diff(sp.diff(dw,x),x)
# dw22 = sp.diff(sp.diff(dw,y),y)
# dw12 = sp.diff(sp.diff(dw,x),y)
# variation_U = D*((w11+w22)*(dw11+dw22)-(1-v)*(w22*dw11+w11*dw22-2*w12*dw12))
# variation_U_integrate = sp.integrate(sp.integrate(variation_U, (y,0,b)),(x,0,a))
# variation_V = - q*dw
# variation_V_integrate = sp.integrate(sp.integrate(variation_V, (y,0,b)),(x,0,a))
# #variation_V_integrate = variation_V_integrate.args[0][0].as_expr()
# variation_PE_integrate = variation_U_integrate + variation_V_integrate
# equation = sp.Eq(variation_PE_integrate,0)
# equation = sp.simplify(equation)

# equations = []
# expr = equation.lhs
# for d in variables_d:
#     print(d)
#     equations.append(sp.collect(expr,d).coeff(d))

# print(equations)
# solution = sp.linsolve(equations,variables_c)
# # solution = sp.solve(equation,variables_c)
# print(solution)

##variables and displacements for one term
# c = sp.symbols('c',real = True)
# d = sp.symbols('d',real = True)
# w = c * sp.sin(np.pi*x/a) * sp.sin(np.pi*y/b) #defining the displacement variable
# dw = d * sp.sin(np.pi*x/a) * sp.sin(np.pi*y/b)#define the virtual displacement here later
# w11 = sp.diff(sp.diff(w,x),x)
# w22 = sp.diff(sp.diff(w,y),y)
# w12 = sp.diff(sp.diff(w,x),y)
# dw11 = sp.diff(sp.diff(dw,x),x)
# dw22 = sp.diff(sp.diff(dw,y),y)
# dw12 = sp.diff(sp.diff(dw,x),y)
# variation_U = D*((w11+w22)*(dw11+dw22)-(1-v)*(w22*dw11+w11*dw22-2*w12*dw12))
# variation_U_integrate = sp.integrate(sp.integrate(variation_U, (y,0,b)),(x,0,a))
# variation_U_integrate = sp.simplify(variation_U_integrate)
# variation_V = - q*dw
# variation_V_integrate = sp.integrate(sp.integrate(variation_V, (y,0,b)),(x,0,a))
# #variation_V_integrate = variation_V_integrate.args[0][0].as_expr()
# variation_PE_integrate = variation_U_integrate + variation_V_integrate
# equation = sp.Eq(variation_PE_integrate,0)
# solution = sp.solve(equation,c)
# print(solution)

# #variables and displacements for two term
# c1 = sp.symbols('c1',real = True)
# d1 = sp.symbols('d1',real = True)
# c2 = sp.symbols('c2',real = True)
# d2 = sp.symbols('d2',real = True)
# w = c1 * sp.sin(np.pi*x/a) * sp.sin(np.pi*y/b) + c2 * sp.sin(2*np.pi*x/a) * sp.sin(2*np.pi*y/b)#defining the displacement variable
# dw = d1 * sp.sin(np.pi*x/a) * sp.sin(np.pi*y/b) + d2 * sp.sin(2*np.pi*x/a) * sp.sin(2*np.pi*y/b)#define the virtual displacement here later

# w11 = sp.diff(sp.diff(w,x),x)
# w22 = sp.diff(sp.diff(w,y),y)
# w12 = sp.diff(sp.diff(w,x),y)
# dw11 = sp.diff(sp.diff(dw,x),x)
# dw22 = sp.diff(sp.diff(dw,y),y)
# dw12 = sp.diff(sp.diff(dw,x),y)

# #print(dw12)
# # PE = (w11+w22)**2-2*(1-v)*(w11*w12-(w12)**2)
# # print(PE)

# variation_U = D*((w11+w22)*(dw11+dw22)-(1-v)*(w22*dw11+w11*dw22-2*w12*dw12))
# variation_U_integrate = sp.integrate(sp.integrate(variation_U, (y,0,b)),(x,0,a))
# variation_U_integrate = sp.simplify(variation_U_integrate)
# variation_V = - q*dw
# variation_V_integrate = sp.integrate(sp.integrate(variation_V, (y,0,b)),(x,0,a))
# #variation_V_integrate = variation_V_integrate.args[0][0].as_expr()
# variation_PE_integrate = variation_U_integrate + variation_V_integrate
# equation = sp.Eq(variation_PE_integrate,0)
# solution = sp.solve(equation,c1,c2)
# print(solution)

