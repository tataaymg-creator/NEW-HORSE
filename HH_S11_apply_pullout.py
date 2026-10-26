"""HH_S11 blocking v04: 8 s, 35 mm, the camera pulls away faster than the horse runs.

Runs inside Blender (Text Editor > Run Script) on the original HH_S11_blocking.blend, or headless with bpy.
Frame 1 matches the HH_S11_v02 still (the horse fills about 82% of the frame height). The camera eases into
its retreat over the first second, then pulls away at a steady rate, so the frame keeps widening to the end.
"""
import bpy

LENS = 35.0        # mm on the 36 mm-wide sensor: about 54 degrees horizontal
FRAMES = 192       # 8 s at 24 fps
D_START = 7.9      # metres from camera to the horse's root at frame 1
D_END = 20.0       # metres at the last frame
EASE = 24          # frames over which the retreat speeds up from zero
CAM_Z = 1.48       # camera height in metres (chest height); places him like the still


def fcurve(action, path, index):
    for layer in action.layers:
        for strip in layer.strips:
            for bag in strip.channelbags:
                for fc in bag.fcurves:
                    if fc.data_path == path and fc.array_index == index:
                        return fc
    raise KeyError(path)


def progress(f):
    """0 at frame 1, 1 at the last frame: velocity eases up over EASE frames, then stays constant."""
    def dist(x):
        x = x - 1
        if x <= EASE:
            u = x / EASE
            return EASE * (u ** 3 - u ** 4 / 2)        # integral of the smoothstep velocity ramp
        return EASE / 2 + (x - EASE)
    return dist(f) / dist(FRAMES)


scene = bpy.context.scene
scene.frame_start, scene.frame_end = 1, FRAMES
cam = bpy.data.objects["Cam"]
cam.data.lens = LENS
root = fcurve(bpy.data.objects["hero_root"].animation_data.action, "location", 1)
fc = fcurve(cam.animation_data.action, "location", 1)
for k in fc.keyframe_points:
    f = k.co[0]
    d = D_START + (D_END - D_START) * progress(min(max(f, 1), FRAMES))
    y = root.evaluate(f) - d                       # the horse runs toward -Y; the camera is ahead of him
    delta = y - k.co[1]
    k.co[1] = y
    k.handle_left[1] += delta
    k.handle_right[1] += delta
fc.update()
zc = fcurve(cam.animation_data.action, "location", 2)
for k in zc.keyframe_points:
    delta = CAM_Z - k.co[1]
    k.co[1] = CAM_Z
    k.handle_left[1] += delta
    k.handle_right[1] += delta
zc.update()
bpy.data.objects["backdrop"].location.z = -60.0   # keep the black backdrop well behind him
