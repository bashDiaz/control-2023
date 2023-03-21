from scipy.io import loadmat
from scipy.integrate import odeint
from scipy.integrate import quad
from scipy.optimize import curve_fit
from scipy import signal
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
import control as ct
import os
from tkinter import filedialog

def transfer_function(t, k, tau1, tau2):
    return k/(tau1*t + tau2)



def get_response(file_path):
    data = loadmat(file_path)
    t = data['t'].ravel()
    y = data['y'].ravel()
    return t, y
def path():
    file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Matlab files", "*.mat"), ("CSV files", "*.csv")])
    return file_path

def sys_function(t, K, tau1, tau2):
    num = [K]
    den = [tau1*tau2, tau1+tau2, 1]
    sys = ct.TransferFunction(num, den)
    print(sys)

def kind(ls):
    max = 0
    for i in range(len(ls)):
        if ls[i] > max:
            max = ls[i]
    if max > ls[len(ls)-1]:
        print("The system is sub amortiguado")
    else:
        print("El sistema es sobre amortiguado")

def create_csv(t, y):
    df = pd.DataFrame({'t': t, 'y': y})
    df_csv = df.to_csv('pruebalab.csv', index=False)
    return df_csv


if __name__ == "__main__":

    os.system("cls")

    file_path = path()
    t, y = get_response(file_path)
    css = create_csv(t, y)
    ls = y.tolist()
    kind(ls)

    params, _ = curve_fit(transfer_function, t,y)
    K, tau1, tau2= params
    sys_function(t, K, tau1, tau2)
    TF = transfer_function(t, K, tau1, tau2)

    adjust, adjus = curve_fit(transfer_function, t, y)

    plt.show()