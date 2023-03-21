import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control as ct

os.system("cls")
sys = ct.tf([118.24**2],[1,2*118.24*0.5912,118.24**2])
print(sys)
t = np.linspace(0, 100, 1000)
step = ct.step_response(sys, T=t)

plt.figure(1)
plt.plot(step.time, step.outputs, label='Respuesta del sistema')
plt.plot(step.time, step.inputs, label='Entrada del sistema')
plt.xlabel('Tiempo (s)')
plt.ylabel('Salida del sistema')
plt.title('Respuesta del sistema a un escalón')
plt.grid()
plt.legend()

# Calcular los parámetros de estado transitorio
info = ct.step_info(sys)

# Agregar los parámetros de estado transitorio en la gráfica
plt.text(25, 0.25, f'Tiempo de subida: {info["RiseTime"]:.2f} s')
plt.text(25, 0.20, f'Tiempo de asentamiento: {info["SettlingTime"]:.2f} s')
plt.text(25, 0.15, f'Sobreelongación: {info["Overshoot"]:.2f}%')
plt.text(25, 0.10, f'Valor de asentamiento: {info["SettlingMax"]:.2f}')
plt.text(25, 0.05, f'Tiempo de pico: {info["PeakTime"]:.2f} s')

# Agregar un cero al sistema
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
zero = ct.tf([a, b], [1, 0])
sys_with_zero = ct.series(zero, sys)
# Calcular la respuesta al escalón del sistema con el cero agregado
step_with_zero = ct.step_response(sys_with_zero, T=t)
plt.figure(2)
print(sys_with_zero)
info2 = ct.step_info(sys_with_zero)

# Agregar los parámetros de estado transitorio en la gráfica
plt.text(25, 50, f'Tiempo de subida: {info2["RiseTime"]:.2f} s')
plt.text(25, 40, f'Tiempo de asentamiento: {info2["SettlingTime"]:.2f} s')
plt.text(25, 30, f'Sobreelongación: {info2["Overshoot"]:.2f}%')
plt.text(25, 20, f'Valor de asentamiento: {info2["SettlingMax"]:.2f}')
plt.text(25, 10, f'Tiempo de pico: {info2["PeakTime"]:.2f} s')
# Agregar la respuesta del sistema con el cero agregado a la gráfica
plt.plot(step_with_zero.time, step_with_zero.outputs, label='Respuesta con cero agregado')
plt.plot(step.time, step.inputs, label='Entrada del sistema')
plt.xlabel('Tiempo (s)')
plt.ylabel('Salida del sistema')
plt.title('Respuesta del sistema a un escalón')
plt.grid()
plt.legend()
plt.show()
