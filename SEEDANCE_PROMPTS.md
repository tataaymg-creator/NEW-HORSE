# HH — Seedance 2.5 prompts, shots 03–11

One prompt per shot, written to be pasted as-is into Seedance 2.5 on Higgsfield. Each prompt stands on its own, so the horse, wind, light, tempo and look blocks repeat on purpose. Paste each one whole.

## Setup for every shot

- **Aspect 21:9**, duration as in the table. Every shot is one continuous take.
- **Attach the files listed for the shot as references.** The handles in the prompt are the file names. If Higgsfield shows a different tag for an upload, swap it in the text.
- **First frame.** For shots 03, 04, 06, 07, 09, 10 and 11 the still is the first frame. **Shot 05** has no start still: `HH_S05_v01` is the head-on frame in the middle of the turn, so attach it as a reference, not as the start frame. **Shot 08** starts on `HH_S08_start_v01`; `HH_S08_v01` is the mid-turn reference.
- **Blender viewports** are referenced only for where the horse sits in frame and how big he is. Each prompt says to ignore their look, rig lines, grid and speed.
- **`gallop_side_ref`** drives the leg mechanics and the tempo. It measures **one full stride every 1.8 s** (54 frames at 30 fps), about 4× real-time slow motion. Every shot uses that tempo so the cut holds together.

## What changed against the fake look

- **Sun rays.** The prompts treat the rays as light on dust, so they have three causes to move: dust rolling through them, the camera's travel sliding them across the background with parallax, and the mane crossing the beams. Several shots also have a timed beat where a shaft passes behind him or he runs through one.
- **Mane and wind.** The mane moves in waves tied to the stride (half a beat behind the head dip), with timed gusts that lift it and settle it again, so it is never one stiff sheet.
- **Real slow motion.** One tempo, stated in seconds, applies to the legs, mane, dust and light alike. When only the legs are slowed and the hair is frozen (or the other way round), it reads as fake.
- **Weight and travel.** The hooves plant and grip, the body rises and falls, and the ground streams past, so he travels through space rather than galloping on a treadmill.

## Shot list

| Shot | What it is for | Seconds | Attach | Prompt length |
|---|---|---|---|---|
| 03 | Medium: head, neck, chest and forelegs, galloping | 8 | `HH_S03_v01.png`, `gallop_side_ref.mp4` | 894 words / 5073 chars |
| 04 | Very close: head and neck, galloping | 14 | `HH_S04_v01.png`, `HH_S04_blocking_preview.mp4`, `gallop_side_ref.mp4` | 941 words / 5273 chars |
| 05 | The turn: gallops in, spins 180°, gallops off the other way | 8 | `HH_S05_v01.png`, `HH_S05_0001-0192.mp4`, `gallop_side_ref.mp4` | 1028 words / 5822 chars |
| 06 | Wide: three horses chase him while he leads | 8 | `HH_S06_v01.png`, `HH_S06_0001-0192.mp4`, `gallop_side_ref.mp4` | 912 words / 5288 chars |
| 07 | Very close: two heads, he leads and the dark bay falls behind | 14 | `HH_S07_v01.png`, `HH_S07_0001-0336.mp4`, `gallop_side_ref.mp4` | 937 words / 5272 chars |
| 08 | The turn back: shot 5 mirrored | 11 | `HH_S08_start_v01.png`, `HH_S08_v01.png`, `gallop_side_ref.mp4` | 1070 words / 6026 chars |
| 09 | Very close: head and neck, galloping | 7 | `HH_S09_v01.png`, `gallop_side_ref.mp4` | 818 words / 4627 chars |
| 10 | Very close: the face and eye | 8 | `HH_S10_v01.png`, `gallop_side_ref.mp4` | 831 words / 4675 chars |
| 11 | He gallops straight at the camera, head-on | 25 | `HH_S11_v01.png`, `HH_S11_0001-0600.mp4`, `gallop_side_ref.mp4` | 1017 words / 5750 chars |

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
@HH_S05_v01 — the look, and the exact frame at 4.4–4.8s (head-on, mid-turn). NOT the first frame.
@HH_S05_0001-0192 — Blender blocking, ONLY for his position and size in frame, which way he faces at each moment, and when the turn happens. Ignore its look, rig lines, grid, grey studio and stride speed.
@gallop_side_ref — real gallop, side view: ONLY the leg mechanics and the tempo. Match it in both directions. Ignore its look and background.

THE HORSE
Grey Iberian stallion: heavy arched neck, deep chest; near-white coat with fine dark flea-bitten freckles, dark slate-grey muzzle, dark brown eyes, long thick wavy silver-white mane and forelock, full silver-white tail, lower legs shading to dark grey, black hooves. Bare, no tack. 100% matches the reference.

CAMERA
Lens at chest height, 29° field of view, full-figure frame: ears near the top edge, hooves near the bottom edge. The camera travels with him and holds him in the same part of the frame: it tracks right with him, eases to a stop through the turn, then tracks left with him, only a faint organic float. Focus follows his eye.
THE VERY FIRST FRAME: full-figure side profile, galloping screen-right mid-stride, body in the left half of the frame, head at about 60% of the frame width; the dark arena with sun shafts behind him, sand floor along the bottom; the look of @HH_S05_v01.

ACTION
0.0–3.0s — He gallops screen-right, a little over one and a half strides, head at about 60% of the width, mane and tail streaming left; the shafts slide left behind him.
3.0–4.4s — The turn: he sits down onto his haunches and plants both hind hooves deep under his belly; they plough the sand and throw a big fan of sand sideways. His body leans into the turn, his front end lifts and sweeps round toward the camera over the planted hind legs; the mane is flung outward by the swing and wraps across his neck.
4.4–4.8s — Head-on to the camera, centred in the frame, chest square to the lens, rump swung slightly left, mane and tail streaming to the left: exactly the frame of @HH_S05_v01.
4.8–5.6s — He keeps swinging round the same way until he faces screen-left; the hind legs push off; the mane swings across his neck and streams back to the right; the tail sweeps round in a wide arc; the fan of sand from the turn hangs in the light shafts.
5.6–8.0s — He gallops off screen-left with full power, body in the right half of the frame, head at about 40% of the width, mane and tail streaming right; the camera now travels left with him and the shafts slide right; the sand cloud from the turn drifts away behind him through the beams. The shot ends mid-stride, still galloping.

GALLOP
The real four-beat gallop of @gallop_side_ref: hind hooves land one after the other, then the forelegs, the leading foreleg reaching far forward, then a moment of suspension with all four legs gathered under the belly. Once per stride the body rises and falls and the head and neck dip as the forelegs land. Hooves plant, grip and leave deep prints. Muscles ripple under the skin, the skin shudders on each landing, nostrils flare with one breath per stride. He truly travels: the sand streams past under him.

WIND, MANE, DUST
The rush of air from his speed plus a gusting wind. The mane streams in thick separate locks back to the left before the turn and back to the right after it, rippling in waves from crest to tips, each wave half a beat behind the dip of his head; tips whip and curl, flyaway hairs glow in the backlight, locks cross and separate all the time. The forelock flutters. Hoof strikes throw sand that arcs up and falls back; the fine dust hangs, rolls away behind him and the gusts tear it into streamers. Dust in three depths: soft grains drifting past the lens, rolling clouds around him, thin haze far back in the dark.

LIGHT IN MOTION
The sun shafts are light on moving dust, so they never hold still: as dust rolls through them the beams thicken, thin, shimmer and break up, and motes glitter as they cross them. While the camera tracks right the shafts slide left with depth parallax; through the turn they slow and stop; after it they slide right. The sand fan from the turn rises into the beams and makes them flare and churn. Backlit mane strands flare gold and flicker as they cross a beam; the rim light on his face and body breathes as the dust in front of the sun thickens and thins.

TEMPO
Real high-speed slow motion at 24 fps, everything slowed equally: one full stride every 1.8 s, the tempo of @gallop_side_ref. Mane, tail, dust and light keep moving at that same slowed rate, fluid in every frame; crisp frames, a trace of motion blur on hooves and flying sand.

LOOK
Photoreal live-action commercial. Dark covered sand arena, loose churned brown sand, background falling to deep black. Low late sun, warm 3500K, from high openings above and behind him, cutting long volumetric shafts through the dust. White coat with a warm gold rim, full texture in the highlights. Shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: slowed, deep, muffled hoofbeats on each footfall, heavy breathing once per stride, gusting wind, the hiss of thrown sand. No music, no voices.

KEEP CONSISTENT
- He turns toward the camera, never away from it; one 180° turn, nothing more.
- Before the turn his head is at about 60% of the width; after it, at about 40%.
- Full figure all shot: ears and hooves stay in frame.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts. No text, no people, no tack.
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
Lens low at the height of their chests, 29° field of view, travelling left alongside the group at their speed (about 45 km/h) while slowly pulling back: over the 8 s the horses shrink to about 85% of their first-frame size, and more dark arena opens above them and more sand below. Faint organic float. Focus on the hero.
FRAMING: the hero leads at the far left, his nose at about 13% of the frame width, his body across the left third; the second grey overlaps his hindquarters; the dark bay and the bright bay follow to the right edge. The sun shafts fall from the upper left.

ACTION
0.0–1.8s — The first frame comes alive: four horses at full gallop, each in its own rhythm, legs never in sync, heads rising and dipping at different moments.
1.8–4.5s — The camera pulls back; their dust rises into one long rolling wall of gold behind and between their legs, drifting right and up into the sun shafts.
4.5–8.0s — The chasers drive hard: the dark bay and the bright bay stretch their necks, ears pinned back, nostrils wide; the hero runs freer, ears forward, mane high. At 6.0s a gust sweeps the dust wall back and tears it into streamers. The shot ends mid-stride, still pulling out.

GALLOP
The real four-beat gallop of @gallop_side_ref: hind hooves land one after the other, then the forelegs, the leading foreleg reaching far forward, then a moment of suspension with all four legs gathered under the belly. Once per stride each body rises and falls and the head and neck dip as the forelegs land. Hooves plant, grip and leave deep prints. Muscles ripple under the skin, the skin shudders on each landing, nostrils flare with one breath per stride. They truly travel: the sand streams past under them.

WIND, MANE, DUST
The rush of air from their speed plus a gusting wind. Every mane streams in thick separate locks back toward screen-right, rippling in waves from crest to tips, each wave half a beat behind the dip of its head; tips whip and curl, flyaway hairs glow in the backlight, locks cross and separate all the time. Forelocks flutter. Hoof strikes throw sand that arcs up and falls back; the fine dust hangs, rolls away behind them and the gusts tear it into streamers. Dust in three depths: soft grains drifting past the lens, rolling clouds around them, thin haze far back in the dark.

LIGHT IN MOTION
The sun shafts are light on moving dust, so they never hold still: as dust rolls through them the beams thicken, thin, shimmer and break up, and motes glitter as they cross them. The camera travels, so the shafts slide toward screen-right with depth parallax, near ones faster than far ones. Backlit mane strands flare gold and flicker as they cross a beam; the rim light on their faces and bodies breathes as the dust in front of the sun thickens and thins.

TEMPO
Real high-speed slow motion at 24 fps, everything slowed equally: one full stride every 1.8 s, the tempo of @gallop_side_ref. Mane, tail, dust and light keep moving at that same slowed rate, fluid in every frame; crisp frames, a trace of motion blur on hooves and flying sand.

LOOK
Photoreal live-action commercial. Dark covered sand arena, loose churned brown sand, background falling to deep black. Low late sun, warm 3500K, from high openings above and behind him, cutting long volumetric shafts through the dust. White coat with a warm gold rim, full texture in the highlights. Shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: slowed, deep, muffled hoofbeats on each footfall, heavy breathing once per stride, gusting wind, the hiss of thrown sand. No music, no voices.

KEEP CONSISTENT
- The hero leads at the far left for the whole shot; order and spacing never change; nobody overtakes.
- Exactly four horses: two greys, one dark bay, one bright bay.
- Every mane and tail streams right and moves in every frame.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts. No text, no people, no tack.
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
The rush of air from his speed plus a gusting wind. The mane streams in thick separate locks back toward screen-right, rippling in waves from crest to tips, each wave half a beat behind the dip of his head; tips whip and curl, flyaway hairs glow in the backlight, locks cross and separate all the time. The forelock flutters. Hoof strikes throw sand that arcs up and falls back; the fine dust hangs, rolls away behind him and the gusts tear it into streamers. Dust in three depths: soft grains drifting past the lens, rolling clouds around him, thin haze far back in the dark.

LIGHT IN MOTION
The sun shafts are light on moving dust, so they never hold still: as dust rolls through them the beams thicken, thin, shimmer and break up, and motes glitter as they cross them. The camera travels, so the shafts slide toward screen-right with depth parallax, near ones faster than far ones. Backlit mane strands flare gold and flicker as they cross a beam; the rim light on his face and body breathes as the dust in front of the sun thickens and thins.

TEMPO
Real high-speed slow motion at 24 fps, everything slowed equally: one full stride every 1.8 s, the tempo of @gallop_side_ref. Mane, tail, dust and light keep moving at that same slowed rate, fluid in every frame; crisp frames, a trace of motion blur on hooves and flying sand.

LOOK
Photoreal live-action commercial. Dark covered sand arena, loose churned brown sand, background falling to deep black. Low late sun, warm 3500K, from high openings above and behind him, cutting long volumetric shafts through the dust. White coat with a warm gold rim, full texture in the highlights. Shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: slowed, deep, muffled hoofbeats on each footfall, heavy breathing once per stride, gusting wind, the hiss of thrown sand. No music, no voices.

KEEP CONSISTENT
- Both gallop screen-left; the hero stays in front, nearest the camera, in the same place all shot.
- The dark bay only drops back to the right; it never passes him; it is gone by 11.0s.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts. No text, no people, no tack.
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
The rush of air from his speed plus a gusting wind. The mane streams in thick separate locks back to the right before the turn and back to the left after it, rippling in waves from crest to tips, each wave half a beat behind the dip of his head; tips whip and curl, flyaway hairs glow in the backlight, locks cross and separate all the time. The forelock flutters. Hoof strikes throw sand that arcs up and falls back; the fine dust hangs, rolls away behind him and the gusts tear it into streamers. Dust in three depths: soft grains drifting past the lens, rolling clouds around him, thin haze far back in the dark.

LIGHT IN MOTION
The sun shafts are light on moving dust, so they never hold still: as dust rolls through them the beams thicken, thin, shimmer and break up, and motes glitter as they cross them. While the camera tracks left the shafts slide right with depth parallax; through the turn they slow and stop; after it they slide left. The sand fan from the turn rises into the beams and makes them flare and churn. Backlit mane strands flare gold and flicker as they cross a beam; the rim light on his face and body breathes as the dust in front of the sun thickens and thins.

TEMPO
Real high-speed slow motion at 24 fps, everything slowed equally: one full stride every 1.8 s, the tempo of @gallop_side_ref. Mane, tail, dust and light keep moving at that same slowed rate, fluid in every frame; crisp frames, a trace of motion blur on hooves and flying sand.

LOOK
Photoreal live-action commercial. Dark covered sand arena, loose churned brown sand, background falling to deep black. Low late sun, warm 3500K, from high openings above and behind him, cutting long volumetric shafts through the dust. White coat with a warm gold rim, full texture in the highlights. Shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: slowed, deep, muffled hoofbeats on each footfall, heavy breathing once per stride, gusting wind, the hiss of thrown sand. No music, no voices.

KEEP CONSISTENT
- He turns toward the camera, never away from it; one 180° turn, nothing more.
- Before the turn his head is at about 40% of the width; after it, at about 60%.
- From 4.0s to the end he is full figure: ears and hooves stay in frame.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts. No text, no people, no tack.
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
- He gallops screen-right for the whole shot; his eye stays at about 37% of the frame width.
- The right half of the frame stays open dark space ahead of him.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts. No text, no people, no tack.
```

## Shot 10 — Very close: the face and eye — 8 s

```text
HH SHOT 10 — 8 s, 21:9 (2.33:1), one continuous slow-motion shot. Very close tracking shot on the grey stallion's face and eye as he gallops screen-right, creeping in on the eye.

REFERENCES
@HH_S10_v01 — THE FIRST FRAME and the look. Framing and his place in frame exactly as this image.
@gallop_side_ref — real gallop, side view: ONLY the leg mechanics and the tempo. It runs screen-left; mirror it, he runs screen-right. Ignore its look and background.

THE HORSE
Grey Iberian stallion: heavy arched neck, deep chest; near-white coat with fine dark flea-bitten freckles, dark slate-grey muzzle, dark brown eyes, long thick wavy silver-white mane and forelock, full silver-white tail, lower legs shading to dark grey, black hooves. Bare, no tack. 100% matches the reference.

CAMERA
Stabilised arm on a tracking vehicle running alongside on his right side at his speed (about 45 km/h), lens at eye height, 18° field of view: long lens, very shallow focus, razor-sharp on the eye. Over the 8 s a very slow push-in toward the eye, about 20% tighter by the end, the eye holding its exact place in frame. Only a faint organic float.
FRAMING: eye at about 39% of the frame width and a third down from the top, nose at about 52%. Neck and mane fill the left side to the edge. The right half of the frame is open dark space ahead of him.

ACTION
0.0–2.0s — The first frame comes alive: the eye wide open, wet, dark brown, a sharp catch-light of the sun in it that shifts as he runs; the head dips and lifts with the stride.
2.0–4.0s — The camera creeps in. A gust lifts the mane, strands whip across the top of the frame; the fine hairs on the muzzle and around the eye quiver in the wind.
4.0–5.0s — He blinks once: the long lashes close and open; the skin around the eye twitches.
5.0–8.0s — The eye looks forward, focused and steady; veins and muscle under the thin skin of the face shift with each stride; dust glitters in the shaft behind him. The shot ends close on the face and eye, still galloping.

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
- He gallops screen-right for the whole shot; the eye stays at about 39% of the frame width.
- The push-in is slow and steady; the eye stays sharp from first frame to last.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts. No text, no people, no tack.
```

## Shot 11 — He gallops straight at the camera, head-on — 25 s

```text
HH SHOT 11 — 25 s, 21:9 (2.33:1), one continuous slow-motion shot. Head-on: the grey stallion gallops straight at the camera, centred, the same size for the whole shot.

REFERENCES
@HH_S11_v01 — THE FIRST FRAME of the clip and the look: the horse head-on, centred, full figure, the dark sand arena, the sun shafts behind him, the dust, the grade. Framing exactly as this image.
@HH_S11_0001-0600 — Blender blocking, ONLY for his position and size in frame: centred, the same size for all 25 s. Ignore its look, rig lines, grid, grey studio and stride speed.
@gallop_side_ref — real gallop, side view: ONLY the leg mechanics and the tempo. Same mechanics, seen from the front. Ignore its look and background.

THE HORSE
Grey Iberian stallion: heavy arched neck, deep chest; near-white coat with fine dark flea-bitten freckles, dark slate-grey muzzle, dark brown eyes, long thick wavy silver-white mane and forelock, full silver-white tail, lower legs shading to dark grey, black hooves. Bare, no tack. 100% matches the reference.

CAMERA
Lens low at the height of his chest, directly in front of him, 18° field of view: long lens, compressed, shallow focus. Stabilised arm on a tracking vehicle driving backwards ahead of him at exactly his speed (about 45 km/h), so he stays centred and the same size for all 25 s, only a faint organic float. Focus on his face.
FRAMING: centred, ears near the top edge, hooves near the bottom edge, both eyes visible, the sun shafts and the dust cloud behind him.

ACTION
0.0–4.0s — The first frame comes alive: he gallops straight at the lens; each stride his chest and head rise and dip, the forelegs fold high toward the lens one after the other and strike, throwing sand forward and sideways; the mane flies out to both sides of his neck and the forelock streams back between his ears.
4.0–7.0s — A gust sweeps across: the mane lifts high and fans to the right, the dust cloud behind him swirls and spreads and breaks up the light behind him.
7.0–10.0s — He runs into a sun shaft that crosses his path: ears, forelock, mane and the dust round his legs flare bright gold, highlights race over the muscles of his chest; at 9.0s he runs out of it, back into the soft backlight.
10.0–14.0s — Focused, ears pricked forward, both eyes on the camera, nostrils flaring on every breath; sand flung by his forelegs flies past the lens out of focus.
14.0–17.0s — At 14.5s his ears flick back and forward again; a stronger gust lifts the mane and blows the dust behind him into a long rolling wave.
17.0–20.0s — He runs through a second sun shaft: the same gold flare across his face, chest and the flying sand, then he runs out of it at 19.0s.
20.0–25.0s — Full power to the end, centred, the same size; the dust cloud behind him fills the background, glowing where the sun cuts through it. The shot ends mid-stride, still galloping at the lens.

GALLOP
The real four-beat gallop of @gallop_side_ref: hind hooves land one after the other, then the forelegs, the leading foreleg reaching far forward, then a moment of suspension with all four legs gathered under the belly. Once per stride the body rises and falls and the head and neck dip as the forelegs land. Hooves plant, grip and leave deep prints. Muscles ripple under the skin, the skin shudders on each landing, nostrils flare with one breath per stride. He truly travels: the sand streams past under him.

WIND, MANE, DUST
The rush of air from his speed plus a gusting wind. The mane streams in thick separate locks back and out to both sides of his neck, rippling in waves from crest to tips, each wave half a beat behind the dip of his head; tips whip and curl, flyaway hairs glow in the backlight, locks cross and separate all the time. The forelock flutters. Hoof strikes throw sand that arcs up and falls back; the fine dust hangs, rolls away behind him and the gusts tear it into streamers. Dust in three depths: soft grains drifting past the lens, rolling clouds around him, thin haze far back in the dark.

LIGHT IN MOTION
The sun shafts are light on moving dust, so they never hold still: as dust rolls through them the beams thicken, thin, shimmer and break up, and motes glitter as they cross them. The shafts stand across his path like pillars of light in the dust; with the camera retreating they drift slowly, and the dust he throws keeps churning through them. Backlit mane strands flare gold and flicker as they cross a beam; the rim light on his face and body breathes as the dust in front of the sun thickens and thins.

TEMPO
Real high-speed slow motion at 24 fps, everything slowed equally: one full stride every 1.8 s, the tempo of @gallop_side_ref. Mane, tail, dust and light keep moving at that same slowed rate, fluid in every frame; crisp frames, a trace of motion blur on hooves and flying sand.

LOOK
Photoreal live-action commercial. Dark covered sand arena, loose churned brown sand, background falling to deep black. Low late sun, warm 3500K, from high openings above and behind him, cutting long volumetric shafts through the dust. White coat with a warm gold rim, full texture in the highlights. Shallow depth of field, deep clean blacks, amber-gold dust, punchy contrast, fine natural grain. 21:9.

SOUND
Only: slowed, deep, muffled hoofbeats on each footfall, heavy breathing once per stride, gusting wind, the hiss of thrown sand. No music, no voices.

KEEP CONSISTENT
- He gallops straight at the lens for all 25 s: centred, the same size, ears and hooves in frame.
- The sun shafts stay behind him and across his path; he passes through two of them.
- Mane, tail and dust move in every frame; the sun shafts shimmer and drift in every frame.
- Eyes open, wet, alive.
- One continuous shot, no cuts. No text, no people, no tack.
```
