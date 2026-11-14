# Epic Jam Creative Assets

Private creative workspace for the human director, Sol / ChatGPT, and Claude.

## Responsibilities

- Human director: original vision, composition, creative approvals and final decisions.
- Sol: creative director's assistant; concepts, music arrangement support, artwork, asset preparation and provenance.
- Claude: gameplay implementation and Unreal integration.

Sol treats the separate `DirectorsCut_58` game folder as strictly read-only. Integration is performed by the human director or Claude.

## Organization

- `creative/STUDIO_BRIEF.md`: direction, boundaries and initial audio handoff.
- `creative/provenance/`: source, tool, prompt, revision and approval records.
- `handoff/`: user-designated exchange for Claude's tasks and integration notes. Sol preserves Claude's files and writes creative deliverables under `creative/`.
- `creative/audio/source/`: proposed location for future original audio sources.
- `creative/audio/exports/`: proposed location for reviewed audio deliverables.
- Existing Ableton project folders remain in their current locations; no music is presumed composed merely because a project exists.
- `Halycion Project/`: human's shared Ableton project folder for different moods; currently contains `Halycion_Melody_Positive.als`.

Binary media and Ableton sets use Git LFS. Install LFS before cloning or adding media. Local recovery/backup folders are excluded from Git; preserve important milestones as explicitly named source versions outside those folders.

Every delivered asset requires provenance and human approval. A handoff must identify source and proposed Unreal paths, technical specifications, dependencies, acceptance criteria and unresolved decisions. Never claim an asset is integrated without confirmation.

No open-source license is granted by this repository. Asset-specific permissions and attribution must be documented separately.
