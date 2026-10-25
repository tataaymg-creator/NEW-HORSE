"""HH_S11 blocking v02: the camera tracks back from the HH_S11_v01 framing to a wide frame.

Runs inside Blender (Text Editor > Run Script) on HH_S11_blocking.blend, or headless with bpy.
Frames 1-97 (0-4 s at 24 fps): the camera eases back an extra EXTRA metres, faster than the horse.
Frame 97 onwards: the camera matches his speed again, so he holds the wide size to the end.
"""
import bpy

EXTRA = 10.0      # metres further from the horse once the move has settled
F0, F1 = 1, 97    # the pull-back runs over these frames


def fcurve(action, path, index):
    for layer in action.layers:
        for strip in layer.strips:
            for bag in strip.channelbags:
                for fc in bag.fcurves:
                    if fc.data_path == path and fc.array_index == index:
                        return fc
    raise KeyError(path)


cam = bpy.data.objects["Cam"]
fc = fcurve(cam.animation_data.action, "location", 1)
for k in fc.keyframe_points:
    t = min(max((k.co[0] - F0) / (F1 - F0), 0.0), 1.0)
    d = -EXTRA * t * t * (3 - 2 * t)    # the horse runs toward -Y and the camera is ahead of him
    k.co[1] += d
    k.handle_left[1] += d
    k.handle_right[1] += d
fc.update()
bpy.data.objects["backdrop"].location.z = -60.0   # keep the black backdrop well behind him
