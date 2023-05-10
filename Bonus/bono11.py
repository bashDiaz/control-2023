import numpy as np
import matplotlib.pyplot as plt
import control as ct
import pandas as pd


# Carga el archivo CSV en un DataFrame
dataframe = pd.read_csv('example_P3.csv')

# Define los datos experimentales
mag = dataframe['Mag']
phase = dataframe['Phase']
omega = dataframe["W"]

# Convertir a db
mag = 20*np.log10(mag)

fig, (ax_mag, ax_phase) = plt.subplots(2, 1)
ax_mag.semilogx(omega, mag)
ax_mag.set_ylabel('Magnitude (dB)')
ax_mag.set_title('Bode Plot')
ax_mag.set_xlabel('Frequency (rad/s)')
ax_mag.grid(True)

ax_phase.semilogx(omega, (phase))
ax_phase.set_ylabel('Phase (deg)')
ax_phase.set_xlabel('Frequency (rad/s)')
ax_phase.grid(True)
plt.show()