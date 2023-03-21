import os
import numpy as np
import control as ct
import matplotlib.pyplot as plt 
from control.matlab import *

# Clear the screen
os.system("cls")
# define the transfer function
sys = tf([10],[1,1])
print(sys)
# plot the unitary step response
plt.figure("Step response")
sys2= ct.step_response(sys)
plt.plot(sys2.time,sys2.outputs)
plt.plot(sys2.time,sys2.inputs)
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.title('Step Response')

# define the ramp response
plt.figure("Ramp response")
t = np.linspace(0, 10, 1000)
ramp= ct.forced_response(sys, T=t, U=t) # type: ignore
# Plot the response
plt.plot(ramp.time,ramp.outputs)
plt.plot(ramp.time,ramp.inputs)
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.title('Ramp Response')

#define quadratic response
plt.figure("Quadratic response")
y = [x**2 for x in t]
quad = ct.forced_response(sys, T=t, U=y) # type: ignore
plt.plot(quad.time,quad.outputs)
plt.plot(quad.time,quad.inputs)
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.title('Quadratic Response')

#define impulse response
plt.figure("Impulse response")
impulse_input = np.zeros_like(t)
impulse_input[0] = 10
# Compute the system response to the impulse input
imp= ct.impulse_response(sys, T=t, X0=0)
# Plot the response
plt.plot(imp.time,imp.outputs)
plt.plot(imp.time,impulse_input)
plt.xlabel('Time')
plt.ylabel('Output')
plt.show()