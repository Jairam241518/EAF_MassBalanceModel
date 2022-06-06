import pandas as pd
import numpy as np
import csv
burnetLime = pd.read_csv("BurnetLime.csv")
carbon = pd.read_csv("Carbon.csv")
gases = pd.read_csv("Gases.csv")
hbi = pd.read_csv("HBI.csv")
scrap = pd.read_csv("Scrap.csv")
slag = pd.read_csv("Slag.csv")
steel = pd.read_csv("Steel.csv")
# HBI = hbi.to_dict('records')

# print(hbi['weight'].iat[0])
a1 = (hbi['FeTotal'].iat[0]*hbi['weight'].iat[0]) + (scrap['Fe'].iat[0]*scrap['weight'].iat[0]) + (0.7*scrap['FeO'].iat[0]*scrap['weight'].iat[0]) + (carbon['Fe'].iat[0]*carbon['weight'].iat[0])
a1 = a1/100
a2 = (hbi['SiO2'].iat[0]*hbi['weight'].iat[0]) + (scrap['SiO2'].iat[0]*scrap['weight'].iat[0]) + (carbon['SiO2'].iat[0]*carbon['weight'].iat[0])
a2 = a2/100
a3 = (hbi['CaO'].iat[0]*hbi['weight'].iat[0]) + (scrap['CaO'].iat[0]*scrap['weight'].iat[0]) + (carbon['CaO'].iat[0]*carbon['weight'].iat[0])
a3 = a3/100
# print(a1)
# print(a2)
# print(a3)
x1 = steel['Fe'].iat[0]/100
x2 = 0.007*slag['FeO'].iat[0]
y2 = (slag['SiO2'].iat[0])/100
y3 = -burnetLime['SiO2'].iat[0]/100
z2 = slag['CaO'].iat[0]/100
z3 = -burnetLime['CaO'].iat[0]/100
A = np.array([[x1, x2, 0], [0, y2, y3], [0, z2, z3]])
b = np.array([a1, a2, a3])
w = np.linalg.solve(A,b)
# print(w)
carbonGas = hbi['C'].iat[0]*hbi['weight'].iat[0] + scrap['C'].iat[0]*scrap['weight'].iat[0] + carbon['C'].iat[0]*carbon['weight'].iat[0] - steel['C'].iat[0]*w[0]
carbonGas = carbonGas/100
weightOfCO2 = 3.67*carbonGas
weightOfGases = weightOfCO2*2.82
# print(weightOfGases)
OxygenInputInFeO = hbi['O'].iat[0]*hbi['weight'].iat[0] + scrap['FeO'].iat[0]*0.22*scrap['weight'].iat[0]
OxygenInputInSiO2 = hbi['SiO2'].iat[0]*0.53*hbi['weight'].iat[0] + burnetLime['SiO2'].iat[0]*0.53*w[2] + scrap['SiO2'].iat[0]*0.53*scrap['weight'].iat[0] + carbon['SiO2'].iat[0]*0.53*carbon['weight'].iat[0]
OxygenInputInAl203 = hbi['Al2O3'].iat[0]*0.47*hbi['weight'].iat[0]
OxygenInputInCaO = hbi['CaO'].iat[0]*0.28*hbi['weight'].iat[0] + burnetLime['CaO'].iat[0]*w[2]*0.28 + scrap['CaO'].iat[0]*0.28*scrap['weight'].iat[0] + carbon['CaO'].iat[0]*0.28*carbon['weight'].iat[0]
OxygenInputInMgO = hbi['MgO'].iat[0]*0.4*hbi['weight'].iat[0] + burnetLime['MgO'].iat[0]*w[2]*0.4
OxygenInputInMnO = hbi['MnO'].iat[0]*0.225*hbi['weight'].iat[0]
OxygenInputInP2O5 = hbi['P2O5'].iat[0]*0.56*hbi['weight'].iat[0]
OxygenInput = OxygenInputInFeO + OxygenInputInCaO + OxygenInputInSiO2 + OxygenInputInAl203  + OxygenInputInMgO + OxygenInputInMnO + OxygenInputInP2O5
OxygenInput = OxygenInput/100
# print(OxygenInput)
OxygenOutput = weightOfCO2*72.7 + gases['O2'].iat[0]*weightOfGases + slag['FeO'].iat[0]*w[1]*0.22 + slag['SiO2'].iat[0]*w[1]*0.53 + slag['Al2O3'].iat[0]*w[1]*0.47 + slag['CaO'].iat[0]*w[1]*0.28 + slag['MgO'].iat[0]*w[1]*0.4 + slag['MnO'].iat[0]*w[1]*0.225 + slag['P2O5'].iat[0]*0.56*w[1]
OxygenOutput = OxygenOutput/100
# print(OxygenOutput)
O2Lance = OxygenOutput - OxygenInput
# print(O2Lance)
print("w1 = ", w[0], " ton")
print("w2 = ", w[1], " ton")
print("w3 = ", w[2], " ton")
print("Total weight of Gases = ", weightOfGases, " ton")
print("O2 Lance = ", O2Lance, " ton")