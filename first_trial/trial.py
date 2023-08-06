import numpy as np
import os
import bpy

# verts are points defined by XYZ coordinates in tuples
verts = [
    (-1.0, -1.0, -1.0),
    (-1.0, 1.0, -1.0),
    (1.0, 1.0, -1.0),
    (1.0, -1.0, -1.0),
    (-1.0, -1.0, 1.0),
    (-1.0, 1.0, 1.0),
    (1.0, 1.0, 1.0),
    (1.0, -1.0, 1.0),
]

# faces are defiend by indices of verts
faces = [
    (0, 1, 2, 3),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (7, 4, 0, 3),
    (6, 7, 3, 2),
    (5, 6, 2, 1)
]

edges = []

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