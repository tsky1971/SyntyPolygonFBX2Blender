# SyntyPolygonFBX2Blender

This script convert all fbx in a file structur to .blend files.
Automatically all preparation for use with the "Auto-Rig Pro" will be applied.

Steps for using:

- export all files (static and skeletal meshes, textures) from Synty PolygonPack in your UE4 project to an clean directory
- copy batch and python file to the root directory
- execute batchfile

What is done, if all goes right:
- remove armatur
- rotate x 90 degrees
- remove duplicate vertices
- convert triangles to quads
- apply transformations (rot and scale)

In result for each FBX file it creates an directory for each file and 2 versions as blend-file.
1. the original file
2. the converted file with an index based naming convention


TODO

- remove ".001" from name
- rename mesh correctly
- apply texture to material


