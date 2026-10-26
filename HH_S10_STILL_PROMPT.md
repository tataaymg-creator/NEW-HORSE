# HH shot 10 — still prompt v02 (client version: very close, head angled to camera)

Save the result as **`HH_S10_v02.png`**: the new shot 10 motion prompt uses it as the first frame. Put it in Higgsfield's start-frame slot when you generate the video.

Attach as reference: `HH_S10_v01.png` (same horse, same look). Do **not** attach the client's double-exposure comp: the face in it would bleed into the horse. Its angle and closeness are written into the prompt instead.

```text
Extreme close-up portrait of the grey stallion's head, standing still in the dark arena, his head turned slightly toward the camera: a three-quarter view, not a flat profile. We look along the front of his face; his near eye is large and sharp, his far eye hidden behind the bridge of his nose.

FRAME: his near eye sits on the right-third line, about 65% across and 38% down. Above it, the forelock and the edge of the mane cross the top of the frame; his ears are out of frame above. His face runs diagonally down to the lower left: the bridge of the nose and the cheek fill the middle of the frame, the nostrils and muzzle sit softly out of focus at the lower left, cut by the bottom edge. The upper left is deep, empty darkness; his cheek and jaw turn into shadow toward the right edge.

LENS: a 100 mm macro lens, very shallow depth of field: the eye, its lashes and the skin around it razor sharp, the muzzle and the far side of his face falling into soft blur.

LIGHT: warm 3500K low sun from above and behind him, a thin gold rim along the forelock, the eyelashes, the brow and the bridge of the nose; the rest of his face in soft, low light that shows every freckle and fine hair; a warm catch-light in the eye. Faint sun shafts and a few dust motes drift in the darkness behind and in front of him.

THE EYE: open, calm, wet, dark brown, with the horizontal oval pupil, long pale lashes, the soft folds of skin around it.

LOOK: the same horse as @HH_S10_v01: near-white flea-bitten grey coat with fine dark freckles, dark slate-grey muzzle, dark brown eyes, long silver-white mane and forelock, bare with no tack. Black void background, warm amber-gold dust, deep clean blacks, punchy contrast, full texture in the white coat, fine natural grain. Photoreal live-action photograph. 21:9, 2688×1152.
```

## Notes

- Composition: the client reference has the eye near the centre. Here it is locked on the right third, so the face crosses the frame on a diagonal and the dark upper left stays free (it is also where the client's double exposure sits).
- Screen direction: the reference faces left, while shot 09 runs right. A still, close portrait reads as a new moment, so the cut works. To keep the right-facing direction instead, flip the generated still horizontally before animating it; the eye then sits on the left third, about 35% across.
