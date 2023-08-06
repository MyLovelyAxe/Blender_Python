import bpy
import math

### basic configuration ###
num_triangles = 50
rad_step = 0.1

### create 10 triangles
for rad in range(num_triangles):

    ################################
    ###### Model one triangle ######
    ################################

    ### add a triangle mesh into the scene
    # GUI operation: in 3D Viewport, shift + A - Mesh - Circle - Add Circle (left-below corner in 3D Viewport - edit sth)
    # code: copy from "info context menu"

    # delete other arguments
    bpy.ops.mesh.primitive_circle_add(vertices=3, radius=((rad + 1 ) * rad_step))

    ### get a reference to the currently active object
    triangle_mesh = bpy.context.active_object

    ### rotate the mesh about x-axis by 90°
    # GUI operation: in 3D Viewport, Item on the right column - Rotation - edit X
    # code: copy from "info context menu"

    # original code:
    #   bpy.context.object.rotation_euler[0] = -1.5708

    # 1. bpy.context.object means the current object
    # which is exactly the traingle_mesh above, so replace it
    # 2. we can also replcae the rotation_euler[0]
    # into rotation_euler.x to show that we rotate along x-axis
    # 3. the value given to rotate is actually radiance
    # use math.radians(degree) to just give a degree in angle
    triangle_mesh.rotation_euler.x = math.radians(-90)
    triangle_mesh.rotation_euler.z = math.radians(-rad*10)

    ### convert mesh into a curve
    # GUI operation: in 3D Viewport, Item on the right column - Rotation - edit X
    # code: copy from "info context menu"

    # original code:
    #   bpy.ops.object.convert(target='CURVE')
    bpy.ops.object.convert(target='CURVE')

    ### add bevel to curve
    # GUI operation: right-below corner Properties Editor - Data - Geometry - Bevel
    # and edit Depth and Resolution
    # code: copy from "info context menu"

    # original code:
    #   bpy.context.object.data.bevel_depth = 0.21
    #   bpy.context.object.data.bevel_resolution = 6
    triangle_mesh.data.bevel_depth = 0.05
    triangle_mesh.data.bevel_resolution = 16

    ### shade smooth
    # GUI operation: in 3D Viewport, right click - shade smooth
    # and edit Depth and Resolution
    # code: copy from "info context menu"

    # original code:
    #   bpy.ops.object.shade_smooth()
    bpy.ops.object.shade_smooth()