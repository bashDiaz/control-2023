import control as ct
import numpy as np
import matplotlib.pyplot as plt
import os


def plot_step(sys,title):
    sys2= ct.step_response(sys)
    plt.figure(title)
    plt.plot(sys2.time,sys2.outputs)
    plt.plot(sys2.time,sys2.inputs)
    plt.xlabel('Time (s)')
    plt.ylabel('Output')
    plt.grid()

def TF(k,a):
    num = [k, a*k]
    den = [1, 8, 17, k+10, a*k]
    sys = ct.TransferFunction(num, den)
    print(sys)
    return sys

# Definimos las variables K y a para realizar el grafico
def f(k, a):
    return (k**2 + (64*a - 116)*k - 1260)/(k - 126)

if __name__ == "__main__":
    
    # Clear the screen
    os.system("cls")

    # Crear valores de k y a
    k = np.linspace(1, 500, 350)
    a = k

    # Crear una máscara booleana para seleccionar solo los valores de k y a que cumplen con la condición a>0 y k>126
    mask = (a > 0) & (k < 126)

    # Tracer la función solo para los valores de k y a que cumplen con la condición a>0 y k>126
    plt.plot(k[mask], f(k[mask], a[mask]), label="K vs a")
    plt.savefig('K_vs_A', dpi=300)

    # Agregar etiquetas de eje y título de la gráfica
    plt.xlabel("k")
    plt.ylabel("a")
    plt.grid()
    plt.title('Gráfico de K vs a')

    a_op = 0
    k_op = 0
    time = 10000000000
    times = []
    for i in range(len(k)):
        for j in range(len(a)):
            if  ( 10/(k[i]*a[j]) <=0.24 ) and (k[i] < 126) and (a[j] >= 0 and a[j] <= 200):
                sys1 = TF(k[i],a[j])
                try:
                    info = ct.step_info(sys1)
                    if not np.isnan(info['SettlingTime']):
                        times.append(info['SettlingTime'])
                        if info['SettlingTime'] < time:
                            print("Entrada", i, " Time: ", info['SettlingTime'])
                            k_op = k[i]
                            a_op = a[j]
                            time = info['SettlingTime']
                except:
                    pass
    if k_op == 0 and a_op == 0:
        print("No se encontró un sistema estable")

    print("K: ", k_op, " a: ", a_op, " Time: ", time)
    print(times)

    #Definimos el sistema inestable
    Isys = TF(127,0)
    plot_step(Isys,"Inestable Step response")
    plt.savefig('Inestable_Step_Response.png', dpi=300)

    #Definimos el sistema estable
    Esys = TF(k_op,a_op)
    plot_step(Esys,"Estable Step response")
    plt.savefig('Estable_Step_Response.png', dpi=300)

    plt.show()
