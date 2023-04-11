import control as ct
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

def TF(k):
    num = [14*k, 38*k, (66*k+2*k), 40*k, 0]
    den = [1, 6, 13, (6*k+20), 6*k]
    sys = ct.tf(num, den)
    return sys

# Función para actualizar el gráfico en cada frame de la animación
def update(frame):
    ax.clear()
    sys1 = TF(k[frame])
    lgr_curve.append(ct.rlocus(sys1))
    ax.set_xlabel("Parte Real")
    ax.set_ylabel("Parte Imaginaria")
    ax.set_title('Lugar Geométrico de las Raíces')
    return lgr_curve

def save_animation(ani):
    # Exportar la animación como un archivo PNG
    ani.save("animation.png", dpi=300)

if __name__ == "__main__":
    os.system("cls")

    sys2 = TF(1)
    plt.savefig('K', dpi=300)

    # Crear la figura y el eje
    fig, ax = plt.subplots()

    val = input("hasta que valor de k desea graficar? : \n >",)

    k = [i+1 for i in range(int(val))]


    # Crear una lista para guardar la curva del LGR en cada iteración
    lgr_curve = []

    # Crear la animación
    ani = animation.FuncAnimation(fig, update, frames=len(k), interval=50, repeat=False)

    # Mostrar el gráfico en una ventana emergente
    plt.show()

    # Guardar la animación en un archivo PNG
    save_animation(ani)
