# HALCYON sleek architecture - proposed in-game direction

Human preference, November 14, 2026: primary target is supplied `ThisTypeOfArt_Target.webp`; Control screenshot is mood support, not a request to reproduce that game. Image rights/authorship are unverified and references must not be used as game textures. Existing gameplay layout and prior approvals remain intact.

## Define

HALCYON should feel expensive, calm and rehearsed: smooth off-white planes, thin reveals, restrained mint accents and soft daylight. Reserve flat corporate illustration for posters, icons and HUD; give the room restrained three-dimensional material/light cues. Fear corrupts this same coherent space rather than requiring another environment build.

## Small feasible pass for Claude (proposal, not implementation authorization)

1. Reuse existing geometry and layout. Create or tune a small shared material family: matte off-white, mint ceramic/plastic, blue-grey carpet, pale wood and satin metal. Starting roughness suggestions only: matte surfaces ~0.6-0.85; satin plastic ~0.35-0.55; metal ~0.25-0.45. Check under actual game lighting before choosing values.
2. Reduce noisy surface patterns. Use restrained texture scale and broad value differences. Keep accent mint on selected panels, badge hardware and mugs, not every surface.
3. Tune existing light/exposure to soft neutral daylight with cool shadow depth. Preserve object readability and the existing Fear blend. Do not add many new shadow-casting lights solely to match generated art.
4. If there is time after end-to-end playability: one reusable glass partition with simple frosted band, and slim white/silver trims. Glass/translucency can cost performance and sorting time; an opaque frosted material is a feasible fallback.

Do not rebuild the office, replace characters, change collisions, add imported reference furniture or introduce a new rendering dependency for this pass. Existing corporate poster art and face textures remain valid.

## Handoff and acceptance

- Proposed deliverable: a focused material/lighting pass, not additional room geometry requirements.
- Reference deliverable: `creative/art/exports/title_keyart_v03.png` is a conceptual title image, not a screenshot or promise of current in-game fidelity.
- Dependencies: Claude's existing material slots, Fear parameter system and current lighting; names/compatibility to be checked by Claude.
- Acceptance: same playable paths and interactions; calm state reads pleasant and clean; Fear state still transforms; objects remain legible; compare frame time before/after on target machine. No exact performance gain is asserted.
- Status: proposed; director approves scope before changes. Sol does not edit the game folder.
