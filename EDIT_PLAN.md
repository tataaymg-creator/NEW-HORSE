# HH — edit plan, shots 03–11

Everything runs at 24 fps and 21:9. Times are seconds on the timeline from the first frame of shot 03; add the length of shots 01–02 in front if they exist. Total for shots 03–11: **103 s (1:43)**.

## Cut list

| Shot | Timeline | Length | Source | In → out on the source | Notes |
|---|---|---|---|---|---|
| 03 | 0–8 | 8 | shot 03 take | 0.0 → 8.0 | Medium, heading right. |
| 04 | 8–22 | 14 | shot 04 take | 0.0 → 14.0 | Very close, heading right. |
| 05 | 22–30 | 8 | shot 05 take | 0.0 → 8.0 (drop frame 193) | The turn, right → left. Fix the background first (see below). |
| 06 | 30–38 | 8 | shot 06 take | 0.0 → 8.0 | Wide, four horses, heading left. |
| 07 | 38–52 | 14 | shot 07 take | 0.0 → 14.0 | Two heads, heading left. |
| 08 | 52–63 | 11 | **`HH_S08_from_S05.mp4`** (built from `SHOT 5.mp4`) | 0.0 → 11.0 | The turn back, left → right. Mirrored, eased speed ramp. |
| 09 | 63–70 | 7 | **`HH_S09_from_S03.mp4`** (built from `shot 3.mp4`) | 0.0 → 7.0 | Heading right. Not mirrored, 1.3× punch-in. |
| 10 | 70–78 | 8 | **`HH_S10_from_S03.mp4`** (built from `shot 3.mp4`) | 0.0 → 8.0 | Face and eye, heading right. Eye-following crop with a slow push-in. |
| 11 | 78–103 | 25 | shot 11 take (wide track-back) | 0.0 → 25.0 | Ends on a frame full of dust. |

All hard cuts. Screen direction holds across every cut: right (03–05 in), left (05 out–08 in), right (08 out–10), head-on (11). For rhythm, cut on a hoof strike: one full stride is 1.8 s in every shot.

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

## Shot 10 from the shot 03 take — built: `HH_S10_from_S03.mp4`

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
- **The end:** shot 11 finishes on 1 s of frame-filling dust (24–25 s). Cut or dissolve (about 12 frames) from there into the end card or packshot.
