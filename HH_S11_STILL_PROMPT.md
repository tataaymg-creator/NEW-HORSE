# HH shot 11 — still prompt v02 (wide, first frame of the 8 s shot)

Save the result as **`HH_S11_v02.png`**: the shot 11 video prompt uses it as the first frame. The approved still came out tighter than asked (he fills about 82% of the frame height), which is now the opening frame of a pull-out: see `HH_S11_apply_pullout.py` and blend v04.

Attach as references:
- `HH_S11_v01.png`: same horse, same look. Its framing and lens are what change.
- `HH_S11_layout_35mm.png` (optional, only if your image model takes more than one reference): the Blender frame with the new camera. It sets only his place and size in the frame and the camera height.

```text
The grey stallion galloping dead straight at the camera, exactly head-on and centred: both eyes equally visible, his nose pointing straight into the lens, his face perfectly symmetrical, his chest square to the camera with both shoulders and both forelegs equally visible, his body hidden directly behind his chest, the mane streaming back evenly on both sides of his neck. The camera is low, at the height of his chest and level, exactly on his line of travel. The warm golden backlight sits directly behind him, outlining his whole body and the dust behind him.

WIDE FRAME: a wide shot. He fills a little under half of the frame height: the tips of his ears about a quarter of the way down from the top edge, his hooves about 70% of the way down, centred left to right. Above him, black darkness with warm sun shafts falling through drifting dust. On both sides of him, wide dark space with soft dust clouds rolling out to the left and right. In front of him, a broad strip of loose, churned brown sand running toward the camera, catching the backlight in its grooves and hoofprints.

LENS AND PERSPECTIVE: shot on a 35 mm lens from about 12 metres, so his head, chest and forelegs read as the biggest part of him and his body falls away smaller behind them. His chest and the points of his shoulders are the widest part of his silhouette. His ribcage and belly sit behind the chest, narrower and almost completely hidden, with only a thin sliver of flank showing behind each shoulder; his outline tapers from the shoulders back. He is a fit, athletic stallion with a deep chest and a lean, tucked-up belly.

POSE: mid-stride, one foreleg folded high with the knee up, the other reaching down into the sand, sand and clods spraying forward and to both sides from the hooves.

LOOK: the same horse and look as @HH_S11_v01: near-white flea-bitten grey, dark slate-grey muzzle, dark brown eyes, long thick silver-white mane and forelock, lower legs shading to dark grey, black hooves, bare with no tack. The same black void background, the same warm 3500K backlight, amber-gold dust, deep clean blacks, punchy contrast, full texture in the white coat, fine natural grain. Photoreal live-action photograph. 21:9, 2688×1152.

@HH_S11_layout_35mm — Blender layout, ONLY for his place and size in the frame and the camera height. Ignore its grey mannequin, grid floor and flat light.
```

Leave out the last line if you don't attach the layout image.

## Why the belly read too big, and what changed

The first still was framed like the old Blender camera: a ~70 mm lens far away. A long lens flattens depth, so the barrel behind the chest shows at almost the same size as the chest and bulges past the shoulders. Real head-on horse shots are usually made closer on a wider lens: the near parts (head, chest, forelegs) read big and the body recedes. This prompt and the v03 blend do that: the same ~12 m distance, a 35 mm lens, so he gets smaller in frame (wider) and the chest dominates. A camera at chest height and level also keeps the underside of the belly out of view.

If he reads too small, the next step is a 40 mm look: he fills about half the frame height. Use "a 40 mm lens", ears "about a fifth of the way down", hooves "about three quarters down". `HH_S11_apply_35mm.py` takes the same number (`LENS = 40.0`) to re-render the lock.
