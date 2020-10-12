#
# blender --background --python fbx2blend.py Path
#
##########

import os
import bpy
import glob
import sys

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
				
				#print("ext  = " + file_extension)
				#print("name = " + filename_fbx)
				#print("path = " + path)
				
				new_path = path + "/"+ filename_fbx 
				#print("new path = " + new_path)
				
				new_filename_blend = filename_fbx + "_ORG_" + ".blend"				
				#print("new filename blend = " + new_filename_blend)
				
				new_file_path_blend = new_path + "/" + new_filename_blend
				#print("new file path blend = " + new_file_path_blend)
				
				if not os.path.exists(new_path):
					os.mkdir(new_path)
					
				if not os.path.exists(new_file_path_blend):
					bpy.ops.wm.save_as_mainfile(filepath = new_file_path_blend)
					#bpy.ops.wm.open_mainfile(filepath=bpy.data.filepath)
					bpy.ops.wm.read_homefile(use_empty=True)
				
				#print("_DONE" + "\n")
				


def checkFolders(directory):
	dir_list = next(os.walk(directory))[1]

	#print(dir_list)

	for dir in dir_list:
		#print(dir)
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
