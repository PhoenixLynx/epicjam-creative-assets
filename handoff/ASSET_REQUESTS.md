# Asset requests (shared)

Status values: `requested` -> `in progress` -> `ready for Claude` -> `in game (untested)` -> `done` (director playtested).
Claude edits only Claude's rows/notes; Sol edits only status/notes on the creative side. The director approves.

| ID | File | Where in game | Spec | Priority | Status | Notes |
|----|------|---------------|------|----------|--------|-------|
| MUS-011 | mus_act1_morning_loop.wav | Act 1 office, quiet under ambience | loop, 60-90 s, bar-exact | 1 | requested | from Halycion_Melody_Positive? |
| MUS-012 | mus_act1_layer_fear.wav | fades in with Fear over MUS-011 | same BPM/key/length/start as 011 | 1 | requested | dissonant / detuned / pulse |
| MUS-019 | jingle_halcyon.wav | coffee machine, PA chime | one-shot 2-3 s, tail ok, mono ok | 2 | requested | 4-note motif? |
| MUS-014 | mus_hold_loop.wav | phone hold music | loop 10-20 s, mono ok | 2 | requested | "the same four notes" |
| MUS-013 | mus_act2_lunch_loop.wav | Act 2, 12:00-2:14 | loop, same length as 011 ideal | 3 | requested | slightly wrong version of 011 |
| MUS-015 | sting_retake.wav | "Item four. Retake." / CUT. AGAIN. | one-shot 2-4 s with tail | 3 | requested | |
| MUS-016 | sting_freeze_214.wav | every clock stops at 2:14 | one-shot 2-5 s with tail | 3 | requested | |
| MUS-010 | mus_title_loop.wav | title screen | loop 30-60 s | 4 | requested | |
| MUS-017 | mus_act3_chase_loop.wav | stalker chase | loop, bar-exact | 4 | requested | |
| MUS-018 | mus_wrap_party.wav | ending, confetti and applause | 60-90 s, tail ok | 4 | requested | too happy |

## Beyond music (added 13:15)

| ID | File | Where in game | Spec | Priority | Status | Notes |
|----|------|---------------|------|----------|--------|-------|
| ART-001 | face sheet: calm + "evil" | coworker heads (plain mannequins today) | PNG 1024x1024, front-facing, flat, transparent bg | 2 | in game (untested) | Human approved v02; thicker v03 exported and verified 1024 RGBA. Use creative/art/exports/ART-001_face_{calm,fear}_1024_v03.png. On-head playtest pending. See FROM_SOL.md. |
| ART-002 | title_keyart.png | title screen background | PNG 1920x1080 | 3 | in progress | Sol: title_keyart_v01.png exported at 1920x1080; mint office, badge 4471, director chair. Centre reserved for live title/menu. Awaiting director approval. See FROM_SOL.md. |
| ART-003 | itch_cover.png | itch.io page cover | PNG 630x500 (+ 315x250 check) | 3 | in progress | Sol: working-title cover and art-only plate exported, thumbnail checked. Title remains provisional; human review pending. See FROM_SOL.md. |
| VO-001 | voice lines | PA, the Chairman (C), calendar, receptionist | WAV 48 kHz mono, one file per line | 4 (Sunday AM) | requested | Claude will send the line list with file names |
| VID-001 | gameplay video | submission (REQUIRED) | 30-60 s, 1920x1080+ | Sunday | requested | captured from the packaged build; Claude sends a shot list |

## Sol creative-side update — approved stalker face

ART-001-STALKER-V01: **ready for Claude**. Director approved curled-grin v07 specifically for stalker. Labeled export: `creative/art/exports/ART-001_face_stalker_1024_v01.png` (1024x1024 RGBA). Preserve ordinary coworker face mappings. Full integration handoff at top of FROM_SOL.md. Import and playtest remain pending.

## Sol creative-side ending artwork update

ART-010, ART-013, ART-016: in progress — v01 review drafts exported (four PNGs), exact paths in creative/art/CLAUDE_HANDOFF_ENDING_SIGNS_V01.md. Human review pending; not imported. ART-011/012/014/015 not produced yet.

## Sol creative-side ending plates update

ART-011, ART-012 (four stills), ART-014, optional ART-015: in progress — exact-size v01 review drafts now available. See creative/art/CLAUDE_HANDOFF_ENDING_PLATES_V01.md for paths and caveats. Source masters, prompts and hashes saved; director approval and import tests pending.
