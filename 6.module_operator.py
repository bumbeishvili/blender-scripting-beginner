# give Python access to Blender's functionality
import bpy

# extend Python's math functionality
import math

import pprint


def get_circle_verts(vert_count, radius):
    # initialize paramaters
    angle_step = math.tau / vert_count

    # create a list of vert coordinates
    vert_coordinates = list()

    # repeat code in a loop
    for i in range(vert_count):

        # calculate current current_angle
        current_angle = angle_step * i

        # calculate coordinate
        x = radius * math.cos(current_angle)
        y = radius * math.sin(current_angle)

        # visualize what we are doing
        # bpy.ops.mesh.primitive_ico_sphere_add(radius=0.05, location=(x, y, 0))

        # add current coordinate to list
        vert_coordinates.append((x, y, 0))

    return vert_coordinates


def create_circle_mesh(coordinates, vert_count):
    verts = coordinates

    faces = []

    edges = []

    for i in range(vert_count ):
        current_vert_index = i
        next_vert_index = (i + 1)%vert_count
        edges.append((current_vert_index, next_vert_index))

 

    # create a mesh from the vert, edge, and face data
    mesh_data = bpy.data.meshes.new("circle_data")
    mesh_data.from_pydata(verts, edges, faces)

    # create a object using the mesh data
    mesh_obj = bpy.data.objects.new("circle_object", mesh_data)

    bpy.context.collection.objects.link(mesh_obj)


# initialize paramaters
vert_count = 32
radius = 2

coordinates = get_circle_verts(vert_count, radius)

mesh_obj = create_circle_mesh(coordinates, vert_count)