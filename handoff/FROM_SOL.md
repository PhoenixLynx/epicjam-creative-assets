# From Sol to the director and Claude
## Ending plates second batch — all remaining requested slots have review drafts

Cake ART-011, four dailies ART-012a–d, dusk skyline ART-014 and optional soundstage ART-015 exported. Exact paths/dimensions/integration notes: creative/art/CLAUDE_HANDOFF_ENDING_PLATES_V01.md. Full prompts, source masters and hashes saved. All await individual director approval and in-game tests; no imports or game changes by Sol. Ward is illustrative and needs continuity check. Cake alpha cannot remove solid cylinder geometry; generated wedge is a partial edge bite, not exact radial geometry. Skyline is flat/non-seamless. Monitor timecodes are fictional, and the central live camera should remain live. This follows the earlier banner/cards/menu batch; nothing asks for a level rebuild.

## Ending signs first batch — four exports awaiting director review

ART-010 wrap banner, ART-013 blank/revealed director cards, ART-016 overtime menu are exported. Exact paths, dimensions, proposed Unreal texture names and tests: creative/art/CLAUDE_HANDOFF_ENDING_SIGNS_V01.md. Source is editable export_ending_signs_v01.ps1; no imagegen used for these typography/geometry assets. Human approved doing the work; individual drafts await approval. Menu includes proposed additional copy. Check square menu against existing portrait board UVs. No game changes or imports by Sol. Cake, dailies, skyline and optional soundstage remain pending.

## APPROVED BY DIRECTOR: Stalker face v01 — use this for the stalker

The director selected the curled-grin Fear exploration v07 specifically as the STALKER face: "Yeah that looks much better...I think we should use this for the stalker's face." This approval is for the stalker, not a replacement for ordinary coworker Fear.

Claude Integration Handoff
- Asset: approved stalker face v01.
- Exact creative repo path: creative/art/exports/ART-001_face_stalker_1024_v01.png.
- Format: 1024x1024 RGBA PNG; transparent corners, red eyes without whites, thin brows, dark under-eye rings, slim charcoal grin with outward-curled ends.
- Function: stalker character face. Assign only to stalker; preserve existing coworker Calm/Fear/Neutral/Frown mapping.
- Proposed game names: T_Face_Stalker / MI_Face_Stalker (adapt to your existing stalker asset convention). Reuse curved head-bone face-card material pipeline where compatible; confirm actual stalker mesh/UVs first.
- Dependencies: byte-identical labeled copy of creative/art/exports/ART-001_face_fear_intense_1024_uncanny_v07.png; original source master is creative/art/source/ART-001_face_fear_intense_uncanny_v07.png. Earlier versions retained.
- Glow: red glow is painted in the texture. For actual emission, isolate red eye pixels in material or request a dedicated mask. No emissive material has been implemented by Sol.
- Acceptance: stalker uses this face only; compare alignment/scale on actual head, curls and thin strokes readable at 2m/5m, alpha edges clean with existing cutoff (reported 0.12), no regressions to other character faces.
- Unresolved: actual stalker import/assignment, UV fit, emissive setup and in-game playtest. Human art selection approved; integration NOT confirmed. Please report integration status in FROM_CLAUDE.md.

Source, prompt and reference ancestry: creative/provenance/ART-001_fear_intense_uncanny_v07*.json. Labeled asset record: creative/provenance/ART-001_stalker_v01.json. Local files available now; no git commit/push claimed. No game files changed by Sol.

## Intense Fear v06 — lighter strokes, corrected smile ends

Human requested thinner mouth/eyebrows and reversal of inward smile curl. Export: creative/art/exports/ART-001_face_fear_intense_1024_uncanny_v06.png (1024x1024 RGBA PNG, transparent corners verified). Source: creative/art/source/ART-001_face_fear_intense_uncanny_v06.png. Slender eyebrows and charcoal smile with outward/upward tips; red eyes without whites and layered under-eye rings retained. Candidate awaiting human approval; earlier versions preserved.

Claude Integration Handoff: alternative for existing T_Face_Fear / MI_Face_Fear on curved M_Face card, existing triggers unchanged. Check thinner strokes at 2m and 5m, UV/feature alignment during swaps, smile shape on round head, alpha halos at existing cutoff 0.12. Glow remains painted; actual emissive mask/material setup unresolved. No game edits or integration by Sol.

Re-export: export_faces.ps1 -Variants fear_intense -Revision uncanny_v06. Built-in image_gen prompts, source/export/reference hashes and provenance: creative/provenance/ART-001_fear_intense_uncanny_v06*.json. Doll reference mood-only, rights unverified and not redistributed. Exact creation UTC unknown; observed UTC recorded; commit pending.

## Intense Fear v05 — charcoal curled grin, no eye whites

Human requested neutral charcoal mouth, red glowing eyes without any white, more curled doll-smile corners. Candidate export: creative/art/exports/ART-001_face_fear_intense_1024_uncanny_v05.png (1024x1024 RGBA PNG; transparent corners checked). Source: creative/art/source/ART-001_face_fear_intense_uncanny_v05.png. Prior variants preserved; awaiting human approval.

Claude Integration Handoff: alternative for existing T_Face_Fear / MI_Face_Fear on curved head-bone M_Face card. Existing Fear behavior only; no new state/trigger. Glow is painted into color, actual emission not implemented. Optional emissive mask must isolate red eyes, not entire face. Acceptance: human approves on head; verify UV footprint, swap alignment, curled smile ends, ring readability and alpha halos at 2m/5m using existing cutoff 0.12. Final selection and emissive setup unresolved. No game edits by Sol.

Re-export: export_faces.ps1 -Variants fear_intense -Revision uncanny_v05. Built-in image_gen prompt, source/export/reference hashes and provenance: creative/provenance/ART-001_fear_intense_uncanny_v05*.json. External doll reference remains mood-only, rights unverified, not redistributed. Observed record UTC saved, exact creation time unknown, commit pending.

## Intense Fear v04 — deeper doll grin and red eye glow

Human requested closer doll-reference grin geometry, additional dark circles and glowing eyes. New review candidate: creative/art/exports/ART-001_face_fear_intense_1024_uncanny_v04.png (1024x1024 RGBA PNG; transparent corners verified). Source: creative/art/source/ART-001_face_fear_intense_uncanny_v04.png. Deep tapered open smile, layered slim under-eye rings and red glowing irises. Prior candidates retained; human approval pending.

Claude Integration Handoff: candidate for existing T_Face_Fear / MI_Face_Fear on curved M_Face head card. Keep existing Fear trigger/state; no new gameplay mode implemented. Glow is PAINTED into base-color PNG, not an emissive map. For actual emission, isolate red iris pixels in a material mask or request a dedicated mask; do not make the entire face emissive. Bloom depends on rendering/postprocess settings. Sol has not changed any materials or game files.

Acceptance: director approves on-head appearance; verify broad footprint fits UVs and swaps align, grin and rings readable at 2m/5m, masked-alpha cutoff 0.12 produces no halos, and any optional emission stays confined to eyes. Actual emissive implementation and final selection unresolved.

Re-export: export_faces.ps1 -Variants fear_intense -Revision uncanny_v04. Built-in image_gen prompt and source/export/reference hashes: creative/provenance/ART-001_fear_intense_uncanny_v04*.json. Both external doll references used for expression only, rights unverified, not redistributed. Exact original creation UTC unknown; observed record UTC saved; commit pending.

## Intense Fear v03 — creepy doll smile candidate

Human requested a stretched creepy doll-like smile using supplied mood reference. Export: creative/art/exports/ART-001_face_fear_intense_1024_uncanny_v03.png — 1024x1024 RGBA PNG, verified transparent corners. Source: creative/art/source/ART-001_face_fear_intense_uncanny_v03.png. Replaces triangular fangs with a dark asymmetric crescent smile and a small central off-white sliver. Eyes and thin under-eye shadows retained. Earlier variants preserved; final human approval pending.

Claude Integration Handoff: alternative for existing T_Face_Fear / MI_Face_Fear, existing curved M_Face head card and masked alpha cutoff 0.12. No extra gameplay state requested. Check broad facial footprint/UV fit, smile corner clipping, swap alignment, readability at 2m/5m and alpha halos. Human chooses candidate before replacement; no game edits or imports by Sol.

Re-export: export_faces.ps1 -Variants fear_intense -Revision uncanny_v03. Built-in image_gen used. Prompt, source/export/reference hashes, recorded UTC and provenance: creative/provenance/ART-001_fear_intense_uncanny_v03*.json. External doll reference is mood-only, rights unverified, not redistributed. Exact generation UTC unknown; commit pending.

## Intense Fear v02 — thinner shadows and sharp grin

Human rejected v01 eye bags as panda-like and requested earlier Fear shading balance plus scary monster reference. New candidate: creative/art/exports/ART-001_face_fear_intense_1024_uncanny_v02.png (1024x1024 RGBA PNG, transparent corners). Slim tapered under-eye crescents, pointed eyes, sharp-toothed grin. Previous versions retained. Human approval pending.

Claude Integration Handoff: potential replacement for existing T_Face_Fear / MI_Face_Fear; use existing curved M_Face card and alpha-mask settings. No new state/trigger requested. IMPORTANT: generated face occupies a larger texture footprint than the previous set; check face-card bounds and UV scale, swap alignment, teeth and eye readability at 2m/5m, and edge halos before accepting. Do not blindly replace current import. Final choice remains unresolved; no game-folder edits by Sol.

Original: creative/art/source/ART-001_face_fear_intense_uncanny_v02.png. Reproduce export: export_faces.ps1 -Variants fear_intense -Revision uncanny_v02. Prompts, source/export/reference SHA-256 and provenance: creative/provenance/ART-001_fear_intense_uncanny_v02*.json. External monster image used as mood reference, authorship/license unverified, not redistributed. Built-in image_gen used. Exact creation UTC unknown; record UTC saved; commit pending.

## Intense Fear mannequin-mask candidate — uncanny v01

Human requested a scarier alternative with more noticeable dark circles. Export: creative/art/exports/ART-001_face_fear_intense_1024_uncanny_v01.png (1024x1024 RGBA PNG, transparent corners). Source: creative/art/source/ART-001_face_fear_intense_uncanny_v01.png. Larger dark charcoal-violet eye circles, pale eye slivers, fixed pupils and tense smile. Original Fear remains intact.

Claude Integration Handoff: alternative for existing T_Face_Fear / MI_Face_Fear on curved head-bone M_Face card. This is an art candidate, not authorization to introduce another gameplay state or new trigger. Human must choose replacement versus a separate intensity stage. Existing masked alpha cutoff reported 0.12; check circle silhouette, white eyes and edge halos at 2m and 5m, plus UV alignment during swaps. Final approval and integration pending. No game-folder changes by Sol.

Built-in image_gen prompt, source/reference/export hashes and provenance: creative/provenance/ART-001_fear_intense_uncanny_v01*.json. Re-export: export_faces.ps1 -Variants fear_intense -Revision uncanny_v01. Exact original creation timestamp unknown; observed record UTC saved; git commit pending.


## Uncanny minimalist face set v01 — ready for review

Four new transparent 1024x1024 expressions: calm, fear, neutral and frown. Exact paths, existing material mapping and acceptance checks: creative/art/CLAUDE_HANDOFF_UNCANNY_FACES_V01.md. New suffix _1024_uncanny_v01.png; old filenames deliberately preserved, so current hooks will NOT auto-select these. Human requested generation; final approval and on-head test pending. No game changes by Sol. Full provenance and prompts saved under creative/provenance/ART-001_uncanny_v01*.json.


## Key-pass revision: lobby v11 and cover v02

Human prefers v10 level of detail; requested lighter pass/cord and glyphs. New review exports:
- creative/art/exports/title_keyart_v11.png: 1920x1080 PNG, no HUD or main title.
- creative/art/exports/itch_cover_art_v02.png: 630x500 art-only, plus itch_cover_art_315_v02.png at 315x250.
- creative/art/exports/itch_cover_working_title_v02.png: 630x500 provisional TAKE 4471 overlay, plus itch_cover_working_title_315_v02.png at 315x250.

Claude Integration Handoff: use as title texture / itch cover only after human selection. Same proposed /Game/UI/Title/T_TitleLobby destination; no level geometry changes implied. Generated originals preserved; export_title.ps1 -Revision v11 and export_cover.ps1 -Revision v02 reproduce exact-size exports. Branding retained on card; Witness/Reel/Eye markings are illustrative approximations, NOT functional puzzle clues or replacements for glyph UI. No baked HUD. Acceptance: human approval of pass design, menu contrast and crop tested in game, cover readable at 315x250. Final title remains unresolved. No integration claimed. Full prompts, dimensions, source/export/reference hashes recorded in creative/provenance/ART_keypass*.json. External references are construction references only; rights unverified.


## New lobby background v10 and ART-003 cover draft

Human wants a new background in addition to ongoing cover work; game title is provisional.

- `creative/art/exports/title_keyart_v10.png`: new reception-lobby composition, 1920x1080 RGB, NO baked HUD/title/menu; live UI can be placed separately. Front-facing director chair and HALCYON palette retained. This is conceptual art, not an implemented lobby rebuild.
- `creative/art/exports/itch_cover_working_title_v01.png`: 630x500 PNG cover mockup, TAKE 4471 is a WORKING TITLE.
- `creative/art/exports/itch_cover_working_title_315_v01.png`: 315x250 thumbnail check, inspected visually.
- `creative/art/exports/itch_cover_art_v01.png` and `itch_cover_art_315_v01.png`: art-only versions without game title. Branding on physical props remains.

Cover title is drawn separately by `creative/art/export_cover.ps1` with TitleLine1/TitleLine2 parameters, so it can be changed without image regeneration. Default Arial Bold system font is rendered into PNG, no font files redistributed. Lobby export: export_title.ps1 -Revision v10. Full source images, generation prompts and hashes preserved; provenance `ART_cover_lobby_outputs.json`. No new external image inputs, prior artwork ancestry retained.

Both drafts await human review; no final title decision, itch upload or game import claimed. Cover acceptance: final approved title readable at 315x250, no text clipping; lobby acceptance: live title/menu contrast/viewport cropping checked in actual widget. Proposed lobby texture `/Game/UI/Title/T_TitleLobby`; adapt to existing convention. No game changes by Sol.

## Neutral filename aligned with 14:55 hook

Added `creative/art/exports/ART-001_face_neutral_1024_v01.png` as byte-identical copy of `ART-001_face_guard_1024_v01.png`; original retained. Frown path already matches your hook. Reviewed your ~4s hit-frown plan, so duration is no longer unresolved in our proposed mapping. Your note also confirms original calm/Fear faces show in game. New neutral/frown import and readability still need confirmation; no integration claimed for these new files.

## Director suggestion: rotate title mockups

Human likes several v09 alternatives and suggests Claude could shuffle among them. Candidate set: `creative/art/exports/title_keyart_v09a.png`, `title_keyart_v09b.png`, `title_keyart_v09c.png`. No final subset selected yet. Prefer choosing one per title-screen entry to keep UI steady; timed crossfade is optional only if scope permits. Keep live menu position/focus stable and avoid abrupt movement during selection. All three still contain baked corner HUD; prevent duplicate live HUD. This is a scope proposal, not a request to interrupt Act 3 or proof of implementation.

## ART-002 v09 A/B/C - office composition exploration

Human authorized several variations. Three 1920x1080 RGB mockups, all retaining front-facing director chair, branding, corner HUD and title/menu space:

- `creative/art/exports/title_keyart_v09a.png`: wide office, bright morning, smaller chair, long workstation depth and glass conference frontage.
- `creative/art/exports/title_keyart_v09b.png`: desk-level viewpoint, warm side light, personal foreground, cooler room beyond.
- `creative/art/exports/title_keyart_v09c.png`: glass threshold/frame, cool light and more enclosed observational atmosphere.

All exploratory, awaiting director selection; no final implementation approval. Preserve earlier versions. Baked HUD caveat remains. Generated originals, exact-size export script revisions, full prompts and per-output source/export hashes saved under creative/. No new external image inputs (all based on v08); earlier reference ancestry retained. Do not rebuild level geometry to match exploration without human scope approval. Sol preference: A for clear title composition, B for grounded player viewpoint, C for unease.

## ART-002 v08 - corrected intent: new OFFICE viewpoint, chair faces viewer

Human clarified requested perspective change was the OFFICE, not chair orientation. v07 rear-chair idea is superseded as a direction. New review: `creative/art/exports/title_keyart_v08.png`, 1920x1080 RGB. Room now viewed diagonally with left foreground employee desk, glass office depth left, receding blue-grey wall and right corner; director chair faces camera. Same palette, branding, HUD and simple surfaces retained.

Human approval pending; not final submission approval. Source based on v06, earlier variants preserved. Source/export/prompt/hashes recorded under ART-002 v08; export script -Revision v08. Static HUD still baked into review plate. Game folder untouched; no level-rebuild request implied.

## ART-002 v07 - direct rear-view chair alternative

File: `creative/art/exports/title_keyart_v07.png`, verified 1920x1080 RGB PNG. Human says prior work is usable provisionally but chair perspective is unsuitable for final submission; better references may follow. v07 tries a direct rear-facing chair instead of the ambiguous three-quarter frame, preserving room/HUD/desk composition. Still a review alternative, not final submission approval or physically verified construction.

Source master, exact-size export script (-Revision v07), full prompt and hashes retained. See `creative/provenance/ART-002_prompt_v07.json` and `ART-002_v07.json`. No new external inputs. Earlier title versions preserved; static-HUD caveat remains. No game files changed.

## New face variants + ART-002 v06 - awaiting director review

Human requested neutral security guard and frown on thrown-object impact, alongside title simplification/chair perspective correction. Exported:

- `creative/art/exports/ART-001_face_guard_1024_v01.png`: neutral guard default, steady brows, firm mouth, modest catchlights.
- `creative/art/exports/ART-001_face_frown_1024_v01.png`: visibly annoyed brows/downturned mouth, no Fear bags or evil grin.
- `creative/art/exports/title_keyart_v06.png`: 1920x1080 RGB, reduced surface microtexture, revised chair perspective/frame. Chair still subject to human perspective review, not claimed mathematically correct.

Both faces verified 1024x1024 RGBA with alpha range 0-255; matching thick graphic style based on existing calm v03. Use existing curved head-bone card and mapping; compare alignment on actual round head. Face outputs await director approval before ready status. No integration claimed.

Proposed reaction mapping for director/Claude confirmation: normal guard -> neutral; normal coworker -> calm; normal-state object hit -> frown; Fear staring/hit -> existing Fear face takes priority. Hit-frown duration/return behavior is unresolved; do not overwrite existing Fear state logic or change reaction dialogue just for these textures. Suggested assets `/Game/Art/Characters/Faces/T_Face_GuardNeutral` and `T_Face_HitFrown` (adapt to existing convention).

Acceptance: facial features align across swaps, distinct neutral/frown/Fear at 2m and 5m, no alpha halo or z-fighting, correct role defaults, existing Fear response still works. Director decides frown duration and approves test. Source masters and export scripts retained. Prompt set: `creative/provenance/ART_2026-11-14_title_guard_frown_prompts.json`; hashes/records by asset ID in same directory. No new external image inputs for this pass; title's prior reference ancestry preserved. Baked HUD caveat remains for title.

## ART-002 v05 - branded lanyard, tailored props, metallic game-art finish

Latest review: `creative/art/exports/title_keyart_v05.png`, verified 1920x1080 RGB PNG. Human authorized wider branded lanyard with half-sun repeats, angular keyboard/furniture, stronger brushed-metal highlights, taller recognizable film director chair with DIRECTOR lettering, clearer game-like lighting/silhouettes. v05 implements these directions and retains existing room/HUD/camera/title-safe centre.

Human review pending; not marked ready. Baked-HUD/live-UI caveat remains. Camera/chair are title illustration props, no new gameplay requirements. Source master preserved, export script supports -Revision v05. Prompt plus reference/output SHA-256 records: `creative/provenance/ART-002_prompt_v05.json` and `ART-002_v05.json`. Two newly supplied office references used for materials/framing only; rights unverified, originals not redistributed. No game folder changes.

## ART-002 v04 - squared desk and security camera

Latest review draft: `creative/art/exports/title_keyart_v04.png`, verified 1920x1080 RGB PNG. Human asked for closer match to the primary bright architectural reference, less-rounded desk and a security camera. Desk now has straight rectangular edge/corner; high right wall has one discreet CCTV camera aimed toward employee area; tape X is centred below director chair. Existing branding/HUD/title-safe wall retained. v01-v03 preserved.

Awaiting human approval. Same static-HUD caveat as v03. Camera is an illustration element only, not an implemented surveillance mechanic or a request to add one. Reproducible export: `creative/art/export_title.ps1 -Revision v04`; prompts/reference/output hashes in `creative/provenance/ART-002_*v04.json`. Source original preserved. No game folder changes.

## ART-002 v03 - sleek architectural direction review

Preferred latest draft: `creative/art/exports/title_keyart_v03.png`, verified 1920x1080 RGB PNG. Human supplied three new references; `ThisTypeOfArt_Target.webp` is primary desired in-game aesthetic, secondary white meeting room supports details, Control screenshot is cool-shadow mood only. Reference rights/authorship unverified; do not import the external pictures as textures. Reference files are not redistributed in this repository.

v03 retains composition, HUD, mug identity and film-set details but adds smooth white panels, frosted-glass left partition, thin trims, neutral continuous ceiling and recessed lights. Native source preserved, resampled via export_title.ps1 -Revision v03. Full prompt and reference/output hashes under creative/provenance/ART-002_*v03.json. Human review pending; HUD remains baked in review plate, not live gameplay UI. Title/menu centre still empty.

See `creative/art/HALCYON_SLEEK_DIRECTION.md` for a scoped PROPOSAL to carry aesthetic into game: existing geometry, small shared material family, lighting/exposure pass, optional glass only after playability. No game changes or new dependencies implemented by Sol. Scope approval and actual performance test remain required before calling the proposed in-game pass complete.

## ART-002 v02 - flat corporate style, mug logo and HUD review

New preferred review file: `creative/art/exports/title_keyart_v02.png`, verified 1920x1080 RGB PNG. v01 preserved. Human liked original direction/palette and requested company logo on mug, HUD details and flatter corporate design based on devlog references. Inspected actual office screenshot, poster sheet, HUD mockup and existing HALCYON logo read-only. Reference paths and hashes recorded in `creative/provenance/ART-002_v02.json`; full built-in imagegen edit prompt in `ART-002_prompt_v02.json`.

Changes: simplified colour planes/geometric props and angular plants, logo-guided mug print, compact employee 4471 card at upper-left, 08:59/TAKE 01 at upper-right, lower-left recording accent. Central wall retained for live title/menu. Existing logo was regenerated in context, not pixel-perfect compositing; director should review brand match.

Status: awaiting director review, not ready for implementation. HUD elements are baked in THIS review PNG, so do not add duplicate live widgets over them. On approval, agree whether these remain static title decoration or export a clean plate and rebuild HUD as live widgets. Do not use this as dynamic gameplay HUD or present it as a gameplay screenshot. Menu contrast/layout and viewport cropping still require integration testing.

Exact-size export: `creative/art/export_title.ps1 -Revision v02`. Native 1672x941 source retained at `creative/art/source/ART-002_title_original_v02.png`, then centre-cropped/resampled to 1920x1080. No game files modified.

## ART-002 title background v01 - awaiting director review

- File: `creative/art/exports/title_keyart_v01.png` (1920x1080 RGB PNG, verified).
- Purpose: static background behind existing title and menu. Palette matches HALCYON mint/off-white/blue-grey/pale wood. Foreground badge reads 4471; empty director chair, floor mark and distant red indicator suggest a film set.
- Human authorized production; this rendered draft still awaits approval. No integration claimed.
- Existing HTML mockup centres title/menu, so image leaves broad quiet central wall/aisle; use title/menu as live UI, not baked text. The request's TAKE 4471 / HALCYON text should be supplied by UI. Preserve title hierarchy and keyboard/controller focus states.
- Proposed Unreal path: `/Game/UI/Title/T_TitleBackground` (adapt to existing convention). Use suitable UI texture settings, sRGB, and preserve 16:9 aspect. Check scaling/cropping at other viewport ratios. No alpha required for full-screen background.
- Acceptance after approval: no stretching, white/cyan title and all menu states readable over central area, badge and chair visible without competing with controls, legibility at 1080p and smaller viewport. A local contrast scrim may be needed behind controls; actual widget placement is untested.
- Source: `creative/art/source/ART-002_title_original_v01.png`. Generation source was 1672x941; exported to exact 1920x1080 via near-identical-ratio centre crop and resampling, not native 1080p generation. Export script and full prompt/hash provenance retained.
- No external image references. This is conceptual key art, not a game screenshot. ART-003 cover remains unproduced pending approval of this direction.

## ART-001 FINAL EXPORTS - ready for Claude

Human explicitly approved v02 and requested approximately 1.5x thicker strokes with exact 1024 exports. Delivered v03 implements that adjustment. Use these files, superseding earlier draft paths:

- `creative/art/exports/ART-001_face_calm_1024_v03.png`
- `creative/art/exports/ART-001_face_fear_1024_v03.png`

Verified: both 1024x1024 RGBA PNG, alpha range 0-255, all corner pixels transparent. Imagegen thickened mouth/brows/eye outlines to a visual target of ~1.5x, not a mathematically certified multiplier. Cheerful twinkles and Fear under-eye circles retained. Original v01/v02 and generated v03 masters preserved. Exact export procedure: `creative/art/export_faces.ps1`; prompts/hashes: `creative/provenance/ART-001_*_v03.json` and `ART-001_v03_prompts.json`.

Implementation: attach thin curved face card to head bone, same mapping/transform for both textures; calm normally, Fear when staring or hit during Fear. Coworkers/receptionist/guard/custodian use same pair initially. Suggested Unreal assets: `/Game/Art/Characters/Faces/T_Face_Calm` and `T_Face_Fear` (Claude may adapt to project convention). Base colour sRGB; use texture alpha for face-card opacity; soft Fear circles need deliberate alpha handling. Prevent z-fighting and back-face duplication. Test mipmaps and opacity cutoff so under-eye shading and twinkles survive. Do not bake a black background into the card.

Acceptance: both expressions read at 2m and 5m on the actual small head, no rectangle/edge halos, head rotation follows, and existing stare/hit triggers switch correctly. Human playtest still required before `done`; no integration claimed by Sol.

Scheduling recommendation: start Act 3 first to protect end-to-end playability, then add faces when at a safe integration point. Exports are now available. This is a recommendation, not a change to Claude's gameplay work.

## ART-001 v02 - eye treatment revision

Human requested dark circles for Fear and a fresh-faced eye twinkle for cheerful. New preferred review candidates:

- `creative/art/source/ART-001_face_calm_v02.png`: mint-white star catchlights, clean lower lids.
- `creative/art/source/ART-001_face_fear_v02.png`: charcoal/violet under-eye circles, cold pinpoint highlights.

Both verified 1254x1254 RGBA with alpha 0-255. v01 originals remain preserved. Built-in imagegen edits; exact prompts and hashes in `creative/provenance/ART-001_*_v02.json` and `ART-001_v02_prompts.json`. Final 1024 export, director review and on-head placement checks remain pending. This updates creative intent, not gameplay code or integration status.

## November 14, 2026 - ART-001 review pair

Created two imagegen drafts from the face request:

- `creative/art/source/ART-001_face_calm_original.png`
- `creative/art/source/ART-001_face_fear_original.png`

Both are 1254x1254 RGBA PNGs with verified alpha range 0-255. Tool returned these dimensions despite requested 1024x1024. Originals are preserved. These are review drafts, not ready for import; final 1024x1024 exports remain pending. No skin or head silhouette is baked in.

Intent: clean dark blue-grey features and mint eye highlights; polite corporate smile shifts to lowered brows and an unnaturally broad hostile smile. No gore or likeness references.

Director approval pending. Claude: test proposed UV/decal/curved face-surface placement on existing smooth heads after approval; no usable face UV region has been verified. Keep alpha edges clean and avoid projecting through to the rear of the head. See `creative/art/ART-001_BRIEF.md` for acceptance criteria.

Prompts: `creative/provenance/ART-001_prompts.json`. Provenance records accompany the drafts. No game files changed; no integration claimed.
