import bpy
import os
import sys
import glob
from math import pi


def rotateX90(obj):
	if obj.type == 'MESH':
		obj.select_set(True)
		print(obj.name)
		bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)


def scale001(obj):
	if obj.type == 'MESH':
		obj.select_set(True)
		bpy.ops.transform.resize(value=(0.01, 0.01, 0.01))


def editMeshes(obj):
	if obj.type == 'MESH':
		obj.select_set(True)
		bpy.context.view_layer.objects.active = obj

		print("toggle EditMode")
		bpy.ops.object.editmode_toggle()
		print(obj.name)
		print("mesh select all faces")
		bpy.ops.mesh.select_all(action='SELECT')
		print("mesh remove doubles")
		bpy.ops.mesh.remove_doubles()
		print("mesh tri to quads")
		bpy.ops.mesh.tris_convert_to_quads()
		print("set normals reset")
		bpy.ops.mesh.normals_tools(mode='RESET')
		print("toggle EditMode")
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
	
	print("filename = " + filename)
	print("full_path = " + full_path)

	objname = filename

	bpy.ops.object.select_all(action='DESELECT')

	objs = [ob for ob in bpy.context.scene.objects if ob.type in ('CAMERA', 'LIGHT')]
	if (objs is not None):
		bpy.ops.object.delete({"selected_objects": objs})
	
	for o in bpy.context.scene.objects:
		if o.name == "Cube":
			objs = [bpy.context.scene.objects['Cube']]
			bpy.ops.object.delete({"selected_objects": objs})
	
	objs = [ob for ob in bpy.context.scene.objects if ob.type in ('ARMATURE')]
	if (objs is not None):
		bpy.ops.object.delete({"selected_objects": objs})

	objs = [ob for ob in bpy.context.scene.objects if ob.type in ('MESH')]

	if objs != None:
		for ob in objs:
			rotateX90(ob)
			scale001(ob)
			editMeshes(ob)
	
	print("DONE")
	