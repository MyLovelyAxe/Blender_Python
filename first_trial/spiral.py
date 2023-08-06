import numpy as np
import os
import bpy

# create spiral

r = 2.0

basis = np.arange(0,20,1)
x = np.sin(basis) * basis*0.1
y = np.cos(basis) * basis*0.1
z = basis * 0.1

# verts are points defined by XYZ coordinates in tuples
verts = list((X,Y,Z) for X,Y,Z in zip(x,y,z))

# faces are defiend by indices of verts
faces = list((i,i+1,i+2) for i in range(len(basis)-2))

edges = list((i,i+1) for i in range(len(basis)-1))

# create a new mesh object
mesh_data = bpy.data.meshes.new("cube_data")

# populate mesh_data
# watch out the order!!!: verts, edges, faces
mesh_data.from_pydata(verts, edges, faces)

# create an object with mesh_data
mesh_obj = bpy.data.objects.new("cube_object",mesh_data)

# without this link, you can manually drag Objects in right 2nd outliner to Collection in right 1st outliner
# with this link, no manually work is necessary
bpy.context.collection.objects.link(mesh_obj)