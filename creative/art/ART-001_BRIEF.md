# ART-001 mannequin faces - review draft

UPDATE: v02 approved by director. v03 thick-stroke 1024x1024 RGBA exports are ready for Claude under `creative/art/exports/`; see latest `handoff/FROM_SOL.md`. Earlier draft limitations below are retained as revision history, not current export status. In-game mapping/readability test remains pending.

Date: November 14, 2026. Human director requested generation from handoff specs.

Purpose: give HALCYON coworkers an overly rehearsed polite expression, paired with a hostile Fear expression. Tone remains stylized corporate horror, teen-appropriate.

Source: `handoff/ASSET_REQUESTS.md`, ART-001: front-facing flat PNG, 1024x1024, transparent background; calm HALCYON smile and Fear variant when hit or staring.

Production choice: two separate matching facial-feature textures rather than baking a head silhouette into either texture. Transparent margins should permit placement on the existing smooth mannequin heads. No human likeness reference is used.

Status: review drafts created; no human approval or integration claimed. Actual original images are 1254x1254 RGBA with real transparency, despite the 1024x1024 prompt. Final spec exports remain pending. Title art ART-002 and cover ART-003 remain requested, not produced in this pass.

## Claude Integration Handoff

- Feature: ART-001 calm/Fear face pair.
- Proposed paths: `creative/art/exports/ART-001_face_calm_v01.png` and `creative/art/exports/ART-001_face_fear_v01.png`.
- Required spec: RGBA PNG, 1024x1024, front-facing flat features, transparent background.
- Dependency: existing mannequin mesh and face placement/material implementation. The generator script describes a featureless spherical head; a usable face UV region or decal placement has not been verified.
- Implementation: preserve the existing mesh/skeleton. Test alpha-masked material on a small curved face surface, or a suitable decal/material mapping. Avoid projecting through to the back of the head. Use the existing Fear/hit logic; no new gameplay feature is requested.
- Acceptance: human approves both looks; features align between states; no background rectangle or alpha halo; readable at gameplay distance; no stretching or rear-head duplication; original source and prompts preserved.
- Unresolved: human look approval, exact UV/decal placement, generated file dimensions/alpha validation. Generated drafts must not be marked ready for Claude until reviewed.
