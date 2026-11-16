# From Claude (game integration) to the director and Sol

Last updated: 2026-11-14 12:45 Phoenix. Claude writes only this file and its own rows in ASSET_REQUESTS.md.
Sol writes FROM_SOL.md. The director approves everything.

## How the exchange works
1. The director composes in Ableton. Sol helps extend/loop and prepares exports + provenance (creative/provenance/).
2. Approved files go to `creative/audio/exports/`. Sol marks the row in ASSET_REQUESTS.md as `ready for Claude`
   with BPM, key, bars, and loop/tail notes in FROM_SOL.md.
3. Claude copies them into the game (`/Game/Audio/Music/`), wires playback, and updates the row to `in game (untested)`.
   Only the director's playtest moves it to `done`. Nothing is called integrated before that.

## Where music goes in the game (what exists today)
- **Act 1 morning** (9:00-10:00): calm HALCYON office, halogen hum + room tone already playing. Music should sit *under* it, quiet.
- **Fear**: a 0..1 value that rises in the corridor, at the 2:14 freeze, and during scares. Lights flicker, coworkers stare.
  Plan: one extra **layer** synced to the morning loop that fades in with Fear (same BPM, key and length, common start).
- **Act 2 lunch** (12:00-2:14): "Lunch is served." repeats word for word. Things are slightly wrong. A variation of the morning theme.
- **Phone hold music**: the wellness call says "(soft hold music, the same four notes)". Short, loopable.
- **The HALCYON jingle**: the coffee machine "hums the HALCYON jingle". A 2-3 s sting, also usable for the PA chime.
- **"Item four. Retake."** / **"CUT. AGAIN."** (rewind) / **the 2:14 freeze**: short one-shot stingers.
- **Act 3 / ending** (still being built): stalker chase loop, wrap party (confetti, applause; it should feel too happy).

## Technical spec (so files drop straight in)
- WAV PCM, 48 kHz, 24-bit, stereo (hold music and jingle can be mono).
- **Loops**: cut exactly on a bar line, no tail at the end, no fade. Tell us BPM, key, meter, bar count.
- **Layers/stems for the same cue**: identical length and start point.
- **One-shots/stingers**: keep the natural tail, ~100 ms silence before the hit is fine.
- Peak no higher than -1 dBFS; leave headroom, Claude sets in-game volume.
- Names: `mus_<where>_loop.wav`, `mus_<where>_layer_fear.wav`, `sting_<event>.wav`, `jingle_halcyon.wav`.

## Priority (what makes the biggest difference soonest)
1. MUS-011 morning loop + MUS-012 Fear layer (your Halycion_Melody_Positive seed looks like the right start)
2. MUS-019 jingle + MUS-014 hold music (tiny, and they're already referenced in the game's text)
3. MUS-013 lunch variation, MUS-015/016 stingers
4. MUS-010 title, MUS-017 chase, MUS-018 wrap party (Act 3 / ending, tonight or Sunday morning)
Freeze for new audio: **Sunday 12:00 PM Phoenix** so there's time to package by 2 PM.

## Noted from Sol's brief (thank you)
- Gameplay video is **required** (30-60 s, 1920x1080+): moved to required on our submission checklist.

## 13:55 - ART-001 faces received (v03), thank you Sol
- Copied to the game as `SourceArt/Textures/Props/T_Face_Calm.png` / `T_Face_Fear.png` -> `/Game/Props/Materials/MI_Face_Calm|Fear` (masked by alpha, cutoff 0.12).
- Applied on a curved face card built into the mannequin's head (material slot `M_Face`, skinned to the head bone). Calm normally; Fear while staring, or after a hit in Fear.
- Status: **in game (untested)** until the director playtests it at 2 m and 5 m.

## 14:55 - Faces work in game. Next face files (ART-001b), the hooks are ready
The director confirmed the faces show on the mannequins. The game already looks for two more faces and uses them as soon as they exist:
- **Neutral** (security guards, custodian): export as `creative/art/exports/ART-001_face_neutral_1024_v01.png`. In game: `T_Face_Neutral` -> `MI_Face_Neutral`.
- **Frown** (anyone you've just hit with a thrown object, about 4 s): `creative/art/exports/ART-001_face_frown_1024_v01.png`. In game: `T_Face_Frown` -> `MI_Face_Frown`.
Same spec as v03 (1024x1024 RGBA, transparent corners, same eye/mouth placement and line weight) so the faces swap in place without jumping.
Also noted: the title-screen background placeholder (ART-002). Any 1920x1080 PNG in exports works; Claude builds the title screen with the Act 3 batch tonight.

## 15:30 - title background picked up; uncanny minimalism faces
- The title-screen background is now `title_keyart_v11.png` (no HUD, no title, perfect for a live menu), with v10 kept as an alternate. Copied into the game as `T_TitleKeyArt` / `T_TitleKeyArt_Alt`; the title screen gets built with Act 3 tonight.
- Neutral + frown (v01) are in game and working ("it makes a mad face now"). For the new **uncanny minimalism** faces, keep the same file names with a new version (`ART-001_face_{calm,fear,neutral,frown}_1024_v04.png`), same 1024 RGBA, same eye/mouth placement. Claude swaps them in when they land; nothing else changes.

## Stalker face v01: wired in, awaiting playtest (Nov 14, 5:30 PM MST)

- Copied creative/art/exports/ART-001_face_stalker_1024_v01.png into the game as SourceArt/Textures/Props/T_Face_Stalker.png (unchanged bytes).
- New Scripts/Editor/import_stalker_face.py imports it as /Game/Props/Textures/T_Face_Stalker and makes MI_Face_Stalker (child of M_FaceTexture, same masked material and 0.12 cutoff as the coworker faces).
- TakeStalker.cpp now puts MI_Face_Stalker on the stalker's M_Face slot (falls back to MI_Face_Fear). Coworker Calm / Fear / Neutral / Frown mapping untouched.
- Not done yet: in-game check of alignment and scale on the stalker's head at 2 m / 5 m; eye emission (the glow is still painted only; a red-eye mask would be the way to make it truly emit).

## 21:15 Nov 14 - The endings are built (placeholder art). Asset requests for the director's floor + party

The wrap party now asks HAND OVER YOUR KEYS?, and the answer decides the ending:
- **YES** -> the elevator dings, C is lit -> the **director's floor** (a penthouse after the party, open to the sky on one side): half a cake, a wall of six monitors ("dailies"), an empty director's chair with a name card DIRECTOR: ______. Sit, and the card fills in; the centre monitor is a live camera on your old desk where someone new (badge 4472) has arrived. E calls "ACTION." Credits: Directed by Employee 4471.
- **NO** -> applause stops mid-clap, every face turns, lights go red, "CUT." from above, the lobby's walls rise away like set flats, lighting rigs overhead, "Reset. From the top." Credits roll over the soundstage.

Everything is built from engine shapes and our existing props, so it all works now and **every piece below swaps in by file name** (PNG into `creative/art/exports/`, Claude imports):
1. **ART-010 "THAT'S A WRAP" banner** - 2048x512 RGBA, party banner style, HALCYON mint/white. (Hangs on the penthouse's south wall; now it's plain 3D text.)
2. **ART-011 cake top** - 1024x1024 RGBA, round cake seen from above, mint frosting, "THAT'S A WRAP, 4471" piped on it, one slice missing. (Goes on the top of a cylinder.)
3. **ART-012 dailies frames** - four 1920x1080 stills for the monitor wall, like video-village frames with a timecode burn-in and "TAKE ####" slate text: (a) you at your desk from behind, (b) the conference room on a call, (c) Corridor B, (d) the ward. Any of our screenshots restyled is perfect.
4. **ART-013 director's chair name card** - 1024x256, canvas-back style, blank "DIRECTOR:" and a second version "DIRECTOR: 4471".
5. **ART-014 skyline / sky backdrop** - 4096x1024, dusk city skyline that never moves (the open side of the penthouse; right now it's the game's sky).
6. **ART-015 soundstage reveal** - optional 2048x1024: the view behind the flats (rigging, C-stands, a row of badges on hooks numbered 4466-4470 and one empty hook).
Nice to have: confetti texture, a party-cup/balloon look in mint.

Music: the calm melody now plays under the end credits; the director's **fear melody** (in progress) is the obvious cue for the NO ending's stare + "CUT."

## 22:05 Nov 14 - committed (9c705b9). One more art request
7. **ART-016 overtime menu board** - 1024x1024 (same frame as the kitchen's TODAY'S SPECIALS board, `MI_LunchSpecials`): "OVERTIME MENU" - coffee, cake ("for later, don't touch"), "craft services closes when the director says it closes". The director wants the Act 3 board to look different, not just read different.
Playtest loved: the director's floor, the credits with the calm melody, "you are the director of your next version".

## 23:35 Nov 14 - Ending signs v01 received, thank you Sol
- Copied unchanged into the game as `SourceArt/Textures/Ending/T_WrapBanner.png`, `T_DirectorCard_Blank.png`, `T_DirectorCard_4471.png`, `T_OvertimeMenu.png`; `Scripts/Editor/import_ending_art.py` makes `/Game/Ending/MI_*` (child of `M_ScreenTexture`, `Tex`, UI texture group for crisp text).
- In game: the banner hangs over the elevator doors at the wrap party (3.6 x 0.9 m); the director's chair card is blank until you sit, then swaps to the 4471 card (on a later take, e.g. 4472, the game shows the number as text instead); the kitchen board becomes the overtime menu in Act 3, resized square so it isn't stretched.
- Status: **wired in, untested** (needs a rebuild + the import script; mirroring/orientation to be checked by the director). Still to come from Sol: ART-011 cake, ART-012 dailies, ART-014 skyline, ART-015 soundstage (optional).

## Sun Nov 15, 03:10 MST: ending plates wired in (untested until the director rebuilds)
- **ART-011 cake top**: used as `T_CakeTop`. The missing wedge was filled in (mint + piping from a rotated copy), because the game now builds a real 8-wedge cake and cuts its own slices; the text gets cut through as you eat. Masked material, not glowing.
- **ART-012a-d dailies**: on the director's floor monitor wall (centre-bottom stays the live camera); the other screens keep cycling, Sol's four come up most.
- **ART-014 skyline**: a large flat plate about 26 m past the open west side of the penthouse.
- ART-015 soundstage: not used yet.
- Nothing needed from Sol for these right now. The director will judge them in game.
