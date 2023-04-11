import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load data from a .mat file
mat_contents = sio.loadmat('pruebalab.mat')
time = mat_contents['t'].ravel().tolist()
response = mat_contents['y'].ravel().tolist()

# Plot the response
plt.plot(time, response)
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Step response of the system')
plt.show()

# Determine if the system is underdamped or overdamped
peaks, _ = find_peaks(response)
if len(peaks) == 1:
    print('The system is critically damped')
elif len(peaks) == 2:
    print('The system is overdamped')
else:
    print('The system is underdamped')

# Fit a transfer function to the data
# Fit a transfer function to the data
from scipy.optimize import curve_fit

def transfer_function(t, K, tau1, tau2, theta):
    return K*(1 - np.exp((-1)*t/tau1))*(np.exp((-1)*t/tau2))*np.broadcast_to((t >= theta), t.shape)

p0 = [1, 1, 1, 0]
params, _ = curve_fit(transfer_function, np.array(time), np.array(response), p0=p0)

K, tau1, tau2, theta = params
print('Transfer function: G(s) = {:.2f}/(s + {:.2f})exp(-{:.2f}s)'.format(K, tau1, tau2))
print('Dead time: {:.2f}s'.format(theta))

# Calculate the step response of the fitted transfer function
step_time = np.linspace(0, time[-1], 1000)
step_response = K*(1 - np.exp((-1)*(step_time-theta)/tau1))*np.exp((-1)*(step_time-theta)/tau2)

# Plot the original and fitted step response
plt.plot(time, response, label='Original response')
plt.plot(step_time, step_response, label='Fitted response')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Comparison of original and fitted step response')
plt.legend()
plt.show()

# Calculate the performance index
def ise(y_true, y_pred):
    return np.sum(np.square(y_true - y_pred))

def itse(y_true, y_pred, t):
    return np.sum(np.square(t)*(y_true - y_pred)**2)

def itae(y_true, y_pred, t):
    return np.sum(np.abs(t)*(y_true - y_pred))

true_response = response
predicted_response = transfer_function(np.array(time), *params)
index = ise(true_response, predicted_response)  # You can use ISE, ITSE or ITAE here
similarity = 100*(1 - index/np.sum(np.square(true_response - np.mean(true_response))))
print('Similarity between model and real system: {:.2f}%'.format(similarity))

# Save the transfer function to a file
import control

num = [K]
den = [tau1*tau2, tau1+tau2, 1]
sys = control.TransferFunction(num, den)
