import numpy as np
import control
import numpy as np
import os
import matplotlib.pyplot as plt

os.system("cls")

# Define the system
sys = control.tf([1], [1, 1])

# Define the time vector
t = np.linspace(0, 10, 1000)

# Define the input vector (impulse)
impulse_input = np.zeros_like(t)
impulse_input[0] = 1

# Compute the system response to the impulse input
y= control.impulse_response(sys, T=t, X0=0)

# Plot the response
plt.plot(y.time,y.outputs)
plt.plot(y.time,impulse_input)
plt.xlabel('Time')
plt.ylabel('Output')
plt.show()