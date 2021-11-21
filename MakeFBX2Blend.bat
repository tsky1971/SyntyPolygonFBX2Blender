echo off
for /D %%d in (*) do (
	echo "%%d"
	"C:\Program Files\Blender Foundation\Blender 2.93\blender.exe" --background --python fbx2blend.py %%d
)
