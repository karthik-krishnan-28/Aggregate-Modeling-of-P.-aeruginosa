# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 16:16:25 2023

@author: karthikkrishnan with help of sarahsundius

This code simulates the on-lattice diffusion mechanics of a chemical across space. It involves a discretization of Fickian diffusion and is merely an approximation
in order to assist the greater goal of a realistic biological environment for the 2D_AGGREGATES simulation. This lattice class was used in the main Julia sim in
order to simulate various environmental "layers" such as a public good, an antibiotic, and a nutrient resource.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import imageio.v2 as imageio

currT = 1 #starting timestep
maxT = 1000 #number of timesteps
posLim = 100
negLim = -100 
meshSize = 20 #lattice dimensions = (meshSize x meshSize)
dx = (posLim - negLim) / meshSize #thickness of each layer (uniform)
diffCoeff = 10 #micrometer squared
photoFileList = []
latThickness = (posLim - negLim) / meshSize #thickness of each layer (uniform)

vmin = 0
vmax = 5
colorWay = 'Purples'
photoFileList = []

#class representing a new lattice object
class Lattice:
    
    def __init__(self, meshSize, diffCoeff): 
        self.meshSize = meshSize #meshSize describes how fine/coarse nutrient lattice is
        self.array = np.empty(shape=(meshSize,meshSize)) #backing array
        self.diffCoeff = diffCoeff
        self.dt = 0.1
            
    def setGradient(self): #define a random gradient
       self.array = np.random.rand(self.meshSize,self.meshSize)

    def showLattice(self, posLim, negLim, colorWay): #print lattice
        plt.imshow(self.array, cmap=colorWay, extent=[negLim,posLim,negLim,posLim], vmin=0, vmax=1)
    
    def printBackingArray(self): #print backing array
        print(self.array)
        
    def calcDiffusion(self): #compute diffusion from one lattice (2d ndarray) to another
        #Y direction difusion
        Yflux = self.array[1:,:] - self.array[:meshSize-1,:] #C[2:N] - [1:N-1] 
        
        YfluxWP = np.zeros(shape=(meshSize+1,meshSize)) #Create padding matrix
        YfluxWP += 1
        
        YfluxWP[1:meshSize,:] = Yflux - 1 #Add padding
        YfluxWP = -1*diffCoeff*YfluxWP
        YfluxWP = YfluxWP/latThickness 
        
        dC = -1*(YfluxWP[1:,:] - YfluxWP[:meshSize,:])/latThickness
        
        #X direction diffusion
        Xflux = self.array[:,1:] - self.array[:,:meshSize-1] #C[2:N] - [1:N-1]
        
        XfluxWP = np.zeros(shape=(meshSize,meshSize+1))
        YfluxWP += 1

        XfluxWP[:,1:meshSize] = Xflux - 1
        XfluxWP  = -1*diffCoeff*XfluxWP 
        XfluxWP = XfluxWP/latThickness

        dC = dC - ((XfluxWP[:,1:] - XfluxWP[:,:meshSize]))/dx #Add flux gradient to rate of change
        self.array = self.array + dC*self.dt #calculate delta C by multiplying with delta t and add to old array
        
#Edit plot properties
plt.title("Discrete Time Simulation: %d seconds" % (currT + 1)) #sets plot title
plt.xlabel("X Microns") #sets x label
plt.ylabel("Y Microns") #sets y label

#Initialize a new chemical lattice
lattice = Lattice(meshSize, diffCoeff)
lattice.setGradient()

#Initialize a colorbar
fig, axs = plt.subplots()
fig.colorbar(plt.cm.ScalarMappable(norm=mpl.colors.Normalize(vmin=0,vmax=1), cmap=colorWay), ax=axs)

lattice.showLattice(posLim, negLim, colorWay)
photoFile = "After 0 timesteps" + '.png'
plt.savefig(photoFile)
photoFileList.append(photoFile)


#Run sim 
while currT < 10:
    lattice.calcDiffusion()
    lattice.showLattice(posLim, negLim, "Purples")
    plt.show()
    plt.title("Discrete Time Simulation: %.1f seconds" % ((currT)*lattice.dt)) #updates plot title
    currT += 1
  
lattice.showLattice(posLim, negLim, colorWay)
photoFile = "After 10 timesteps" + '.png'
plt.savefig(photoFile)
photoFileList.append(photoFile)

while currT < 50:
    lattice.calcDiffusion()
    lattice.showLattice(posLim, negLim, "Purples")
    plt.show()
    plt.title("Discrete Time Simulation: %.1f seconds" % ((currT)*lattice.dt)) #updates plot title
    currT += 1

lattice.showLattice(posLim, negLim, colorWay)
photoFile = "After 50" + '.png'
plt.savefig(photoFile)
photoFileList.append(photoFile)

while currT < 300:
    lattice.calcDiffusion()
    lattice.showLattice(posLim, negLim, "Purples")
    plt.show()
    plt.title("Discrete Time Simulation: %.1f seconds" % ((currT)*lattice.dt)) #updates plot title
    currT += 1

lattice.showLattice(posLim, negLim, colorWay)
plt.show()
photoFile = "After 300" + '.png'
plt.savefig(photoFile)
photoFileList.append(photoFile)

"""
while currT < maxT:
    lattice.calcDiffusion()
    #plt.title("Discrete Time Simulation: %.1f seconds" % ((currT)*lattice.dt)) #updates plot title
    currT += 1

lattice.showLattice(posLim, negLim, colorWay)   
photoFile = "After 1000" + '.png'
plt.savefig(photoFile)
photoFileList.append(photoFile)"""
