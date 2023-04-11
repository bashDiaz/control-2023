import matplotlib.pyplot as plt
import os
import math

#limpiar pantalla
os.system("cls")

dic = {}
#definir parametros
pol = input("Defina los numeros que acompanan las S empezando por el de mayor grado  y separando espacio Empieza: ")
pol = pol.split(" ")
pol = [int(i) for i in pol]

for i in range(len(pol)):
    vec = []
    dic["s"+str(i)] = vec

for i in range(len(pol)):
    if i%2 == 0:
        dic["s"+str(len(pol)-1)].append(pol[i])
    else:
        dic["s"+str(len(pol)-2)].append(pol[i])

for i in range(len(pol)-3,-1,-1):
    vec1 = dic["s"+str(i+2)]
    vec2 = dic["s"+str(i+1)]
    vec3 = []
    for j in range(len(vec1)):
        try:
            val = ((vec2[0]*vec1[j+1])-(vec1[0]*vec2[j+1]))/vec2[0]
            vec3.append(val)
        except IndexError:
            vec3.append(0)
    dic["s"+str(i)] = vec3

est = []

for i in range(len(pol)-1,-1,-1):
    est.append(dic["s"+str(i)][0])
    vec = dic["s"+str(i)]
    for j in range (len(vec)): 
        try:
            if (vec[j] == 0 or vec[j]==-0 or vec[j]== 0.0 or vec[j]==-0.0) and j != 0 :
                vec.pop(j)
        except IndexError:
            pass
    dic["s"+str(i)] = vec

for i in range(len(pol)-1,-1,-1):
    vec = dic["s"+str(i)]
    print("s"+str(i), end=" ")
    for j in range(len(vec)):
        print(vec[j], end=" ")
    print("")
        

ins = False
cri = False

for i in range(len(est)):
    if est[i] < 0:
        ins = True
    if est[i] == 0 and ins!=True:
        cri = True

if ins:
    print("El sistema es inestable")
elif cri:
    print("El sistema es critico")
else:
    print("El sistema es estable")