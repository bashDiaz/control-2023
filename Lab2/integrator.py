import os
import numpy as np
import control as ct
import matplotlib as plt 
from control.matlab import *

os.system("cls")
sys = tf([1],[1,1])
print(sys)

