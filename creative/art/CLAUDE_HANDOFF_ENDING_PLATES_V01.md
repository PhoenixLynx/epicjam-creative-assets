# Ending plates v01 — seven review drafts

Paths relative to Music_Video_Assets. Individual director approval, level continuity and import tests pending. No game changes by Sol.

| Request / function | File under creative/art/exports/ | Spec |
|---|---|---|
| ART-011 cake top | ART-011_cake_top_1024x1024_v01.png | 1024x1024 RGBA, transparent outside cake and missing wedge |
| ART-012a employee at desk from behind | ART-012a_desk_1920x1080_v01.png | 1920x1080, opaque RGBA |
| ART-012b conference call | ART-012b_conference_1920x1080_v01.png | 1920x1080, opaque RGBA |
| ART-012c Corridor B | ART-012c_corridor_1920x1080_v01.png | 1920x1080, opaque RGBA |
| ART-012d ward | ART-012d_ward_1920x1080_v01.png | 1920x1080, opaque RGBA |
| ART-014 dusk skyline | ART-014_skyline_4096x1024_v01.png | 4096x1024, opaque RGBA, single non-seamless plate |
| ART-015 optional soundstage | ART-015_soundstage_2048x1024_v01.png | 2048x1024, opaque RGBA |

All generated at smaller native resolution then cropped/resampled to exact requested dimensions. Native masters under creative/art/source/<asset>_original_v01.png are preserved. Full prompts: creative/provenance/ART_ending_plates_v01_prompts.json; per-file/source/reference hashes and dimensions: ART_ending_plates_v01.json. Built-in image_gen plus System.Drawing used. No external image references; monitor illustrations use read-only project campus screenshot as palette/layout reference. They are reconstructions, NOT gameplay captures or proof of actual level geometry.

Cake: text reads THAT'S A WRAP, 4471. Use top plane/decal UVs, preserve alpha and test dark/bright background halos. The generated wedge is a partial edge bite, not a perfectly radial cut; do not assume mesh alignment. A transparent top texture over an opaque solid cylinder will NOT remove physical cake: choose suitable masked top/mesh treatment or keep this a surface illustration. Do not rebuild mesh without director scope decision. Check text at player distance.

Dailies: fictional TAKE 4471 and timecodes are burned in by the export script, not real recording metadata. Apply to static monitor surfaces and keep center LIVE CAMERA monitor implementation intact. No demand to match these scenes by rebuilding levels. Ward is a clinical interpretation without a verified ward screenshot; compare against actual built ward before approval. Screenshot-inspired room layouts are approximate. Proposed texture names T_Dailies_Desk, T_Dailies_Conference, T_Dailies_CorridorB, T_Dailies_Ward.

Skyline: use a flat distant backdrop on penthouse open side, clamp sampling; not equirectangular or seamless, so do not wrap on a sky sphere. Align horizon to current camera. Proposed T_PenthouseSkyline; brightness/emission should be tuned in level.

Optional soundstage: view behind flats with lighting rigs, C-stands, badges numbered 4466–4470 and an empty sixth hook. Exact badge numbering added after generation; source has blank badge fronts. A static background/image candidate, not new 3D scenery. Proposed T_SoundstageReveal. Avoid obscuring existing reveal geometry.

Acceptance: human visual approval; textures fit existing UV/aspect ratio, correct color/gamma, no stretching; all labels legible at actual camera distance; cake alpha and wedge treated deliberately; monitor live feed remains separate; skyline horizon sensible. Unresolved: final selection, ward match, cake geometry and actual import result. Source export script creative/art/export_ending_plates_v01.ps1 reproduces cropping and overlays using installed Consolas (pixels only, no font redistribution).
