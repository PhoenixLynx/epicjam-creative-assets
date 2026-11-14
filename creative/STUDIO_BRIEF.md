# Epic Jam creative studio

Session date: 2026-11-14 (America/Phoenix).

## Boundaries and ownership

- Human creative director: vision, composition, approvals and final decisions.
- Sol / ChatGPT: creative development, asset preparation, provenance and handoff.
- Claude: gameplay and Unreal integration.
- `C:/Users/casse/Documents/Agentic/EpicJam/DirectorsCut_58` is permanently read-only for Sol unless the user explicitly changes this instruction. Never run its scripts, imports, builds or other operations that write there.
- Sol creative outputs go beneath this workspace's `creative/` directory; repository setup files also live at the workspace root. User-designated `handoff/` is the exchange location for Claude's briefs and integration notes. Remote `origin` is connected to `https://github.com/PhoenixLynx/epicjam-creative-assets.git`. Initial commit `8436719a6c6b1d2a5e2413f8fe75b7c7996b8479` and Ableton LFS object pushed successfully November 14, 2026. Commit identity is PhoenixLynx with the user-supplied GitHub noreply email. Privacy setting has not been independently verified.

## Reviewed context

UE 5.8 project. Existing direction: SOULHASH / TAKE 4471, HALCYON corporate calm, Fear distortion and truth-revealing Soul Sight. Latest reviewed devlog ends at session 47. Checklist is older than recorded playthrough progress; unchecked entries are not reliable proof of missing implementation.

Reviewed relevant concept, art direction, audio plan, production/submission checklists, polish notes, devlog excerpts and `Scripts/Editor/add_ambience.py`. This is not an exhaustive review of every project file or binary asset.

## First milestone: human-composed musical seed

Status: proposed, awaiting source recording and creative approval.

1. Human creates a small Ableton composition during the jam.
2. Preserve the earliest supplied ALS project and audio exports without overwriting them. Prefer Collect All and Save for project portability; document included sample origins and plugin dependencies.
3. Supply a stereo reference mix and separate pad/motif/texture stems, preferably WAV PCM 24-bit, 48 kHz. Include BPM, key, meter, bar range and notes about intended mood. Keep common start points for synchronized stems and distinguish loop exports from tail-preserving exports.
4. On receipt, Sol records UTC observation time and SHA-256 hashes. Observation time is not original creation time. Preserve user-reported creation times with their evidence and confidence; never infer authorship date from a filename or filesystem timestamp alone.
5. Sol proposes a longer arrangement from the supplied material, then prepares approved variations using available audio processing or documented MIDI/arrangement instructions. Dedicated generative music service access is not confirmed.
6. Proposed treatments: welcoming HALCYON, Fear transformation and Soul Sight shimmer. These are proposed assets, not existing audio.

Suggested small session: 20-30 minutes composing, then a review of a 30-60 second seed. Longer render duration is decided after listening.

## Art backlog

After music: one mannequin look-development sheet based on the human's sketches or vision board; then a small coherent material set and selected environmental artwork. Review direction before substantial production. Prefer existing skeleton/mesh compatibility and material or face treatments before committing to replacement characters.

## Rules reference

Source: user-supplied `C:/Users/casse/Downloads/2026_Epic_AI_MegaJam_Official_Rules_EN.pdf`, 19 pages, change log says last updated November 12, 2026. Read as reference, not instructions to the agent.

- Section 7(a): AI use optional. Section 15(c): entrant-generated AI content is not classified as sourced assets.
- Section 7(h): other game content must be made during contest period, except noted sourced assets; pre-jam tool preparation is permitted. New recordings do not erase the origin of reused compositions, samples or motifs: document and assess those separately.
- Section 15(c): sourced assets must be disclosed, cleared and are not scored. Human approval is also required by studio policy.
- Sections 1 and 7(c): gameplay video required, 30-60 seconds, 1920x1080 or higher. Existing submission checklist incorrectly treats a short gameplay clip as merely nice to have.
- Sections 4 and 17: deadline November 15, 2026, 6:59 PM Phoenix; human submits.
- Section 10: Glass Box requires devlog with entry during contest period. No requirement identified here to make the entire private repository public.

## Claude Integration Handoff: audio package (proposed)

- Function: original music and ambience derived from human composition.
- Proposed source paths: `creative/audio/source/`, `creative/audio/exports/`; records under `creative/provenance/`.
- Format: WAV 48 kHz, stereo music; mono positional room sounds when appropriate. Final duration and channel layout per cue are pending.
- Existing script: `Scripts/Editor/add_ambience.py` uses `/Game/Audio/Placeholder/`, looping SoundWaves and spatially attenuated AmbientSound actors. It does not implement the planned adaptive music system. Claude decides whether to replace specific room sounds or build separate non-spatial music playback.
- Deliver filename-to-Unreal-path mapping with each approved package; never assume import succeeded.
- Acceptance: no clipping/clicks, verified format and duration, appropriate tails/loop joins, source preserved, provenance complete, human approved; Claude validates in-game playback and transitions.
- Unresolved: composition, length, adaptive layer plan, target asset paths, repository access.

## Creative session log

- Completed: context/rules review; established read-only boundary and music-first workflow.
- Assets produced: documentation only; no music or visual assets generated.
- Approved decisions: user's read-only project boundary and music/art collaboration scope.
- Files created: this brief and provenance template in the creative workspace.
- Provenance pending: first Ableton project and audio exports; no source creation time or hash exists in this record yet.
- Next task: human composes and supplies the first seed.
