from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import pandas as pd
from scipy.optimize import curve_fit
import os
import control as ct


os.system("cls")
# Función para cargar el archivo
def load_file():
    file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Matlab files", "*.mat"), ("CSV files", "*.csv")])
    return file_path

# Función para obtener los parámetros de tiempo y respuesta
def get_param(file_path):
    data = loadmat(file_path)
    t = data['t'].ravel()
    y = data['y'].ravel()
    return t, y

def transfer_function(t, K, tau1, tau2, theta):
    return K*(1 - np.exp((-1)*t/tau1))*(np.exp((-1)*t/tau2))*(t >= theta)

def sys_function(t, K, tau1, tau2):
    num = [K]
    den = [tau1*tau2, tau1+tau2, 1]
    sys = ct.TransferFunction(num, den)
    print(sys)
# Loop principal
if __name__ == "__main__":
    file_path = load_file()
    data = loadmat(file_path)
    #t, y = get_param(file_path)
    t = data['t'].ravel()
    y = data['y'].ravel()
    p0 = [1, 1, 1, 0]
    params, _ = curve_fit(transfer_function, t, y, p0=p0)
    K, tau1, tau2, theta = params
    sys_function(t, K, tau1, tau2)
    TF = transfer_function(t, K, tau1, tau2, theta)
 