"""HH main angle blocking: side-on tracking shot, the horse locked in place in the frame.

Matches the HH_MAIN still: he gallops screen-right, his eye about 46% across and 20% down, the tips of his
ears near the top, his hooves on the ground near the bottom edge. The camera travels beside him at his
exact speed (a Copy Location constraint on hero_root), so he holds his place in the frame.

The rig gallops in real time (one stride per 0.5 s); the scene is time-remapped 3.6x so the lock plays at the
film's slow-motion tempo, one stride every 1.8 s.

Runs inside Blender (Text Editor > Run Script) on the original HH_S11_blocking.blend, or headless with bpy.
"""
import math
import bpy

LENS = 85.0        # mm on the 36 mm-wide sensor
D = 15.0           # metres from the camera to the horse's centre line (side-on)
CAM_Z = 1.20       # camera height in metres: level camera, ground near the bottom edge
LEAD = -2.10       # camera position along his line of travel, relative to hero_root (he runs toward -Y)
SLOW = 3.6         # time stretch: rig stride 0.5 s -> 1.8 s
SECONDS = 15
NECK_DOWN = 0.20   # radians: lowers the rig's high-held neck toward the still's longer, flatter gallop neck

scene = bpy.context.scene
scene.render.frame_map_old = 10
scene.render.frame_map_new = round(10 * SLOW)
scene.frame_start, scene.frame_end = 1, SECONDS * 24

bpy.data.objects["hero_neck"].delta_rotation_euler = (0.0, NECK_DOWN, 0.0)

cam = bpy.data.objects["Cam"]
cam.animation_data_clear()
cam.data.lens = LENS
cam.location = (-D, LEAD, CAM_Z)                    # on his right side, looking along +X: screen-right is -Y
cam.rotation_euler = (math.pi / 2, 0.0, -math.pi / 2)
for c in list(cam.constraints):
    cam.constraints.remove(c)
follow = cam.constraints.new("COPY_LOCATION")
follow.target = bpy.data.objects["hero_root"]
follow.use_x = follow.use_z = False
follow.use_offset = True                            # camera location = root + the offset above
