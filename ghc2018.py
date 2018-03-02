#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:44:04 2018

@author: JavaWizards
"""

import numpy as np

file = "/Users/nuno_chicoria/Downloads/b_should_be_easy.in"

handle = open(file)

R, C, F, N, B, T = handle.readline().split()

rides = []

index = []
for i in range(int(N)):
    index.append(i)

for line in handle:
    rides.append(line.split())
    
rides_np = np.asarray(rides)
rides_np = np.column_stack([rides_np, index])
rides_np = rides_np.astype(np.int)
rides_np = rides_np[rides_np[:,5].argsort()]

vehicles = {}
for i in range(int(F)):
    vehicles [i] = ["A", [0, 0], [0, 0], [0, 0], []]
   
for i in range(int(T)):
    rides_np = rides_np[rides_np[:,5] > i]
    for item in range(len(vehicles)):
        if vehicles[item][0] == "A":
            if rides_np.size != 0:
                if abs(vehicles[item][1][0] - rides_np[0, 0]) + abs(vehicles[item][1][1] - rides_np[0, 1]) + i >= rides_np[0, 4]:
                    if  abs(vehicles[item][1][0] - rides_np[0, 0]) + abs(vehicles[item][1][1] - rides_np[0, 1]) + i + abs(rides_np[0,0] - rides_np[0,2]) + abs(rides_np[0,1] - rides_np[0,3]) <= rides_np[0, 5]:
                        vehicles[item][0] = "C"
                        vehicles[item][2] = [rides_np[0, 0], rides_np[0, 1]]
                        vehicles[item][3] = [rides_np[0, 2], rides_np[0, 3]]
                        vehicles[item][4].append(rides_np[0, 6])
                        rides_np = np.delete(rides_np, (0), axis=0)
                    else:
                        rides_np = np.delete(rides_np, (0), axis=0)
    for item in range(len(vehicles)):
        if vehicles[item][0] == "C":
            if vehicles[item][1][0] < vehicles[item][2][0]:
                vehicles[item][1][0] = vehicles[item][1][0] + 1
            elif vehicles[item][1][0] > vehicles[item][2][0]:
                vehicles[item][1][0] = vehicles[item][1][0] - 1
            elif vehicles[item][1][0] == vehicles[item][2][0]:
                if vehicles[item][1][1] < vehicles[item][2][1]:
                    vehicles[item][1][1] =  vehicles[item][1][1] + 1
                elif vehicles[item][1][1] > vehicles[item][2][1]:
                    vehicles[item][1][1] = vehicles[item][1][1] - 1
                else:
                   vehicles[item][0] = "D"
    for item in range(len(vehicles)):
        if vehicles[item][0] == "D":
            if vehicles[item][1][0] < vehicles[item][3][0]:
                vehicles[item][1][0] += 1
            elif vehicles[item][1][0] > vehicles[item][3][0]:
                vehicles[item][1][0] -= 1
            elif vehicles[item][1][0] == vehicles[item][3][0]:
                if vehicles[item][1][1] < vehicles[item][3][1]:
                    vehicles[item][1][1] += 1
                elif vehicles[item][1][1] > vehicles[item][3][1]:
                    vehicles[item][1][1] -= 1
                else:
                    vehicles[item][0] = "A"
                    vehicles[item][2] = None
                    vehicles[item][3] = None
        
results = open("ghc2018.txt", "w+")
for item in range(len(vehicles)):
    if len(vehicles[item][4]) !=0:
        results.write(str(len(vehicles[item][4])))
        for ride in vehicles[item][4]:
            results.write(" ")
            results.write(str(ride))
        results.write("\n")
results.close()