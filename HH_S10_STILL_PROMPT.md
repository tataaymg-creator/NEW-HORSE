# HH shot 10 — still prompt v03 (client version, seen from above)

Save the result as **`HH_S10_v03.png`**: the shot 10 motion prompt uses it as the first frame. Put it in Higgsfield's start-frame slot when you generate the video.

v02 came out right in look but too low: a near-profile at eye height with the nostrils in frame. v03 raises the camera above his eye line and frames higher on the head, like the client reference.

## Reframe the v03 result (eye on the upper third)

The v03 result is right in angle and look, but the eye sits at 55% down, the vertical centre. Keep the image and move the frame down instead of generating again:

1. Cut **21.9%** off the top (186 px on the 2000×851 file, 252 px on a 2688×1152 original).
2. Extend the bottom by the same amount with outpainting (Photoshop Generative Expand, or Higgsfield outpaint). `HH_S10_v03_reframe_canvas.png` is the 2000×851 frame with the top already cut and the empty strip at the bottom.
3. The eye then sits on the upper-right third: **67.8% across, 33.4% down**. The dark upper left, the shafts and the forelock across the top all stay. `HH_S10_v03_reframe_guide.png` shows before and after on a thirds grid.
4. Save the result as `HH_S10_v03.png`: that is the first frame for the motion prompt.

Outpaint prompt for the bottom strip:

```text
Continue the photograph downward: the bridge of the horse's nose and his cheek in the same near-white coat with fine dark freckles, the same soft low warm light falling into shadow toward the bottom edge, the grey skin below the eye continuing down, the soft focus of the lower face. To the left of the nose, the same black background with faint warm gold dust. The nostrils and muzzle stay out of frame. Seamless with the image above, same grain.
```

If you generate again instead, Options A and B below already ask for the eye on the upper-right third.

## Generate

Attach as reference: `HH_S10_v02.png` (the first result: horse, light, dust and colour). Do **not** attach the client's double-exposure comp: the face in it would bleed into the horse.

## Option A — edit the v02 still (fastest, keeps the look)

For an image model that edits an attached image (Nano Banana, Seedream edit, etc.), with `HH_S10_v02.png` attached:

```text
Same photograph, same horse, same light. Move the camera up and a little closer: it now looks down at his face from above his eye line at about 30°. We see the top of his forehead under the forelock and the bridge of his nose running down to the lower-left corner; the nostrils and muzzle are out of frame below. His near eye stays razor sharp on the right third, on the upper-right third, about 67% across and 33% down (one third down from the top), a little larger in the frame. Keep everything else exactly: the near-white freckled coat, the gold rim light on the forelock, lashes and brow, the warm catch-light in the eye, the sun shafts and dust in the dark upper left, the black background, 21:9.
```

## Option B — full prompt

```text
Extreme close-up of the grey stallion's head seen from above: the camera is higher than his eye, in front of him and to his side, looking down at his face at about 30°. His head is turned slightly toward the camera, so we see the top and front of his forehead and the bridge of his nose, not a flat profile. His near eye is large and sharp; his far eye is hidden beyond the curve of his forehead.

FRAME: very close: his near eye is about a tenth of the frame width and sits on the right-third line, on the upper-right third, about 67% across and 33% down (one third down from the top). The forelock falls across his forehead and the top edge of the frame; his ears are out of frame above. From the eye, the bridge of his nose runs down to the lower-left corner and leaves the frame there; the nostrils and muzzle are out of frame below. The upper left is deep darkness with faint sun shafts and dust; his cheek and jaw turn into shadow toward the right and bottom edges.

LENS: a 100 mm macro lens, very shallow depth of field: the eye, its lashes and the skin around it razor sharp, the lower part of his face falling into soft blur.

LIGHT: warm 3500K low sun from above and behind him, a thin gold rim along the forelock, the eyelashes, the brow and the bridge of the nose; the rest of his face in soft, low light that shows every freckle and fine hair; a warm catch-light in the eye. Faint sun shafts and a few dust motes drift in the darkness behind and in front of him.

THE EYE: open, calm, wet, dark brown, with the horizontal oval pupil, long pale lashes, the soft folds of skin around it.

LOOK: exactly the horse, light and colour of @HH_S10_v02, only the camera is higher and closer: near-white flea-bitten grey coat with fine dark freckles, dark brown eyes, long silver-white mane and forelock, bare with no tack. Black void background, warm amber-gold dust, deep clean blacks, punchy contrast, full texture in the white coat, fine natural grain. Photoreal live-action photograph. 21:9, 2688×1152.
```

## Notes

- If the result keeps the old low angle, the attached v02 is pulling it back. Run Option B again with `HH_S10_v01.png` attached instead, or with no reference.
- Composition: the client reference has the eye near the centre. Here it is locked on the right third, so the face crosses the frame on a diagonal and the dark upper left stays free (it is also where the client's double exposure sits).
- Screen direction: he faces left, while shot 09 runs right. A still, close portrait reads as a new moment, so the cut works. To keep the right-facing direction instead, flip the generated still horizontally before animating it; the eye then sits on the left third, about 35% across.

---

# Previous: still prompt v02 (eye height)

```text
Extreme close-up portrait of the grey stallion's head, standing still in the dark arena, his head turned slightly toward the camera: a three-quarter view, not a flat profile. We look along the front of his face; his near eye is large and sharp, his far eye hidden behind the bridge of his nose.

FRAME: his near eye sits on the right-third line, about 65% across and 38% down. Above it, the forelock and the edge of the mane cross the top of the frame; his ears are out of frame above. His face runs diagonally down to the lower left: the bridge of the nose and the cheek fill the middle of the frame, the nostrils and muzzle sit softly out of focus at the lower left, cut by the bottom edge. The upper left is deep, empty darkness; his cheek and jaw turn into shadow toward the right edge.

LENS: a 100 mm macro lens, very shallow depth of field: the eye, its lashes and the skin around it razor sharp, the muzzle and the far side of his face falling into soft blur.

LIGHT: warm 3500K low sun from above and behind him, a thin gold rim along the forelock, the eyelashes, the brow and the bridge of the nose; the rest of his face in soft, low light that shows every freckle and fine hair; a warm catch-light in the eye. Faint sun shafts and a few dust motes drift in the darkness behind and in front of him.

THE EYE: open, calm, wet, dark brown, with the horizontal oval pupil, long pale lashes, the soft folds of skin around it.

LOOK: the same horse as @HH_S10_v01: near-white flea-bitten grey coat with fine dark freckles, dark slate-grey muzzle, dark brown eyes, long silver-white mane and forelock, bare with no tack. Black void background, warm amber-gold dust, deep clean blacks, punchy contrast, full texture in the white coat, fine natural grain. Photoreal live-action photograph. 21:9, 2688×1152.
```
