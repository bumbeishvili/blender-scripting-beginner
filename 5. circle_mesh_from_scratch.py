# imports
import bpy
import math
import pprint


def get_circle_vert_coordinates(points,radius):
    coords = [];
    for i in range(points):
        angle = 2*math.pi/points
        x = radius*math.sin(angle*i)
        y = radius*math.cos(angle*i)
        coord = (x, y, 0)
        coords.append(coord)
    return coords;



def get_obj(points,verts,rotation=0):
    edges = []
    for i in range(points-1):
        edges.append((i,i+1))
    edges.append((points-1,0))
    faces = []

    # create mesh data from the vert,edge and face
    mesh = bpy.data.meshes.new('circle mesh')
    mesh.from_pydata(verts,edges,faces)
    # create obj using mesh data
    obj =  bpy.data.objects.new('circle',mesh)
    obj.rotation_euler.y = math.radians(rotation)
    
    return obj
    

# clear everything
for obj in bpy.context.scene.objects:
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj;
    bpy.ops.object.delete()
    

points = 140
radius = 3

# define lists for verts,edges and faces
verts = get_circle_vert_coordinates(points,radius); 

# get obj
obj = get_obj(points,verts,rotation=0)
obj2 = get_obj(points,verts,rotation=90)

pprint.pprint(obj)

# add obj to scene
bpy.context.collection.objects.link(obj)
bpy.context.collection.objects.link(obj2)