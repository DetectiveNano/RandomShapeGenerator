## Paul BReeding AKA DetectiveNano
##10/18/21
##used to generate random 3d images

import numpy as np
import random as r
from stl import mesh

vMin = -50
vMax = 50
fMin = 0
fMax = 100
vertVal = 12000
faceVal = 30000


def makeList(rMin,rMax,amount):
    listToArray = []
    for i in range(0,amount):
        r.seed()
        data = [r.randint(rMin,rMax),r.randint(rMin,rMax),r.randint(rMin,rMax)]
        listToArray.append(data)
    return np.array(listToArray)


numShapes = int(input("How many shapes would you like to generate : "))
for k in range(1,numShapes+1):
    faces = []
    vertices = []
    # Define the vertices
    vertices = np.array(
        makeList(vMin,vMax,vertVal+1)
        )
    # Define the  triangles 
    faces = np.array(
        makeList(fMin,fMax,faceVal)
        )
    # Create the mesh
    shape = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            shape.vectors[i][j] = vertices[f[j],:]
    # save
    filename = str(k) + '.stl'
    shape.save(filename)

print('done')
