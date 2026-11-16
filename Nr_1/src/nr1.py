#  created on 16. Nov. 2026
#  Solution to Exercise 1

import matplotlib.pyplot as plt
import numpy as np
import scipy

boundarys = [0, 1]

def solve_all(n):
    h = 1/n
    aa = np.zeros((n, n))
    # ----- write the matirx elements of A ------
    for i in range(0, n):
        aa[i, i] = 1/h * 2
        if i < n-1:
            aa[i+1, i] = -1/h
        if i > 0:
            aa[i-1, i] = -1/h
    # -------------------------------------------
    
    solve_1(n, h, aa)
    

        

def solve_1(n, h, aa):
    def real_solution_1(x):
        xx = x.copy()
        yy = np.zeros(1000)
        print(np.shape(x[0]))
        for j in range(np.shape(x)[0]):
            print(xx[j])
            yy[j] = -1/2 * (xx[j] - 1/2)**2 + 1/8
            yy[j]
        return yy

    bb = np.zeros(n) # right side b
    for i in range(n):
        bb[i] = h

    uu = np.linalg.solve(aa, bb) # Solution u of Au = b

    xx = np.zeros(n)
    for j in range(n):
        xx[j] = j * h

    xx_real = np.linspace(0, 1, 1000)
    yy_real = real_solution_1(xx_real)
    
    plt.title(f'FEM Exercise - f = 1, n={n}')
    plt.xlabel('x')
    plt.ylabel('u')
    
    plt.plot(xx_real, yy_real, label='Algebraic Solution')
    plt.plot(xx, uu, linestyle='--', color='red', linewidth=3, label='FEM Solution')
    plt.legend()
    plt.show()
    

def sovle_2():
    pass

def solve_3():
    pass

solve_all(1000)