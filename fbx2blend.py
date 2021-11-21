#
# blender --background --python fbx2blend.py Path
#
##########

import os
import bpy
import glob
import sys
import math
import mathutils


def rotateX90(obj):
	if obj.type == 'MESH':
		obj.select_set(True)
		print("rotate 90 X = " + obj.name)		
		obj.rotation_euler = mathutils.Euler((math.radians(0.0), 0, 0), 'XYZ')
		print("rotation finish")


def scale001(obj):
	if obj.type == 'MESH':
		obj.select_set(True)
		print("scale = " + obj.name)
		bpy.ops.transform.resize(value=(0.01, 0.01, 0.01))
		#obj.proportional_size(0.01)
		print("scale finish")


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

def printDirectoryFiles(directory):
	for filename in os.listdir(directory):
		full_path=os.path.join(directory, filename)
		if not os.path.isdir(full_path):
			#print( full_path + "\n")
			if full_path[-4:] == ".FBX":
				#print("FBX File = " + full_path)
				bpy.ops.import_scene.fbx(filepath = full_path,
					filter_glob="*.fbx",
					use_image_search=False,
					use_custom_props=False,
					ignore_leaf_bones=False,
					automatic_bone_orientation=False,
					primary_bone_axis='Y',
					secondary_bone_axis='X',
					use_prepost_rot=True,
					axis_forward='-Z',
					axis_up='Y')

				filename_w_ext = os.path.basename(full_path)
				filename_fbx, file_extension = os.path.splitext(filename_w_ext)
				path, filename = os.path.split(full_path)

				print("ext	= " + file_extension)
				print("name = " + filename_fbx)
				print("path = " + path)

				new_path = path + "/"+ filename_fbx
				print("new path = " + new_path)
				
				if not os.path.exists(new_path):
					os.mkdir(new_path)
				else:
					new_path = path + "/" + filename_fbx + "_NEW"
					os.mkdir(new_path)

				new_filename_blend = filename_fbx + "_ORG_" + ".blend"
				print("new filename blend = " + new_filename_blend)

				first_filename_blend = filename_fbx + "_00.blend"
				print("first filename blend = " + first_filename_blend)

				new_file_path_blend = new_path + "/" + new_filename_blend
				print("new file path blend = " + new_file_path_blend)

				first_file_path_blend = new_path + "/" + first_filename_blend
				print("first file path blend = " + first_file_path_blend)

				if not os.path.exists(new_file_path_blend):
					bpy.ops.wm.save_as_mainfile(filepath = new_file_path_blend)
					bpy.ops.wm.save_as_mainfile(filepath = first_file_path_blend)

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

					bpy.ops.wm.save_mainfile(filepath = first_file_path_blend)

					#bpy.ops.wm.open_mainfile(filepath=first_file_path_blend)

				bpy.ops.wm.read_homefile(use_empty=True)
				#print("_DONE" + "\n")




def checkFolders(directory):
	dir_list = next(os.walk(directory))[1]

	print(dir_list)

	for dir in dir_list:
		print(dir)
		checkFolders(directory +"/"+ dir)

	printDirectoryFiles(directory)


def main():
	print("MAIN_")

	#for arg in sys.argv[1:]:
	#	print(arg)

	main_dir = sys.argv[4] #"F:/FBX/Game"

	#print("argv " + main_dir)
	checkFolders(main_dir)


if __name__ == "__main__":
	main()
