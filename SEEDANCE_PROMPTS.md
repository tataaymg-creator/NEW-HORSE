# HH — Seedance 2.5 prompts, shots 03–11

One prompt per shot, written to be pasted as-is into Seedance 2.5 on Higgsfield. Each prompt stands on its own, so the horse, wind, light, tempo and look blocks repeat on purpose. Paste each one whole.

## Setup for every shot

- **Aspect 21:9**, duration as in the table. Every shot is one continuous take.
- **Attach the files listed for the shot as references.** The handles in the prompt are the file names. If Higgsfield shows a different tag for an upload, swap it in the text.
- **First frame.** For shots 03, 04, 06, 07, 09, 10 and 11 the still is the first frame. **Shot 05** has no start still: `HH_S05_v01` is the head-on frame in the middle of the turn, so attach it as a reference, not as the start frame. **Shot 08** starts on `HH_S08_start_v01`; `HH_S08_v01` is the mid-turn reference.
- **Blender viewports** are referenced only for where the horse sits in frame and how big he is. Each prompt says to ignore their look, rig lines, grid and speed.
- **Higgsfield caps attached reference video at 30 s in total per generation.** Every shot here is under it (the Video refs column). Shot 11 uses the 5 s lock `HH_S11_0001-0120` (frames 1–120 of `HH_S11_0001-0600`; the horse is the same size in all 600 frames).
- **`gallop_side_ref`** drives the leg mechanics and the tempo. It measures **one full stride every 1.8 s** (54 frames at 30 fps), about 4× real-time slow motion. Every shot uses that tempo so the cut holds together.

## What changed against the fake look

- **Sun rays.** The prompts treat the rays as light on dust, so they have three causes to move: dust rolling through them, the camera's travel sliding them across the background with parallax, and the mane crossing the beams. Several shots also have a timed beat where a shaft passes behind him or he runs through one.
- **Mane and wind.** The mane moves in waves tied to the stride (half a beat behind the head dip), with timed gusts that lift it and settle it again, so it is never one stiff sheet.
- **Real slow motion.** One tempo, stated in seconds, applies to the legs, mane, dust and light alike. When only the legs are slowed and the hair is frozen (or the other way round), it reads as fake.
- **Weight and travel.** The hooves plant and grip, the body rises and falls, and the ground streams past, so he travels through space rather than galloping on a treadmill.

## Revisions

- **v2, after the shot 05 take.** Motion and turn were approved. The take invented a row of arena windows with a steel roof along the top of frame (0–1.5 s and 7.7–8.0 s) and a sand clod that turned into a tiny human figure (about 7.2–7.7 s). Shots 05–11 now describe the background as a black void with only sun shafts and dust (no "covered arena", no "high openings"), say the sand is only grains, clods and dust, and lock the top of the frame to black. Shots 03 and 04 are approved takes, so their text is unchanged.
- **v3, shot 11 ending.** From 20 s his hooves throw bigger sprays at the lens; at 22 s a gust drives the whole dust cloud forward over and around him; by 24 s the dust has swallowed him; 24–25 s is a frame completely filled with glowing, moving dust, which you can cut or dissolve out of.
- **v4, shot 11 reference length.** 25 s lock + 8.3 s gallop ref went over Higgsfield's 30 s limit for attached video. The lock is now `HH_S11_0001-0120` (5 s), 13.3 s in total.
- **v6, shot 11 wider (from `HH_S11_blocking.blend`).** The camera now opens on the `HH_S11_v01` framing and tracks back an extra 10 m over 0–4 s (eased), then matches his speed, so from 4 s he fills about half the frame height (ears ~24% from the top, hooves ~73%) instead of 90%. The new lock is `HH_S11_wide_0001-0144` (6 s; 14.3 s of reference video in total). The edited blend is `HH_S11_blocking_v02.blend` (saved from Blender 5.2.3 LTS); `HH_S11_apply_wide.py` applies the same change to the original file in any Blender 5.x. The field of view in the prompt now matches the blend camera (69.6 mm = 29° horizontal) instead of 18°.
- **v10, shot 11 new still and 50 mm.** The v02 still was long-legged, but the close 35 mm lens made his head about 38% of his height, which reads as short and squat. New still `HH_S11_v03` (`HH_S11_STILL_PROMPT.md`): a 50 mm look from about 10 m, one foreleg planted straight, explicit proportions. Blend v05 keeps the same pull-out with the lens and distances scaled (11.0 m to 28.6 m): 80% of the frame height at the start, 49% at 3 s, 38% at 5 s, 28% at 8 s. Lock `HH_S11_pullout50_0001-0192`.
- **v9, shot 11 proportions.** The first pull-out take did not start on `HH_S11_v02` and redrew him stocky: shorter, thicker legs, big hooves, a wider body. The prompt had asked for his head, chest and forelegs to read largest and his chest and shoulders to be the widest part of him, and the shared horse block says heavy neck, deep chest. Shot 11 now has its own horse block with the still's build (legs as long as the body is deep, slender cannons, small hooves) and a lock line that he only gets smaller, never shorter. Put `HH_S11_v02` in the start-frame slot, and set the duration to 8 s.
- **v8, shot 11 pull-out.** The new still `HH_S11_v02` came out with him filling about 82% of the frame height (chest dominant, belly hidden: the client note is solved). The camera now starts on that framing and pulls away faster than he runs: 35 mm, camera 1.48 m high, from 7.9 m to 20 m (horse root) with a 1 s ease-in. He shrinks to ~50% of the frame height by 3 s, ~38% by 5 s, ~29% by 8 s. Blend v04 (`HH_S11_apply_pullout.py`), lock `HH_S11_pullout_0001-0192`.
- **v14, shot 10 moved right for titles.** The reframe also moves him right: the eye at about 83% across and 33% down, his head in the right half, the left half empty darkness for the text.
- **v13, shot 10 eye on the upper third.** The v03 still was reframed (top cut, bottom extended) so the eye sits on the upper-right third, about 67% across and 33% down.
- **v12, shot 10 from above.** The camera sits above his eye line and looks down at his face at about 30°: the forehead under the forelock and the bridge of the nose in view, the nostrils out of frame, the eye on the right third (about 65% across, 40% down). New first frame `HH_S10_v03`.
- **v11, shot 10 replaced (client).** A very close, still portrait instead of the galloping eye shot: the head turned slightly toward the camera, the near eye locked on the right third, the wind in the forelock while he slowly closes and opens his eye. New first frame `HH_S10_v02` (`HH_S10_STILL_PROMPT.md`). The shot 10 built from the shot 03 take is no longer needed.
- **v7, shot 11 cut to 8 s and widened with a wider lens.** New first frame `HH_S11_v02` (still prompt in `HH_S11_STILL_PROMPT.md`). The client found the belly too big next to the chest: the old 70 mm-from-far-away framing flattened depth, so the barrel read as wide as the chest. The camera now stays at the original ~12 m with a 35 mm lens (blend v03, lock `HH_S11_35mm_0001-0192`): he fills about 45% of the frame height and his chest and shoulders read largest, the body falling away behind. Beats compressed: gallop 0–5 s, dust surge 5–7 s, full dust 7–8 s.
- **v5, shot 11 light.** The take lit the horse up from inside at 7–9 s and 17–19 s (frame brightness more than doubled) because the prompt had him run through two sun shafts that "flare bright gold" across his chest. Both beats are gone: the sun now stays behind him all shot, he is lit only by a rim, exposure stays even, and the shafts move only in the dust behind him. New beats: the dust rolling through the shafts at 7–10 s, a head toss at 18 s. The dust ending is unchanged apart from a dark, rim-lit silhouette at 23 s.

## Shot list

| Shot | What it is for | Seconds | Attach | Video refs | Prompt length |
|---|---|---|---|---|---|
| 03 | Medium: head, neck, chest and forelegs, galloping | 8 | `HH_S03_v01.png`, `gallop_side_ref.mp4` | 8.3 s | 894 words / 5073 chars |
| 04 | Very close: head and neck, galloping | 14 | `HH_S04_v01.png`, `HH_S04_blocking_preview.mp4`, `gallop_side_ref.mp4` | 17.9 s | 941 words / 5273 chars |
| 05 | The turn: gallops in, spins 180°, gallops off the other way | 8 | `HH_S05_v01.png`, `HH_S05_0001-0192.mp4`, `gallop_side_ref.mp4` | 16.3 s | 1115 words / 6297 chars |
| 06 | Wide: three horses chase him while he leads | 8 | `HH_S06_v01.png`, `HH_S06_0001-0192.mp4`, `gallop_side_ref.mp4` | 16.3 s | 993 words / 5715 chars |
| 07 | Very close: two heads, he leads and the dark bay falls behind | 14 | `HH_S07_v01.png`, `HH_S07_0001-0336.mp4`, `gallop_side_ref.mp4` | 22.3 s | 1015 words / 5676 chars |
| 08 | The turn back: shot 5 mirrored | 11 | `HH_S08_start_v01.png`, `HH_S08_v01.png`, `gallop_side_ref.mp4` | 8.3 s | 1146 words / 6416 chars |
| 09 | Very close: head and neck, galloping | 7 | `HH_S09_v01.png`, `gallop_side_ref.mp4` | 8.3 s | 894 words / 5017 chars |
| 10 | Very close: the eye closes and opens (client version, standing) | 8 | `HH_S10_v03` | 0.0 s | 826 words / 4523 chars |
| 11 | He gallops straight at the camera, head-on (wide) | 8 | `HH_S11_v03`, `HH_S11_pullout50_0001-0192.mp4`, `gallop_side_ref.mp4` | 16.3 s | 1461 words / 8217 chars |

## Shot 02 — Close dust plate (title space) — 5 s

First generate the still from `HH_S02_STILL_PROMPT.md` and save it as `HH_S02_v01`. No video references. 652 words / 3452 chars.

```text
HH SHOT 02 — 5 s, 21:9 (2.33:1), one continuous slow-motion shot. Close, low shot of a plume of fine sand dust rising off the sand in the empty dark arena, faint sun shafts, the right half and upper part deep black for titles added in post. It opens the film small, before the wider shots of the horse.

REFERENCES
@HH_S02_v01 — THE FIRST FRAME of the clip and the look. Framing exactly as this image.

FRAME
Exactly the composition of the first frame: the dust plume rising off the sand in the left part of the frame, up to about half the frame height; loose, lumpy brown sand along the bottom, the nearest lumps large and soft; faint warm sun shafts falling from above the top edge at the upper left of centre. The right half of the frame and the upper part stay clean, deep black for the entire shot: this is the title space.

CAMERA
Close to the sand, just above the ground, level, about 29° field of view (an 85 mm look), shallow focus on the front of the plume. A very slow, perfectly smooth push-in toward the plume, about 4% tighter over the 5 s; the soft foreground lumps of sand slide gently toward the bottom edge.

ACTION
0.0–1.5s — The first frame comes alive: the plume keeps rising slowly, its edges curl over and fold into themselves, single grains glitter as they drift up through the faint shafts.
1.5–3.5s — A soft breath of wind from the left lifts a thin wisp off the top of the plume and draws it out to the right in a slow ribbon that dissolves before it reaches the middle of the frame. At the base, a low skin of dust slides across the lumps of sand, and a few loose grains tumble down the side of a lump.
3.5–5.0s — The top of the plume thins and spreads into a soft glowing haze while fresh dust keeps lifting gently off the sand at its base; motes float up through the shafts, in and out of focus. The shot ends with the dust still moving.

DUST
Fine sand dust in close-up and slow motion: soft billowing edges with fine wispy detail, single grains sharp and glinting in the plane of focus, motes in front of and behind the plume falling into soft round glints. It rolls, curls and thins continuously and stays low and in the left part of the frame.

LIGHT IN MOTION
The plume is backlit: its edges glow warm amber where the shafts touch it and its core stays darker, and that glowing edge shifts as the plume rolls. The faint shafts are light on drifting dust, so they shimmer and breathe as the dust passes through them. Warm 3500K low sun from above and behind; the lumps of sand at the left catch a warm rim. The shafts stay faint and the right side stays unlit.

TEMPO
Real high-speed slow motion at 24 fps, the same slowed pace as the rest of the film: the dust keeps moving in every frame, slow and fluid.

LOOK
Photoreal live-action commercial, the same look as the rest of the film: deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: a low wind and the faint hiss of drifting sand. No music, no voices.

KEEP CONSISTENT
- Close shot all the way: the plume stays large in the left part of the frame.
- The right half and the upper part of the frame stay clean, deep black for all 5 s.
- The dust drifts gently and stays in the lower left; it never spreads across the frame.
- The arena is empty: only sand, dust, light and darkness; black void above, exactly as in the first frame.
- Exposure stays even from frame to frame.
- One continuous shot, no cuts, no on-screen text.
```

## Alternative: wide establishing plate — 5 s

The wider version, from the original dust still. Shot 02 above replaces it in the cut; kept in case you want a wide title card. Attach the dust still as `HH_establishing_v01` (rename the handle if your file has another name). No video references. 568 words / 3064 chars.

```text
HH ESTABLISHING — 5 s, 21:9 (2.33:1), one continuous slow-motion shot. Title plate: the empty dark sand arena before the horse arrives, low dust drifting over the sand at the left through faint sun shafts, most of the frame deep black for titles added in post.

REFERENCES
@HH_establishing_v01 — THE FIRST FRAME of the clip and the look. Framing exactly as this image.

FRAME
Exactly the composition of the first frame: a strip of loose, churned brown sand along the bottom of the frame; a low cloud of fine dust rising off the sand in the left third; faint warm sun shafts falling from above the top edge at the upper left of centre; everything else deep black. The right half of the frame and the whole upper part stay clean, deep black for the entire shot: this is the title space.

CAMERA
Low, a little above the sand, level, about 47° field of view, on a heavy tripod head. A very slow, perfectly smooth push-in, about 3% tighter over the 5 s.

ACTION
0.0–2.0s — The first frame comes alive: the dust cloud at the left keeps rising slowly and curls over on itself; a light breeze from the left draws its top edge out to the right in thin, soft streamers that fade away before they reach the middle of the frame; fine grains glitter as they drift through the faint shafts.
2.0–3.5s — A soft gust skims the sand: a low, thin sheet of dust lifts off the surface at the left, slides a little to the right along the ground and settles again; loose grains roll over the ripples of the sand.
3.5–5.0s — The dust thins and spreads into a low, glowing haze over the sand at the left; single motes keep floating up through the shafts. The shot ends with the dust still drifting.

DUST
Fine sand dust in slow motion: it rolls, curls and thins continuously, with soft edges and single glittering grains; it stays low and in the left part of the frame. The sand surface keeps its lumpy, churned texture; a few loose grains tumble across it in the breeze.

LIGHT IN MOTION
The faint shafts are light on drifting dust, so they shimmer and breathe as the dust passes through them, and motes glint as they cross. Warm 3500K low sun from above and behind; the lumps of sand at the left catch a warm rim. The shafts stay faint and the right side stays unlit.

TEMPO
Real high-speed slow motion at 24 fps, the same slowed pace as the rest of the film: the dust keeps moving in every frame, slow and fluid.

LOOK
Photoreal live-action commercial, the same look as the rest of the film: deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: a low wind and the faint hiss of drifting sand. No music, no voices.

KEEP CONSISTENT
- The right half and the upper part of the frame stay clean, deep black for all 5 s; dust and light stay low and at the left.
- The dust drifts gently and stays in the lower left; it never spreads across the frame.
- The arena is empty: only sand, dust, light and darkness; black void above, exactly as in the first frame.
- Exposure stays even from frame to frame.
- One continuous shot, no cuts, no on-screen text.
```

## Shot 03 — Medium: head, neck, chest and forelegs, galloping — 8 s

```text
HH SHOT 03 — 8 s, 21:9 (2.33:1), one continuous slow-motion shot. Medium tracking shot of the grey stallion galloping screen-right: head, neck, chest and forelegs, so the stride reads.

REFERENCES
@HH_S03_v01 — THE FIRST FRAME and the look. Framing and his place in frame exactly as this image.
@gallop_side_ref — real gallop, side view: ONLY the leg mechanics and the tempo. It runs screen-left; mirror it, he runs screen-right. Ignore its look and background.

THE HORSE
Grey Iberian stallion: heavy arched neck, deep chest; near-white coat with fine dark flea-bitten freckles, dark slate-grey muzzle, dark brown eyes, long thick wavy silver-white mane and forelock, full silver-white tail, lower legs shading to dark grey, black hooves. Bare, no tack. 100% matches the reference.

CAMERA
Stabilised arm on a tracking vehicle running alongside on his right side at his speed (about 45 km/h), lens at shoulder height, 29° field of view. The camera holds him in the same place in frame for the whole shot, only a faint organic float. Focus on his eye.
FRAMING: his head sits on the left third: eye at about 40% of the frame width and a third down from the top, nose at about 50%, ears near the top edge. The bottom edge cuts across his chest so the forearms and knees fold up into frame on every stride. The mane streams out to the left edge. The right half of the frame stays open dark space ahead of him with the sun shafts.

ACTION
0.0–1.8s — The first frame comes alive: the leading foreleg reaches forward out of the bottom of the frame and lands, head and neck dip; then the forelegs fold up and the knees rise into the bottom of the frame during the suspension, the head lifts.
1.8–3.6s — Second stride. At 2.4s a strong gust lifts the whole mane higher and fans it out to the left edge; a sheet of sand dust rolls up behind his chest and spreads through the shafts.
3.6–5.4s — Third stride. At 4.2s his near ear swivels back toward the camera and forward again; nostrils flare wide on the breath.
5.4–8.0s — Fourth stride and the start of the fifth. The gust eases, the mane settles back into long rippling waves; at 6.6s he blinks once; the dust he threw drifts across the right half of the frame, glittering where it crosses the beams. The shot ends mid-stride, still galloping.

GALLOP
The real four-beat gallop of @gallop_side_ref: hind hooves land one after the other, then the forelegs, the leading foreleg reaching far forward, then a moment of suspension with all four legs gathered under the belly. Once per stride the body rises and falls and the head and neck dip as the forelegs land. Hooves plant, grip and leave deep prints. Muscles ripple under the skin, the skin shudders on each landing, nostrils flare with one breath per stride. He truly travels: the sand streams past under him.

WIND, MANE, DUST
The rush of air from his speed plus a gusting wind. The mane streams in thick separate locks back toward screen-left, rippling in waves from crest to tips, each wave half a beat behind the dip of his head; tips whip and curl, flyaway hairs glow in the backlight, locks cross and separate all the time. The forelock flutters. Hoof strikes throw sand that arcs up and falls back; the fine dust hangs, rolls away behind him and the gusts tear it into streamers. Dust in three depths: soft grains drifting past the lens, rolling clouds around him, thin haze far back in the dark.

LIGHT IN MOTION
The sun shafts are light on moving dust, so they never hold still: as dust rolls through them the beams thicken, thin, shimmer and break up, and motes glitter as they cross them. The camera travels, so the shafts slide toward screen-left with depth parallax, near ones faster than far ones. Backlit mane strands flare gold and flicker as they cross a beam; the rim light on his face and body breathes as the dust in front of the sun thickens and thins.

TEMPO
Real high-speed slow motion at 24 fps, everything slowed equally: one full stride every 1.8 s, the tempo of @gallop_side_ref. Mane, tail, dust and light keep moving at that same slowed rate, fluid in every frame; crisp frames, a trace of motion blur on hooves and flying sand.

LOOK
Photoreal live-action commercial. Dark covered sand arena, loose churned brown sand, background falling to deep black. Low late sun, warm 3500K, from high openings above and behind him, cutting long volumetric shafts through the dust. White coat with a warm gold rim, full texture in the highlights. Shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: slowed, deep, muffled hoofbeats on each footfall, heavy breathing once per stride, gusting wind, the hiss of thrown sand. No music, no voices.

KEEP CONSISTENT
- He gallops screen-right for the whole shot; his eye stays at about 40% of the frame width.
- The right half of the frame stays open dark space ahead of him.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts. No text, no people, no tack.
```

## Shot 04 — Very close: head and neck, galloping — 14 s

```text
HH SHOT 04 — 14 s, 21:9 (2.33:1), one continuous slow-motion shot. Very close tracking shot of the grey stallion's head and neck as he gallops screen-right.

REFERENCES
@HH_S04_v01 — THE FIRST FRAME and the look. Framing and his place in frame exactly as this image.
@HH_S04_blocking_preview — Blender blocking, ONLY for where his head sits in the frame and how big it is. Ignore its look, rig lines, grid, grey studio and stride speed. Hold that placement for all 14 s.
@gallop_side_ref — real gallop, side view: ONLY the leg mechanics and the tempo. It runs screen-left; mirror it, he runs screen-right. Ignore its look and background.

THE HORSE
Grey Iberian stallion: heavy arched neck, deep chest; near-white coat with fine dark flea-bitten freckles, dark slate-grey muzzle, dark brown eyes, long thick wavy silver-white mane and forelock, full silver-white tail, lower legs shading to dark grey, black hooves. Bare, no tack. 100% matches the reference.

CAMERA
Stabilised arm on a tracking vehicle running alongside on his right side at his speed (about 45 km/h), lens at eye height, 18° field of view: long lens, compressed background, very shallow focus. The camera holds his head in the same place in frame for all 14 s, only a faint organic float. Focus on his eye.
FRAMING: head and upper neck fill the frame. Eye at about 40% of the frame width and a third down from the top, nose at about 50%, ears near the top edge. Neck and mane fill the left side to the edge. The right half of the frame is open dark space ahead of him with the sun shafts; a strip of sand floor at the bottom right streams past.

ACTION
0.0–3.6s — The first frame comes alive: two strides; the head dips and lifts once per stride, the mane rolls in a wave from crest to tips after each dip, nostrils flare on each breath.
3.6–5.4s — A strong gust: the mane lifts high and fans out to the left edge, the forelock blows back off the forehead, a cloud of dust boils up under his jaw and drifts left through the light.
5.4–8.0s — The gust eases and the mane settles into long rippling waves; at 6.5s both ears flick back for a moment and forward again; at 7.5s he blinks once.
8.0–10.0s — A bright sun shaft slides in from the right, passes behind his head and leaves the frame on the left: while it is behind him the backlit edge of his mane, ears and muzzle hairs flare brighter gold and the dust around his head glows, then the rim softens again.
10.0–14.0s — Two more strides; at 11.5s a second gust lifts the mane again and tears a streamer of dust across the open space ahead of him. The shot ends mid-stride, still galloping.

GALLOP
Below the frame his legs run the real four-beat gallop of @gallop_side_ref, and its rhythm drives everything in frame: once per stride the head and neck dip as the forelegs land and lift in the moment of suspension. Muscles ripple under the skin of neck and jaw, the skin shudders on each landing, nostrils flare with one breath per stride. He truly travels forward through the space.

WIND, MANE, DUST
The rush of air from his speed plus a gusting wind. The mane streams in thick separate locks back toward screen-left, rippling in waves from crest to tips, each wave half a beat behind the dip of his head; tips whip and curl, flyaway hairs glow in the backlight, locks cross and separate all the time. The forelock flutters. Hoof strikes throw sand that arcs up and falls back; the fine dust hangs, rolls away behind him and the gusts tear it into streamers. Dust in three depths: soft grains drifting past the lens, rolling clouds around him, thin haze far back in the dark.

LIGHT IN MOTION
The sun shafts are light on moving dust, so they never hold still: as dust rolls through them the beams thicken, thin, shimmer and break up, and motes glitter as they cross them. The camera travels, so the shafts slide toward screen-left with depth parallax, near ones faster than far ones. Backlit mane strands flare gold and flicker as they cross a beam; the rim light on his face and body breathes as the dust in front of the sun thickens and thins.

TEMPO
Real high-speed slow motion at 24 fps, everything slowed equally: one full stride every 1.8 s, the tempo of @gallop_side_ref. Mane, tail, dust and light keep moving at that same slowed rate, fluid in every frame; crisp frames, a trace of motion blur on hooves and flying sand.

LOOK
Photoreal live-action commercial. Dark covered sand arena, loose churned brown sand, background falling to deep black. Low late sun, warm 3500K, from high openings above and behind him, cutting long volumetric shafts through the dust. White coat with a warm gold rim, full texture in the highlights. Shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: slowed, deep, muffled hoofbeats on each footfall, heavy breathing once per stride, gusting wind, the hiss of thrown sand. No music, no voices.

KEEP CONSISTENT
- He gallops screen-right for the whole shot; his eye stays at about 40% of the frame width.
- The right half of the frame stays open dark space ahead of him.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts. No text, no people, no tack.
```

## Shot 05 — The turn: gallops in, spins 180°, gallops off the other way — 8 s

```text
HH SHOT 05 — 8 s, 21:9 (2.33:1), one continuous slow-motion shot. Full-figure shot: the grey stallion gallops in screen-right, spins 180° toward the camera and gallops off screen-left.

REFERENCES
@HH_S05_v01 — the look, including its background (black void, sun shafts, dust), and the exact frame at 4.4–4.8s (head-on, mid-turn). NOT the first frame.
@HH_S05_0001-0192 — Blender blocking, ONLY for his position and size in frame, which way he faces at each moment, and when the turn happens. Ignore its look, rig lines, grid, grey studio and stride speed.
@gallop_side_ref — real gallop, side view: ONLY the leg mechanics and the tempo. Match it in both directions. Ignore its look and background.

THE HORSE
Grey Iberian stallion: heavy arched neck, deep chest; near-white coat with fine dark flea-bitten freckles, dark slate-grey muzzle, dark brown eyes, long thick wavy silver-white mane and forelock, full silver-white tail, lower legs shading to dark grey, black hooves. Bare, no tack. 100% matches the reference.

CAMERA
Lens at chest height, 29° field of view, full-figure frame: ears near the top edge, hooves near the bottom edge. The camera travels with him and holds him in the same part of the frame: it tracks right with him, eases to a stop through the turn, then tracks left with him, only a faint organic float. Focus follows his eye.
THE VERY FIRST FRAME: full-figure side profile, galloping screen-right mid-stride, body in the left half of the frame, head at about 60% of the frame width; behind him black darkness with sun shafts and dust, exactly like the background of @HH_S05_v01; sand floor along the bottom.

ACTION
0.0–3.0s — He gallops screen-right, a little over one and a half strides, head at about 60% of the width, mane and tail streaming left; the shafts slide left behind him.
3.0–4.4s — The turn: he sits down onto his haunches and plants both hind hooves deep under his belly; they plough the sand and throw a big fan of sand sideways. His body leans into the turn, his front end lifts and sweeps round toward the camera over the planted hind legs; the mane is flung outward by the swing and wraps across his neck.
4.4–4.8s — Head-on to the camera, centred in the frame, chest square to the lens, rump swung slightly left, mane and tail streaming to the left: exactly the frame of @HH_S05_v01.
4.8–5.6s — He keeps swinging round the same way until he faces screen-left; the hind legs push off; the mane swings across his neck and streams back to the right; the tail sweeps round in a wide arc; the fan of sand from the turn hangs in the light shafts.
5.6–8.0s — He gallops off screen-left with full power, body in the right half of the frame, head at about 40% of the width, mane and tail streaming right; the camera now travels left with him and the shafts slide right; the sand cloud from the turn drifts away behind him through the beams. The shot ends mid-stride, still galloping.

GALLOP
The real four-beat gallop of @gallop_side_ref: hind hooves land one after the other, then the forelegs, the leading foreleg reaching far forward, then a moment of suspension with all four legs gathered under the belly. Once per stride the body rises and falls and the head and neck dip as the forelegs land. Hooves plant, grip and leave deep prints. Muscles ripple under the skin, the skin shudders on each landing, nostrils flare with one breath per stride. He truly travels: the sand streams past under him.

WIND, MANE, DUST
The rush of air from his speed plus a gusting wind. The mane streams in thick separate locks back to the left before the turn and back to the right after it, rippling in waves from crest to tips, each wave half a beat behind the dip of his head; tips whip and curl, flyaway hairs glow in the backlight, locks cross and separate all the time. The forelock flutters. Hoof strikes throw sand that arcs up and falls back, plain grains and clods that break apart into dust; the fine dust hangs, rolls away behind him and the gusts tear it into streamers. Dust in three depths: soft grains drifting past the lens, rolling clouds around him, thin haze far back in the dark.

LIGHT IN MOTION
The sun shafts are light on moving dust, so they never hold still: as dust rolls through them the beams thicken, thin, shimmer and break up, and motes glitter as they cross them. While the camera tracks right the shafts slide left with depth parallax; through the turn they slow and stop; after it they slide right. The sand fan from the turn rises into the beams and makes them flare and churn. Backlit mane strands flare gold and flicker as they cross a beam; the rim light on his face and body breathes as the dust in front of the sun thickens and thins.

TEMPO
Real high-speed slow motion at 24 fps, everything slowed equally: one full stride every 1.8 s, the tempo of @gallop_side_ref. Mane, tail, dust and light keep moving at that same slowed rate, fluid in every frame; crisp frames, a trace of motion blur on hooves and flying sand.

LOOK
Photoreal live-action commercial. He runs on loose, churned brown sand. Behind him the background is a deep black void, exactly as in the reference stills: black darkness, sun shafts and drifting dust, nothing else, from the top edge of the frame to the sand. The shafts fall into the frame from above its top edge, warm 3500K low late sun, cutting long volumetric beams through the dust. White coat with a warm gold rim, full texture in the highlights. Shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: slowed, deep, muffled hoofbeats on each footfall, heavy breathing once per stride, gusting wind, the hiss of thrown sand. No music, no voices.

KEEP CONSISTENT
- He turns toward the camera, never away from it; one 180° turn, nothing more.
- Before the turn his head is at about 60% of the width; after it, at about 40%.
- Full figure all shot: ears and hooves stay in frame.
- Background from first frame to last: black darkness, sun shafts and dust only; the top of the frame stays black.
- The sand stays plain sand and dust; he is the only living thing in the frame.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts, no on-screen text.
```

## Shot 06 — Wide: three horses chase him while he leads — 8 s

```text
HH SHOT 06 — 8 s, 21:9 (2.33:1), one continuous slow-motion shot. Wide tracking shot that pulls out: the grey stallion leads three horses galloping screen-left.

REFERENCES
@HH_S06_v01 — THE FIRST FRAME of the clip and the look. Four horses in profile galloping screen-left in one line at the same distance from camera, left to right: the hero grey stallion leading; a second grey horse half a length behind him; a dark bay (deep chocolate-brown coat, black mane and tail); a bright bay (copper-red coat, black mane, black lower legs).
@HH_S06_0001-0192 — Blender blocking, ONLY for the positions, spacing and sizes of the four horses in frame and the slow pull-out. Ignore its look, rig lines, grid, grey studio and stride speed.
@gallop_side_ref — real gallop, side view: ONLY the leg mechanics and the tempo. Same direction as here, screen-left. Ignore its look and background.

THE HERO HORSE (the leading grey)
Grey Iberian stallion: heavy arched neck, deep chest; near-white coat with fine dark flea-bitten freckles, dark slate-grey muzzle, dark brown eyes, long thick wavy silver-white mane and forelock, full silver-white tail, lower legs shading to dark grey, black hooves. Bare, no tack. 100% matches the reference.

CAMERA
Lens low at the height of their chests, 29° field of view, travelling left alongside the group at their speed (about 45 km/h) while slowly pulling back: over the 8 s the horses shrink to about 85% of their first-frame size, and more black darkness with sun shafts opens above them and more sand below. Faint organic float. Focus on the hero.
FRAMING: the hero leads at the far left, his nose at about 13% of the frame width, his body across the left third; the second grey overlaps his hindquarters; the dark bay and the bright bay follow to the right edge. The sun shafts fall from the upper left.

ACTION
0.0–1.8s — The first frame comes alive: four horses at full gallop, each in its own rhythm, legs never in sync, heads rising and dipping at different moments.
1.8–4.5s — The camera pulls back; their dust rises into one long rolling wall of gold behind and between their legs, drifting right and up into the sun shafts.
4.5–8.0s — The chasers drive hard: the dark bay and the bright bay stretch their necks, ears pinned back, nostrils wide; the hero runs freer, ears forward, mane high. At 6.0s a gust sweeps the dust wall back and tears it into streamers. The shot ends mid-stride, still pulling out.

GALLOP
The real four-beat gallop of @gallop_side_ref: hind hooves land one after the other, then the forelegs, the leading foreleg reaching far forward, then a moment of suspension with all four legs gathered under the belly. Once per stride each body rises and falls and the head and neck dip as the forelegs land. Hooves plant, grip and leave deep prints. Muscles ripple under the skin, the skin shudders on each landing, nostrils flare with one breath per stride. They truly travel: the sand streams past under them.

WIND, MANE, DUST
The rush of air from their speed plus a gusting wind. Every mane streams in thick separate locks back toward screen-right, rippling in waves from crest to tips, each wave half a beat behind the dip of its head; tips whip and curl, flyaway hairs glow in the backlight, locks cross and separate all the time. Forelocks flutter. Hoof strikes throw sand that arcs up and falls back, plain grains and clods that break apart into dust; the fine dust hangs, rolls away behind them and the gusts tear it into streamers. Dust in three depths: soft grains drifting past the lens, rolling clouds around them, thin haze far back in the dark.

LIGHT IN MOTION
The sun shafts are light on moving dust, so they never hold still: as dust rolls through them the beams thicken, thin, shimmer and break up, and motes glitter as they cross them. The camera travels, so the shafts slide toward screen-right with depth parallax, near ones faster than far ones. Backlit mane strands flare gold and flicker as they cross a beam; the rim light on their faces and bodies breathes as the dust in front of the sun thickens and thins.

TEMPO
Real high-speed slow motion at 24 fps, everything slowed equally: one full stride every 1.8 s, the tempo of @gallop_side_ref. Mane, tail, dust and light keep moving at that same slowed rate, fluid in every frame; crisp frames, a trace of motion blur on hooves and flying sand.

LOOK
Photoreal live-action commercial. They run on loose, churned brown sand. Behind them the background is a deep black void, exactly as in the reference stills: black darkness, sun shafts and drifting dust, nothing else, from the top edge of the frame to the sand. The shafts fall into the frame from above its top edge, warm 3500K low late sun, cutting long volumetric beams through the dust. White coat with a warm gold rim, full texture in the highlights. Shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: slowed, deep, muffled hoofbeats on each footfall, heavy breathing once per stride, gusting wind, the hiss of thrown sand. No music, no voices.

KEEP CONSISTENT
- The hero leads at the far left for the whole shot; order and spacing never change; nobody overtakes.
- Exactly four horses: two greys, one dark bay, one bright bay.
- Every mane and tail streams right and moves in every frame.
- Background from first frame to last: black darkness, sun shafts and dust only; the top of the frame stays black.
- The sand stays plain sand and dust; the four horses are the only living things in the frame.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts, no on-screen text.
```

## Shot 07 — Very close: two heads, he leads and the dark bay falls behind — 14 s

```text
HH SHOT 07 — 14 s, 21:9 (2.33:1), one continuous slow-motion shot. Very close tracking shot of two galloping heads, screen-left: the grey stallion holds, the dark bay falls behind.

REFERENCES
@HH_S07_v01 — THE FIRST FRAME of the clip and the look. Two heads in profile galloping screen-left: the hero grey stallion nearest the camera in the lower half of the frame; the dark bay (deep brown coat, black mane) on the far side just behind him, its head higher, at the top of the frame.
@HH_S07_0001-0336 — Blender blocking, ONLY for the positions and sizes of the two heads in frame and when the dark bay drops back out of frame. Ignore its look, rig lines, grid, grey studio and stride speed.
@gallop_side_ref — real gallop, side view: ONLY the leg mechanics and the tempo. Same direction as here, screen-left. Ignore its look and background.

THE HERO HORSE (the leading grey)
Grey Iberian stallion: heavy arched neck, deep chest; near-white coat with fine dark flea-bitten freckles, dark slate-grey muzzle, dark brown eyes, long thick wavy silver-white mane and forelock, full silver-white tail, lower legs shading to dark grey, black hooves. Bare, no tack. 100% matches the reference.

CAMERA
Stabilised arm on a tracking vehicle running alongside on the hero's left side at his speed (about 45 km/h), lens at his eye height, 18° field of view: long lens, compressed, very shallow focus. The camera stays locked on the hero so his head holds its place for all 14 s, only a faint organic float. Focus on his eye; the dark bay slightly softer behind him.
FRAMING: hero nose at about 45% of the frame width, eye at about 55%, a little below the middle; his neck and mane fill the right side to the edge. Dark bay head above and just behind his: nose at about 48%, eye at about 58%, ears at the top edge.

ACTION
0.0–6.0s — Neck and neck. Both heads rise and dip once per stride, each on its own rhythm. The dark bay strains: ears pinned back, nostrils wide, the white of its eye showing at the rim. The hero runs with ears forward, mane streaming right in long waves; the two manes whip in the same wind. At 3.0s a gust lifts both manes high.
6.0–11.0s — The dark bay falls behind: stride by stride its head slips back to the right, past the hero's ears, past his mane, and leaves the frame at the right edge by 11.0s. The camera stays locked on the hero.
11.0–14.0s — The hero alone in the frame, in the same place; the dust the dark bay kicked up drifts across the background through the light shafts. At 12.0s a gust fans his mane high. The shot ends mid-stride, still galloping.

GALLOP
Below the frame his legs run the real four-beat gallop of @gallop_side_ref, and its rhythm drives everything in frame: once per stride the head and neck dip as the forelegs land and lift in the moment of suspension. Muscles ripple under the skin of neck and jaw, the skin shudders on each landing, nostrils flare with one breath per stride. He truly travels forward through the space.

WIND, MANE, DUST
The rush of air from his speed plus a gusting wind. The mane streams in thick separate locks back toward screen-right, rippling in waves from crest to tips, each wave half a beat behind the dip of his head; tips whip and curl, flyaway hairs glow in the backlight, locks cross and separate all the time. The forelock flutters. Hoof strikes throw sand that arcs up and falls back, plain grains and clods that break apart into dust; the fine dust hangs, rolls away behind him and the gusts tear it into streamers. Dust in three depths: soft grains drifting past the lens, rolling clouds around him, thin haze far back in the dark.

LIGHT IN MOTION
The sun shafts are light on moving dust, so they never hold still: as dust rolls through them the beams thicken, thin, shimmer and break up, and motes glitter as they cross them. The camera travels, so the shafts slide toward screen-right with depth parallax, near ones faster than far ones. Backlit mane strands flare gold and flicker as they cross a beam; the rim light on his face and body breathes as the dust in front of the sun thickens and thins.

TEMPO
Real high-speed slow motion at 24 fps, everything slowed equally: one full stride every 1.8 s, the tempo of @gallop_side_ref. Mane, tail, dust and light keep moving at that same slowed rate, fluid in every frame; crisp frames, a trace of motion blur on hooves and flying sand.

LOOK
Photoreal live-action commercial. He runs on loose, churned brown sand. Behind him the background is a deep black void, exactly as in the reference stills: black darkness, sun shafts and drifting dust, nothing else, from the top edge of the frame to the sand. The shafts fall into the frame from above its top edge, warm 3500K low late sun, cutting long volumetric beams through the dust. White coat with a warm gold rim, full texture in the highlights. Shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: slowed, deep, muffled hoofbeats on each footfall, heavy breathing once per stride, gusting wind, the hiss of thrown sand. No music, no voices.

KEEP CONSISTENT
- Both gallop screen-left; the hero stays in front, nearest the camera, in the same place all shot.
- The dark bay only drops back to the right; it never passes him; it is gone by 11.0s.
- Background from first frame to last: black darkness, sun shafts and dust only; the top of the frame stays black.
- The sand stays plain sand and dust; the two horses are the only living things in the frame.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts, no on-screen text.
```

## Shot 08 — The turn back: shot 5 mirrored — 11 s

```text
HH SHOT 08 — 11 s, 21:9 (2.33:1), one continuous slow-motion shot. Starts very close and pulls out to full figure: the grey stallion gallops screen-left, spins 180° toward the camera and gallops off screen-right. The mirror of shot 5.

REFERENCES
@HH_S08_start_v01 — THE FIRST FRAME of the clip and the look: very close head and neck galloping screen-left, head on the right half of the frame (eye at about 59% of the width, nose at about 50%), the left half open dark space.
@HH_S08_v01 — the look, and the exact frame at 7.4–7.8s (head-on, mid-turn). NOT the first frame.
@gallop_side_ref — real gallop, side view: ONLY the leg mechanics and the tempo. Match it in both directions. Ignore its look and background.

THE HORSE
Grey Iberian stallion: heavy arched neck, deep chest; near-white coat with fine dark flea-bitten freckles, dark slate-grey muzzle, dark brown eyes, long thick wavy silver-white mane and forelock, full silver-white tail, lower legs shading to dark grey, black hooves. Bare, no tack. 100% matches the reference.

CAMERA
Starts very close at his eye height, 18° field of view, tracking left alongside at his speed (about 45 km/h). From 0.8s to 4.0s it pulls back and widens in one smooth move to a full-figure frame (29° field of view, ears near the top edge, hooves near the bottom edge) and keeps that size. It tracks left with him, eases to a stop through the turn, then tracks right with him. Only a faint organic float. Focus follows his eye.

ACTION
0.0–0.8s — The first frame comes alive: very close head and neck galloping screen-left, mane streaming right.
0.8–4.0s — Still galloping screen-left, the camera pulls back and widens until he is full-figure: body in the right half of the frame, head at about 40% of the width, hooves throwing sand along the bottom of the frame.
4.0–6.0s — Full-figure gallop screen-left, a little over one stride; the shafts slide right behind him.
6.0–7.4s — The turn: he sits down onto his haunches and plants both hind hooves deep under his belly; they plough the sand and throw a big fan of sand sideways. His body leans into the turn, his front end lifts and sweeps round toward the camera over the planted hind legs; the mane is flung outward by the swing and wraps across his neck.
7.4–7.8s — Head-on to the camera, just left of centre, chest square to the lens, rump swung slightly right, mane and tail streaming to the right: exactly the frame of @HH_S08_v01.
7.8–8.6s — He keeps swinging round the same way until he faces screen-right; the hind legs push off; the mane swings across his neck and streams back to the left; the tail sweeps round in a wide arc; the fan of sand from the turn hangs in the light shafts.
8.6–11.0s — He gallops off screen-right with full power, body in the left half of the frame, head at about 60% of the width, mane and tail streaming left; the camera now travels right with him and the shafts slide left; the sand cloud from the turn drifts away behind him through the beams. The shot ends mid-stride, still galloping.

GALLOP
The real four-beat gallop of @gallop_side_ref: hind hooves land one after the other, then the forelegs, the leading foreleg reaching far forward, then a moment of suspension with all four legs gathered under the belly. Once per stride the body rises and falls and the head and neck dip as the forelegs land. Hooves plant, grip and leave deep prints. Muscles ripple under the skin, the skin shudders on each landing, nostrils flare with one breath per stride. He truly travels: the sand streams past under him.

WIND, MANE, DUST
The rush of air from his speed plus a gusting wind. The mane streams in thick separate locks back to the right before the turn and back to the left after it, rippling in waves from crest to tips, each wave half a beat behind the dip of his head; tips whip and curl, flyaway hairs glow in the backlight, locks cross and separate all the time. The forelock flutters. Hoof strikes throw sand that arcs up and falls back, plain grains and clods that break apart into dust; the fine dust hangs, rolls away behind him and the gusts tear it into streamers. Dust in three depths: soft grains drifting past the lens, rolling clouds around him, thin haze far back in the dark.

LIGHT IN MOTION
The sun shafts are light on moving dust, so they never hold still: as dust rolls through them the beams thicken, thin, shimmer and break up, and motes glitter as they cross them. While the camera tracks left the shafts slide right with depth parallax; through the turn they slow and stop; after it they slide left. The sand fan from the turn rises into the beams and makes them flare and churn. Backlit mane strands flare gold and flicker as they cross a beam; the rim light on his face and body breathes as the dust in front of the sun thickens and thins.

TEMPO
Real high-speed slow motion at 24 fps, everything slowed equally: one full stride every 1.8 s, the tempo of @gallop_side_ref. Mane, tail, dust and light keep moving at that same slowed rate, fluid in every frame; crisp frames, a trace of motion blur on hooves and flying sand.

LOOK
Photoreal live-action commercial. He runs on loose, churned brown sand. Behind him the background is a deep black void, exactly as in the reference stills: black darkness, sun shafts and drifting dust, nothing else, from the top edge of the frame to the sand. The shafts fall into the frame from above its top edge, warm 3500K low late sun, cutting long volumetric beams through the dust. White coat with a warm gold rim, full texture in the highlights. Shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: slowed, deep, muffled hoofbeats on each footfall, heavy breathing once per stride, gusting wind, the hiss of thrown sand. No music, no voices.

KEEP CONSISTENT
- He turns toward the camera, never away from it; one 180° turn, nothing more.
- Before the turn his head is at about 40% of the width; after it, at about 60%.
- From 4.0s to the end he is full figure: ears and hooves stay in frame.
- Background from first frame to last: black darkness, sun shafts and dust only; the top of the frame stays black.
- The sand stays plain sand and dust; he is the only living thing in the frame.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts, no on-screen text.
```

## Shot 09 — Very close: head and neck, galloping — 7 s

```text
HH SHOT 09 — 7 s, 21:9 (2.33:1), one continuous slow-motion shot. Very close tracking shot of the grey stallion's head and neck as he gallops screen-right.

REFERENCES
@HH_S09_v01 — THE FIRST FRAME and the look. Framing and his place in frame exactly as this image.
@gallop_side_ref — real gallop, side view: ONLY the leg mechanics and the tempo. It runs screen-left; mirror it, he runs screen-right. Ignore its look and background.

THE HORSE
Grey Iberian stallion: heavy arched neck, deep chest; near-white coat with fine dark flea-bitten freckles, dark slate-grey muzzle, dark brown eyes, long thick wavy silver-white mane and forelock, full silver-white tail, lower legs shading to dark grey, black hooves. Bare, no tack. 100% matches the reference.

CAMERA
Stabilised arm on a tracking vehicle running alongside on his right side at his speed (about 45 km/h), lens at eye height, 18° field of view: long lens, compressed background, very shallow focus. The camera holds his head in the same place in frame for the whole shot, only a faint organic float. Focus on his eye.
FRAMING: head and upper neck fill the frame. Eye at about 37% of the frame width and a third down from the top, nose at about 48%, ears near the top edge. Neck and mane fill the left side to the edge. The right half of the frame is open dark space ahead of him with the sun shafts.

ACTION
0.0–1.8s — The first frame comes alive: the head dips and lifts with the stride, the mane rolls in a wave from crest to tips, nostrils flare on the breath.
1.8–3.6s — At 2.2s a gust: the mane lifts and fans out to the left edge, dust sweeps up under his jaw and glitters through the shaft above his head.
3.6–5.4s — At 4.3s he blows out hard: nostrils flare wide, the soft muzzle skin and whiskers shiver; ears pricked forward.
5.4–7.0s — A bright shaft slides in from the right behind his head; the backlit muzzle hairs and the edge of the mane flare gold. The shot ends mid-stride, still galloping.

GALLOP
Below the frame his legs run the real four-beat gallop of @gallop_side_ref, and its rhythm drives everything in frame: once per stride the head and neck dip as the forelegs land and lift in the moment of suspension. Muscles ripple under the skin of neck and jaw, the skin shudders on each landing, nostrils flare with one breath per stride. He truly travels forward through the space.

WIND, MANE, DUST
The rush of air from his speed plus a gusting wind. The mane streams in thick separate locks back toward screen-left, rippling in waves from crest to tips, each wave half a beat behind the dip of his head; tips whip and curl, flyaway hairs glow in the backlight, locks cross and separate all the time. The forelock flutters. Hoof strikes throw sand that arcs up and falls back, plain grains and clods that break apart into dust; the fine dust hangs, rolls away behind him and the gusts tear it into streamers. Dust in three depths: soft grains drifting past the lens, rolling clouds around him, thin haze far back in the dark.

LIGHT IN MOTION
The sun shafts are light on moving dust, so they never hold still: as dust rolls through them the beams thicken, thin, shimmer and break up, and motes glitter as they cross them. The camera travels, so the shafts slide toward screen-left with depth parallax, near ones faster than far ones. Backlit mane strands flare gold and flicker as they cross a beam; the rim light on his face and body breathes as the dust in front of the sun thickens and thins.

TEMPO
Real high-speed slow motion at 24 fps, everything slowed equally: one full stride every 1.8 s, the tempo of @gallop_side_ref. Mane, tail, dust and light keep moving at that same slowed rate, fluid in every frame; crisp frames, a trace of motion blur on hooves and flying sand.

LOOK
Photoreal live-action commercial. He runs on loose, churned brown sand. Behind him the background is a deep black void, exactly as in the reference stills: black darkness, sun shafts and drifting dust, nothing else, from the top edge of the frame to the sand. The shafts fall into the frame from above its top edge, warm 3500K low late sun, cutting long volumetric beams through the dust. White coat with a warm gold rim, full texture in the highlights. Shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: slowed, deep, muffled hoofbeats on each footfall, heavy breathing once per stride, gusting wind, the hiss of thrown sand. No music, no voices.

KEEP CONSISTENT
- He gallops screen-right for the whole shot; his eye stays at about 37% of the frame width.
- The right half of the frame stays open dark space ahead of him.
- Background from first frame to last: black darkness, sun shafts and dust only; the top of the frame stays black.
- The sand stays plain sand and dust; he is the only living thing in the frame.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts, no on-screen text.
```

## Shot 10 — Very close: the eye closes and opens (client version, standing) — 8 s

```text
HH SHOT 10 — 8 s, 21:9 (2.33:1), one continuous slow-motion shot. Extreme close-up of the grey stallion's head seen from above, standing still, turned slightly toward the camera; the wind moves his forelock and mane while he slowly closes his eye and slowly opens it again.

REFERENCES
@HH_S10_v03 — THE FIRST FRAME of the clip and the look: framing, angle and light exactly as this image.

THE HORSE
Grey Iberian stallion, standing still: near-white coat with fine dark flea-bitten freckles, dark slate-grey muzzle, dark brown eyes with long pale lashes, long silver-white mane and forelock. Bare, no tack. 100% matches the reference.

CAMERA
Locked off on a heavy tripod above his eye line, looking down at his face at about 30°, about 18° field of view (a 100 mm macro look), very shallow focus on the eye. The frame holds still for all 8 s, with only a barely perceptible organic float.
FRAMING: exactly the first frame: seen from above, his head turned slightly toward the camera, the top of his forehead under the forelock and the bridge of his nose in view; his head fills the right half of the frame, his near eye far right, about 83% across and 33% down; the forelock across his forehead and the top edge; the bridge of his nose running down to the bottom edge left of centre, soft and out of focus, the nostrils out of frame below; his cheek and the mane cut by the right edge, turning into shadow. The left half of the frame is empty deep darkness with only faint dust and faint sun shafts: space for titles.

ACTION
0.0–2.0s — The first frame comes alive: he stands still, his eye open and calm. A steady breeze from behind lifts the forelock and loose strands of the mane across the top of the frame; single hairs drift across his brow; the skin of his cheek and above his eye rises and falls with one slow breath.
2.0–3.6s — He slowly closes his eye: the upper lid lowers smoothly, the long lashes come down and meet the lower lashes, the soft skin around the eye folds. At 2.8s a gust lifts the forelock higher.
3.6–4.6s — Eye closed, calm. A slow breath moves the skin of his cheek; dust motes drift through the warm light in front of him.
4.6–6.6s — He slowly opens his eye: the lid lifts, the lashes part, the wet dark-brown eye with its horizontal pupil returns, and the warm catch-light comes back into it.
6.6–8.0s — Eye open, steady and calm, looking past the camera; the forelock settles and lifts again in the breeze. The shot ends still and calm, the eye open.

WIND, HAIR, DUST
A steady breeze from behind him with soft gusts. The forelock and the loose strands of the mane lift, wave, cross and settle all the time, single flyaway hairs glowing in the backlight; the fine hairs on his face and the eyelashes tremble in the air. Dust in three depths: soft grains drifting past the lens, motes glittering in the light around his head, a thin haze far back in the dark.

LIGHT IN MOTION
Warm 3500K low sun from above and behind him: a thin gold rim along the forelock, the lashes, the brow and the bridge of the nose; the rest of his face in soft, low light showing every freckle and fine hair. The faint sun shafts behind him shimmer as dust drifts through them; the rim on the forelock flickers as the strands move; the catch-light in the eye shifts with his breathing. Exposure stays even; his coat reflects the light and never glows from within.

TEMPO
Real high-speed slow motion at 24 fps, the same slowed pace as the rest of the film: the eye closes over about 1.5 s and opens over about 2 s; hair and dust keep moving at that same slowed rate, fluid in every frame.

LOOK
Photoreal live-action commercial. Behind him a deep black void with faint sun shafts and drifting dust, nothing else. Very shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, full texture in the white coat, fine natural grain. 21:9.

SOUND
Only: a soft wind, one slow calm breath, the faint hiss of drifting sand. No music, no voices.

KEEP CONSISTENT
- He stands still: his head stays in the same place for all 8 s, the near eye far right (about 83% across, 33% down); only breathing and the wind move him.
- The eye closes once and opens once, both slowly; only the near eye is visible.
- The frame holds still; the background stays black darkness, faint shafts and dust; the left half stays empty and dark, only flyaway hairs and dust drift into it.
- Forelock, mane and dust move in every frame.
- He is the only living thing in the frame.
- One continuous shot, no cuts, no on-screen text.
```

## Shot 11 — He gallops straight at the camera, head-on (wide) — 8 s

```text
HH SHOT 11 — 8 s, 21:9 (2.33:1), one continuous slow-motion shot. Head-on: the grey stallion gallops straight at the camera while the camera pulls away faster than he runs, so the frame keeps widening around him, until a huge cloud of dust surges at the lens and fills the whole frame.

REFERENCES
@HH_S11_v03 — THE FIRST FRAME of the clip and the look: the horse head-on, centred, the black background, the sun shafts behind him, the dust, the grade. Framing exactly as this image.
@HH_S11_pullout50_0001-0192 — Blender blocking, ONLY for his position and size in frame: centred, shrinking steadily as the camera pulls away. Ignore its look, rig lines, grid, grey studio and stride speed. Follow that widening until the dust covers him.
@gallop_side_ref — real gallop, side view: ONLY the leg mechanics and the tempo. Same mechanics, seen from the front. Ignore its look and background.

THE HORSE
Tall, elegant grey stallion with exactly the build of @HH_S11_v03: a long arched neck, a deep but narrow chest, long slender legs (from elbow to hoof about as long as from withers to elbow), clean thin cannon bones, small neat hooves, a refined head. Near-white coat with fine dark flea-bitten freckles, dark slate-grey muzzle, dark brown eyes, long thick wavy silver-white mane and forelock, full silver-white tail, lower legs shading to dark grey, black hooves. Bare, no tack. 100% matches the reference.

CAMERA
Lens low at the height of his chest and level, exactly on his line of travel, about 40° horizontal field of view (a 50 mm look), the same lens for the whole shot; at this distance the lens keeps his natural proportions: tall, long-legged, exactly as in the first frame. Stabilised arm on a tracking vehicle driving backwards ahead of him, faster than he runs: it starts about 10 m in front of him at exactly the framing of the first frame, eases into the move over the first second, then pulls away from him at a steady rate, about 17 m further away by the end. The frame widens continuously and smoothly around him, more sand appearing in front of him and more darkness, shafts and dust around him. Only a faint organic float. Focus follows his face.
FRAMING: centred all shot. It starts exactly as the first frame, where he fills most of the frame height; by 3.0s he fills about half the frame height, by 5.0s a little under 40%, by 8.0s under 30%.

ACTION
0.0–3.0s — The first frame comes alive and the camera starts pulling away: he gallops straight at the camera, getting steadily smaller in the widening frame; each stride his chest and head rise and dip, the forelegs fold high one after the other and strike, throwing sand forward and to both sides; the mane flies out to both sides of his neck and the forelock streams back between his ears. At 1.8s a gust lifts the mane and swirls the dust behind him.
3.0–5.0s — He drives harder: ears pricked forward, nostrils flaring; each stride his forelegs hurl bigger sprays of sand toward the camera, and the dust cloud behind him swells and rises higher than his ears, glowing where the sun cuts through it.
5.0–7.0s — The dust comes for the camera: at 5.0s a powerful gust from behind him drives the whole cloud forward, faster than the camera retreats; it rolls over his back and round both sides of him and, with the sand he throws, rolls toward the camera and surges over the lens. The camera keeps pulling away at the same rate. The dust fills the frame from the edges inward: by 6.0s he is a dark silhouette with a thin gold rim inside the dust, by 7.0s he is gone inside it.
7.0–8.0s — The whole frame is dense, billowing dust, lit from behind so it glows amber and gold; soft out-of-focus grains streak past the lens. The dust keeps rolling and churning to the last frame: the shot ends on a frame completely filled with moving dust.

GALLOP
The real four-beat gallop of @gallop_side_ref: hind hooves land one after the other, then the forelegs, the leading foreleg reaching far forward, then a moment of suspension with all four legs gathered under the belly. Once per stride the body rises and falls and the head and neck dip as the forelegs land. Hooves plant, grip and leave deep prints. Muscles ripple under the skin, the skin shudders on each landing, nostrils flare with one breath per stride. He truly travels: the sand streams past under him.

WIND, MANE, DUST
The rush of air from his speed plus a gusting wind. The mane streams in thick separate locks back and out to both sides of his neck, rippling in waves from crest to tips, each wave half a beat behind the dip of his head; tips whip and curl, flyaway hairs glow in the backlight, locks cross and separate all the time. The forelock flutters. Hoof strikes throw sand that arcs up and falls back, plain grains and clods that break apart into dust; the fine dust hangs, rolls away behind him and the gusts tear it into streamers. Dust in three depths: soft grains drifting past the lens, rolling clouds around him, thin haze far back in the dark.

LIGHT IN MOTION
The sun shafts are light on moving dust, so they never hold still: as dust rolls through them the beams thicken, thin, shimmer and break up, and motes glitter as they cross them. The shafts stand behind him, between him and the far darkness; with the camera retreating they drift slowly, and the dust he throws keeps churning through them. The sun stays behind him the whole shot, so he is lit only from behind: a thin warm rim on his outline, mane and ears, his face and chest in soft, even light exactly as in @HH_S11_v03. Backlit mane strands catch the light and flicker as they move. In the last seconds the dust thickens until the sunlight scatters through all of it and the dust glows amber around his dark silhouette.

TEMPO
Real high-speed slow motion at 24 fps, everything slowed equally: one full stride every 1.8 s, the tempo of @gallop_side_ref. Mane, tail, dust and light keep moving at that same slowed rate, fluid in every frame; crisp frames, a trace of motion blur on hooves and flying sand.

LOOK
Photoreal live-action commercial. He runs on loose, churned brown sand. Behind him the background is a deep black void, exactly as in the reference stills: black darkness, sun shafts and drifting dust, nothing else, from the top edge of the frame to the sand. The shafts fall into the frame from above its top edge, warm 3500K low late sun, cutting long volumetric beams through the dust. White coat with a warm gold rim, full texture in the highlights. Shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: slowed, deep, muffled hoofbeats on each footfall, heavy breathing once per stride, gusting wind, the hiss of thrown sand; as the dust surges over the lens, a deep rushing roar of wind and sand. No music, no voices.

KEEP CONSISTENT
- He gallops straight at the camera, centred, while the camera pulls away faster than he runs: he gets steadily smaller and the frame only ever widens, smoothly, with the same lens throughout, until the dust swallows him between 5.0s and 7.0s.
- His proportions stay exactly as in @HH_S11_v03 in every frame: tall, long slender legs, a refined head, small neat hooves; as the camera pulls away he only gets smaller, never shorter or stockier.
- Seen from the front his ribcage and belly stay hidden behind his chest and shoulders, his outline narrowing from the shoulders back; a lean, tucked-up belly.
- The sun stays behind him all shot: he is lit only from behind, a thin warm rim round his outline, his face and chest in soft, even light exactly as in @HH_S11_v03; his coat reflects light and never glows from within.
- Exposure stays even from frame to frame; the light changes only in the dust and shafts behind him.
- The shot ends on a frame completely filled with glowing dust that is still moving.
- Until 5.0s the background is black darkness, sun shafts and dust only, the top of the frame black; from then on the dust fills everything.
- The sand stays plain sand and dust; he is the only living thing in the frame.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts, no on-screen text.
```
