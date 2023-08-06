import numpy as np
import os
import bpy

# verts are points defined by XYZ coordinates in tuples
verts = [
    (-1.0, -1.0, -1.0),
    (-1.0, 1.0, -1.0),
    (1.0, 1.0, -1.0),
    (1.0, -1.0, -1.0),
    (0.0, 0.0, 1.0)
]

# faces are defiend by indices of verts
# the index of verts is defined as the order in verts
# e.g.
# vert with index 0 is the vert (-1.0,-1.0,-1.0)
# vert with index 2 is the vert (1.0, 1.0, -1.0)
faces = [
    (0, 1, 2, 3),
    (0, 3, 4),
    (1, 0, 4),
    (2, 1, 4),
    (3, 2, 4),
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