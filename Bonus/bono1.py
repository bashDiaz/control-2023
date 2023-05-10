import numpy as np
import matplotlib.pyplot as plt
import control as ct
import pandas as pd
import math

# Carga el archivo CSV en un DataFrame
dataframe = pd.read_csv('example_P3.csv')

# Imprime el DataFrame
mag = dataframe['Mag']
phase = dataframe['Phase']
omega = dataframe["W"]

# Convierte los datos de magnitud y fase a dB y radianes
mag_db = 20*np.log10(mag)
phase_rad = np.deg2rad(phase)

# Define la función de transferencia de tu sistema
sys = ct.TransferFunction([1], [1, 1])

# Calcula la respuesta de frecuencia de tu sistema
mag_bode, phase_bode, omega_bode = ct.bode(sys, omega)

# Grafica la respuesta de frecuencia del sistema y los datos experimentales
fig, (ax_mag, ax_phase) = plt.subplots(2, 1, sharex=True)
ax_mag.semilogx(omega_bode, mag_bode, label='Teórico')
ax_mag.semilogx(omega, mag_db, label='Experimental')
ax_mag.set_ylabel('Magnitud (dB)')
ax_mag.legend()

ax_phase.semilogx(omega_bode, np.rad2deg(phase_bode), label='Teórico')
ax_phase.semilogx(omega, phase, label='Experimental')
ax_phase.set_xlabel('Frecuencia (rad/s)')
ax_phase.set_ylabel('Fase (grados)')
ax_phase.legend()

plt.show()
