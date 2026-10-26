# HH — edit plan, shots 02–11

Everything runs at 24 fps and 21:9. Times are seconds on the timeline from the first frame of shot 02; add the length of shot 01 in front if it exists. Total for shots 02–11: **91 s (1:31)**.

## Cut list

| Shot | Timeline | Length | Source | In → out on the source | Notes |
|---|---|---|---|---|---|
| 02 | 0–5 | 5 | shot 02 take (close dust plate, from `HH_S02_v01`) | 0.0 → 5.0 | Title space on the right half and top. Opens small before the horse. |
| 03 | 5–13 | 8 | shot 03 take | 0.0 → 8.0 | Medium, heading right. |
| 04 | 13–27 | 14 | shot 04 take | 0.0 → 14.0 | Very close, heading right. |
| 05 | 27–35 | 8 | shot 05 take | 0.0 → 8.0 (drop frame 193) | The turn, right → left. Fix the background first (see below). |
| 06 | 35–43 | 8 | shot 06 take | 0.0 → 8.0 | Wide, four horses, heading left. |
| 07 | 43–57 | 14 | shot 07 take | 0.0 → 14.0 | Two heads, heading left. |
| 08 | 57–68 | 11 | **`HH_S08_from_S05.mp4`** (built from `SHOT 5.mp4`) | 0.0 → 11.0 | The turn back, left → right. Mirrored, eased speed ramp. |
| 09 | 68–75 | 7 | **`HH_S09_from_S03.mp4`** (built from `shot 3.mp4`) | 0.0 → 7.0 | Heading right. Not mirrored, 1.3× punch-in. |
| 10 | 75–83 | 8 | shot 10 take (client version, from `HH_S10_v03`) | 0.0 → 8.0 | Extreme close-up from above, standing still: he slowly closes and opens his eye in the wind. Eye on the right third. |
| 11 | 83–91 | 8 | shot 11 take (wide, 50 mm look, from `HH_S11_v03`) | 0.0 → 8.0 | Ends on a frame full of dust (7–8 s). |

All hard cuts. Screen direction holds across the running shots: right (03–05 in), left (05 out–08 in), right (08 out–09), head-on (11). Shot 10 is a still portrait facing left, which reads as a new moment after shot 09; to keep it facing right, flip `HH_S10_v03` before animating it (the eye then sits on the left third). For rhythm, cut the running shots on a hoof strike: one full stride is 1.8 s in every shot.

## Shot 08 from the shot 05 take — built: `HH_S08_from_S05.mp4`

Source: `SHOT 5.mp4` (the fixed take), frames 0–191.

1. Speed ramp on the source: 0.0–2.75 s at 100% → 2.75–5.75 s at 50% → 5.75–8.0 s at 100%. That is 2.75 + 6.0 + 2.25 = **11.0 s** (264 frames). In this take the turn runs about 2.5–6.0 s with the head-on moment at 4.25–5.25 s, so the slow section sits on it; on the timeline he is head-on at about 5–8 s.
2. Each speed change eases over 8 frames (cosine), centred on 2.75 s and 8.75 s of the output.
3. In-between frames: ffmpeg motion-compensated interpolation at 4× over source frames 58–146, so the slow section and the eases land on real or quarter-frame positions.
4. Flipped horizontally. No audio. HEVC 10-bit, 2206×946, 24 fps, BT.709.
5. The interpolated section went through 8-bit. Good for the client preview; for the final, redo the same ramp on the upscaled take in Resolve Speed Warp or Topaz (same ramp points), and check the flying sand in the 50% section.

## Shot 09 from the shot 03 take — built: `HH_S09_from_S03.mp4`

Source: `shot 3.mp4`.

1. Not mirrored: shot 03 already faces right, and shots 08 → 09 → 10 all head right.
2. Source 1.0 → 8.0 s (frames 24–191, 168 frames = **7.0 s**), so it does not open on the same frame as shot 03.
3. Punch-in 1.3×: crop 1698×728 at x 370, y 0, scaled back to 2206×946 (Lanczos). The crop is anchored to the top because his ears already touch the top edge of the source; his eye lands at about 39% across, nose about 53%.
4. No audio. HEVC 10-bit, 2206×946, 24 fps, BT.709.
5. After upscaling, redo it from the upscaled `shot 3.mp4` with the same numbers scaled up (e.g. at 2× source: crop 3396×1456 at x 740, y 0).

## Shot 10 from the shot 03 take — built: `HH_S10_from_S03.mp4` (replaced)

The client's close-up replaces this clip: shot 10 is now generated from `HH_S10_v03` (still prompt in `HH_S10_STILL_PROMPT.md`, motion prompt in `SEEDANCE_PROMPTS.md`). Keep it only as a fallback.

Source: `shot 3.mp4`, frames 0–191 (**8.0 s**). Shot 09 uses 1.0–8.0 s of the same take right before it, so shot 10 is framed much tighter to read as a new shot.

1. Face-and-eye crop: zoom 1.80× at the start easing to 2.16× at the end (20% push-in, as in the shot 10 prompt).
2. The eye was tracked in every frame (template match, score ≥ 0.93). The virtual camera follows its slow drift fully and 60% of the stride bob with a short lag, like an operator on a long lens. The eye stays at 37–41% across and 28–44% down, matching `HH_S10_v01` (39%, 36%).
3. Lanczos resampling in 10-bit. No audio. HEVC 10-bit, 2206×946, 24 fps, BT.709.
4. Watch for: the sun shafts arrive on the right in the last 2–3 s of both shot 09 and shot 10 (same source). If the pair reads as a repeat, build shot 10 from the shot 04 take instead: different footage, already close, and 50 s away from where it is first used.
5. After upscaling, redo it from the upscaled take; at 2× zoom it is the softest of the reused shots.

## Fixes on the first shot 05 take

Only if you keep that take; a re-roll with the v2 prompt should not need them. Positions are for the unmirrored take.

| What | When | Where | Fix |
|---|---|---|---|
| Arena windows and roof frame | 0.0–1.5 s | top edge, up to ~22% down at frame 1, shrinking to nothing by 1.5 s | Feathered black gradient or mask over the top strip, keyed off as they leave |
| Windows again | 7.7–8.0 s | top-left, 0–40% across, top ~10% | Same mask |
| Sand clump that turns into a tiny figure | 7.17–7.67 s (frames 172–184) | lower right on the sand, moving from ~77% to ~87% across, ~90% down | Patch or object removal (Content-Aware Fill, Resolve patch replacer); 12 frames |

In the mirrored shot 08 these move to 0.0–1.5 s and 10.7–11.0 s (top, now top-right for the second one) and 10.2–10.7 s (lower left, ~13–23% across).

## Finishing

- **Upscale every take before grading.** The Higgsfield takes are 992×432. Upscale all of them with the same model and settings (e.g. to 3840×1646) so detail matches from shot to shot.
- **Grade to the stills.** Match every shot to the `HH_Sxx_v01` frames: deep clean blacks, warm amber dust, white coat with full texture in the highlights. Check the sun shafts did not get flattened.
- **One grain pass over the whole timeline.** The same grain over every shot glues AI shots together better than each shot's own texture.
- **Flicker:** if a take shimmers, use a light deflicker and keep the strength low. It must not freeze the moving light in the dust, which is what makes these shots read as real.
- **Sound:** mute all generated audio and build one track for the whole piece: music plus one consistent set of slowed hoofbeats, breathing, wind and sand. The generated sound changes from shot to shot, and it is wrong on any retimed or mirrored clip.
- **The end:** shot 11 finishes on 1 s of frame-filling dust (7–8 s). Cut or dissolve (about 12 frames) from there into the end card or packshot.

## Lyric overlay — `HH_Lyrics_AE.jsx`

Run it in After Effects (File > Scripts > Run Script File…). It builds the comp `HH_Lyrics`: 2206×946, 24 fps, 44 s, transparent, white text, font «ديوان مد» (change `FONT` at the top of the script, or run `HH_Lyrics_SetFont.jsx` to swap the font on every line).

| Time | Text | Where |
|---|---|---|
| 0–5 | هامة المجد / كلمات الشيخ محمد بن راشد آل مكتوم | Right half, upper part: shot 02's title space (0–5 s on the timeline) |
| 5–44 | 13 lyric lines, 3 s each | Centred in the lower part of the frame, from the start of shot 03 |

- Each line: words appear in reading order out of a soft blur, rising slightly into place (0.9 s); a slow 2% push while it holds; then it dissolves upward with a blur (last 0.6 s). The title gets a warm gold glint passing through it at 2.0–3.4 s.
- A soft dark halo (Drop Shadow at 0 distance) sits in the alpha so the white text stays readable over bright dust. Turn it off with `SHADOW = false`.
- Render: the comp goes into the Render Queue with the "High Quality with Alpha" output module. Lay the result over the edit starting at shot 02. Each line also has a comp marker, so you can slide lines to the music.
- Arabic needs Preferences > Type > Text Engine > South Asian and Middle Eastern (restart After Effects). If the words appear left to right, set `REVEAL_REVERSED = true` and run again.
- For the upscaled final, set `WIDTH`/`HEIGHT` (e.g. 3840×1646) and run again: sizes and positions are fractions of the frame.

## Lyric overlay from the lettering SVG — `HH_Lyrics_SVG_AE.jsx` (use this one)

Built from `lyrics_svg/lyrics_svg.svg` (your lettering), so no font is needed. Run it in After Effects (File > Scripts > Run Script File…). It builds the comp `HH_Lyrics_SVG`: 2206×946, 24 fps, 44 s, transparent, pure white shape layers.

| Time | Block | Where (dark space of the shot underneath) |
|---|---|---|
| 0–5 | Title «هامة المجد» + credit | Right half, upper part: shot 02's title space |
| 5–29 | Lines 1–8 | Right of the horse, shots 03–04 (line 8 higher, clear of his head at the start of shot 05) |
| 29–35 | Lines 9–10 | Upper left, shot 05 (he turns, then leaves on the right) |
| 35–44 | Lines 11–13 | Top centre, above the four horses in shot 06 |

- Each row of lettering is written right to left behind a soft edge, with a warm light riding the pen tip; the rows of a line follow each other 0.3 s apart. The line rises gently into place, holds on a slow 2% push, and in its last 0.6 s breaks up like dust, blurs and fades upward.
- Every line uses the same scale (`LYRIC_WIDTH`), so the lettering stays one size. Positions are in `LYRIC_POS` (one [x, y] per line, fractions of the frame); move any line there and run again.
- If the edit changes, check each line against its shot: white lettering over the white horse is hard to read.
- To change the lettering: replace `lyrics_svg/lyrics_svg.svg` (same structure: the title as loose shapes, the credit and each line in its own group, a gap between blocks) and run `python3 tools/svg_to_ae.py jsx lyrics_svg/lyrics_svg.svg HH_Lyrics_SVG_AE.jsx`. `python3 tools/svg_to_ae.py report lyrics_svg/lyrics_svg.svg` lists the blocks and rows it finds.

### Extra lines — `HH_Lyrics_SVG_Extra_AE.jsx`

A separate comp, `HH_Lyrics_SVG_Extra`: 11 s, transparent, same lettering size and motion as the main lyric comp. Each entry is on screen alone, one after the other:

| Time | Entry | Layout |
|---|---|---|
| 0–2 | من قوباسك ما | one line (row 1 of line 10 plus the word «ما») |
| 2–4 | يعرف عزمك الانهيار | one line (the word «يعرف» plus row 3 of line 10) |
| 4–6 | على خطى فكرتك تضوي مصابيحها | its three rows, as in the artwork |
| 6–11 | إللي تسابق على مضمارها ريحها | one line, written as one continuous stroke |

- The 2 s entries write, settle and dissolve proportionally faster (write 0.4–0.9 s, hold, 0.5 s dissolve). Durations are in `DURATIONS`, positions in `LYRIC_POS` (all centred for now), and `ORDER` reorders the entries.
- Regenerate after changing the SVG: `python3 tools/svg_to_ae.py jsx lyrics_svg/lyrics_svg.svg HH_Lyrics_SVG_Extra_AE.jsx "11.r1+11.r2w1s,11.r2w2+11.r3s,14,8s"`. Entries are separated by commas; parts are blocks (0 title, 1 credit, line n = n+1), rows (`.r2`) or words (`.r2w1`, rightmost first) joined with `+`; a trailing `s` sets the entry on one straight line.
