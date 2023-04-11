import numpy as np
import matplotlib.pyplot as plt

def routh(p, k=1):
    n = len(p)
    routh_table = np.zeros((n, (n+1)//2))
    routh_table[0, :] = p[0::2]
    if n%2 == 0:
        routh_table[1, :] = p[1::2]
    else:
        routh_table[1, :-1] = p[1::2]

    for i in range(2, n):
        for j in range((n+1)//2 - 1):
            a, b, c = routh_table[i-2, j], routh_table[i-1, j], routh_table[i-1, j+1]
            if b == 0:
                b = 1e-9 #avoid division by zero
            routh_table[i, j] = -c/b * a

        if np.all(np.isnan(routh_table[i])):
            print("Error: Polynomial has multiple roots on imaginary axis")
            return None

    num_sign_changes = np.sum(np.diff(np.sign(routh_table), axis=1) != 0, axis=1)
    unstable_roots = 0
    for nsc in num_sign_changes:
        if nsc % 2 != 0:
            unstable_roots += 1

    if unstable_roots == 0:
        print("System is stable for all values of K")
    elif unstable_roots == 1:
        print("System has 1 unstable root for some values of K")
    else:
        print("System has {} unstable roots for some values of K".format(unstable_roots))

    print("Routh table:")
    print(routh_table)
    
    # Polinomio roots
    roots = np.roots(p)
    print(f"Polynomial roots: {roots}")
    
    # Gráfica del polinomio en el plano imaginario
    plt.figure()
    plt.title("Polynomial roots")
    plt.xlabel("Real axis")
    plt.ylabel("Imaginary axis")
    np_roots = np.roots(p)
    plt.plot(np_roots.real, np_roots.imag, 'o')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.grid(True)
    plt.show()

# Ejemplo 1: Polinomio sin coeficientes nulos
p1 = [1, 5, 8, 6]
routh(p1, k=1)

# Ejemplo 2: Polinomio con coeficientes nulos
p2 = [1, 0, 3, 0, 2, 0]
routh(p2, k=2)

# Ejemplo 3: Polinomio con raíces imaginarias puras
p3 = [1, 2, 4, 2]
routh(p3, k=1.5)

# Ejemplo 4: Polinomio con raíces múltiples en el eje imaginario
p4 = [1, 2, 2, 2, 2]
routh(p4, k=3)

# Ejemplo 5: Polinomio con un caso especial del criterio de estabilidad de Routh
p5 = [1, 6, 5, -4]
routh(p5, k=1)