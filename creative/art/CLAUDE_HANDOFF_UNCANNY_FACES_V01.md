# Claude Integration Handoff — uncanny minimalist faces v01

Status: generated/exported for director review and in-game comparison; not yet approved as final or integrated. Prior files remain intact. Do not auto-replace the old filename hooks without selecting this set.

All paths below are relative to Music_Video_Assets. Each is a 1024x1024 RGBA PNG with transparent corners and facial marks only.

| Expression/function | Export | Existing destination |
|---|---|---|
| Calm / practiced cheerful default | creative/art/exports/ART-001_face_calm_1024_uncanny_v01.png | T_Face_Calm / MI_Face_Calm |
| Fear stare / hit during Fear | creative/art/exports/ART-001_face_fear_1024_uncanny_v01.png | T_Face_Fear / MI_Face_Fear |
| Neutral guards / custodian | creative/art/exports/ART-001_face_neutral_1024_uncanny_v01.png | T_Face_Neutral / MI_Face_Neutral |
| Thrown-object hit frown | creative/art/exports/ART-001_face_frown_1024_uncanny_v01.png | T_Face_Frown / MI_Face_Frown |

Use existing curved head-bone face card, M_Face slot and masked alpha material (reported cutoff 0.12). Keep existing ~4-second frown duration and Fear precedence. No gameplay changes requested. New filenames are deliberate: existing old hooks still point to old assets until Claude explicitly selects these.

Art direction: uncanny minimalism, narrow half-lidded eyes, restrained mouth, small highlights instead of stars, no nose; Fear retains grey-violet under-eye circles. Calm is deliberately restrained rather than exuberant.

Acceptance: director approves style on head; all four align during swaps without noticeable jumping; expressions readable at 2m and 5m; no edge halos; Fear circles survive alpha masking; correct role defaults and existing reaction priority preserved. The generated variants have approximate matching anchors, NOT guaranteed pixel-registered features. Check actual mesh before final import approval.

Sources: creative/art/source/ART-001_face_{calm,fear,neutral,frown}_uncanny_v01.png. Re-export with export_faces.ps1 -Variants calm,fear,neutral,frown -Revision uncanny_v01. Full prompts and SHA-256 records in creative/provenance/ART-001_uncanny_v01*.json. Built-in image_gen used; no new external reference imagery. Original creation times unknown; record UTC is observation time. Commit hashes pending.

Unresolved: human final selection, on-head UV/scale fit and distance readability. Sol made no game-folder changes.
