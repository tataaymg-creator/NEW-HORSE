"""HH_S11 blocking v03: 8 s shot, wider lens at the original distance.

Runs inside Blender (Text Editor > Run Script) on the original HH_S11_blocking.blend, or headless with bpy.
The camera keeps its original path (about 11.8 m in front of the horse, at chest height, matching his
speed), but the lens goes from 69.6 mm to LENS mm. The horse drops to about half the frame height, and the
stronger perspective makes his chest and shoulders read largest while his body falls away behind them.
"""
import bpy

LENS = 35.0       # mm on the 36 mm-wide sensor: about 54 degrees horizontal
FRAMES = 192      # 8 s at 24 fps

scene = bpy.context.scene
scene.frame_start, scene.frame_end = 1, FRAMES
bpy.data.objects["Cam"].data.lens = LENS
bpy.data.objects["backdrop"].location.z = -60.0   # keep the black backdrop well behind him
