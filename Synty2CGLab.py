import bpy
import os
import sys
import glob
from math import pi

def deleteArmature():
    objects = bpy.data.objects
    for object in objects:
        if ("Root" in object.name):
            print(object.name)
            object.select_set(True)
            bpy.ops.object.delete()
    #    else:
    #        print("not found")


def rotateX90():
   bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)


def scale001():
    bpy.ops.transform.resize(value=(0.01, 0.01, 0.01))

def editMeshes():
    if bpy.context.selected_objects != []:
        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                print(obj.name)
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.editmode_toggle()
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.remove_doubles()
                bpy.ops.mesh.tris_convert_to_quads()
                bpy.ops.object.editmode_toggle()
                print("set shade flat")
                bpy.ops.object.shade_flat()
                print("apply transformations")
                bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)


if __name__ == "__main__":

    full_path = bpy.path.basename(bpy.context.blend_data.filepath)
    print("full_path = " + full_path)

    filename =  bpy.path.basename(bpy.context.blend_data.filepath)
    filename_w_ext = os.path.basename(full_path)
    file_extension = os.path.splitext(filename_w_ext)

    print("filename=" + filename + " ext=" + file_extension)

    objname = filename

    cube = bpy.data.objects["Cube"]
    cube.select_set(True)
    bpy.ops.object.delete()

    deleteArmature()

    object = bpy.data.objects[objname + ".001"]
    print(object.name)

    if object != None:
        object.select_set(True)
        
        rotateX90()
        scale001()
        
    print("do editMeshes")
    editMeshes()    
        
    print("DONE")
