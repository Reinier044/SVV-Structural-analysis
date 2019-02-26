# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 20:20:30 2019

@author: Reinier
"""

import numpy as np
Ca      =   0.547       #[m]
la      =   2.771       #[m]
x1      =   0.153       #[m]
x2      =   1.281       #[m]
x3      =   2.681       #[m]
xa      =   0.28        #[m]
h       =   0.225       #[m]
tsk     =   1.1*10**-3   #[m]     
tsp     =   2.9*10**-3   #[m]
tst     =   1.2*10**-3   #[m]
hst     =   1.5*10**-2   #[m]
wst     =   2.0*10**-2   #[m]
nst     =   17
d1      =   1.103*10**-2 #[m]
d3      =   1.642*10**-2 #[m]
theta   =   26          #[deg]
P       =   91700       #[N]
q       =   4530        #[N/m]
Iyy     =   261143990.8*10**-12     #[m^4]
Izz     =   11991695.56*10**-12     #[m^4]

r = h/2                #[m], radius of circular segment

#-------------------------------

U = 1/float(Izz)

BoomZ = [0.25062, 0.19631, 0.142, 0.08769, 0.03337999999999999, -0.020930000000000008, -0.07524000000000002, -0.12955, -0.20907, -0.24206999999999998, -0.20907, -0.12955, -0.07524000000000002, -0.020930000000000008, 0.03337999999999999, 0.08769, 0.142, 0.19631, 0.25062]
BoomY = [-0.0140625, -0.028125, -0.0421875, -0.05625, -0.0703125, -0.084375, -0.0984375, -0.1125, -0.07955, 0, 0.07955, 0.1125, 0.0984375, 0.084375, 0.0703125, 0.05625, 0.0421875, 0.028125, 0.0140625]
BoomA = [0.00010371, 0.00010371, 0.00010371, 0.00010371, 0.00010371, 0.00010371, 0.00010371, 0.00018219, 0.00012975, 0.00010682999999999999, 0.00012975, 0.00018219, 0.00010371, 0.00010371, 0.00010371, 0.00010371, 0.00010371, 0.00010371, 0.00010371]

Half  = [0.277775, 0.223465, 0.169155, 0.114845, 0.060535, 0.006225, -0.048085, -0.102395, -0.16931, -0.22557, -0.22557, -0.16931, -0.102395, -0.048085, 0.006224999999999994, 0.060535, 0.114845, 0.169155, 0.223465, 0.277775]

Zcent = 0.30493
Ycent = 0

qBase = []
index = 0
while index <len(BoomZ):
    qBase.append(U*(BoomA[index]*BoomZ[index]))
    index = index +1

LengthsUp = [] 
LengthsDown = []    
i = 0
j = 18
OuterCoorUp = Zcent
OuterCoorDown = Zcent
while i <10:
    LengthsDown.append(OuterCoorDown-BoomZ[i])
    LengthsUp.append(OuterCoorUp-BoomZ[j])
    OuterCoorDown = BoomZ[j]
    OuterCoorUp = BoomZ[j]
    j = j - 1
    i = i + 1

SegLengths = LengthsDown   
i = len(LengthsUp)-1
while i>0:
    SegLengths.append(LengthsUp[i])
    i = i -1




