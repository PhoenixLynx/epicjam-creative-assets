# Ending signs v01 — director review drafts

All paths relative to Music_Video_Assets. Purpose: replace ending/Act 3 placeholder signage using existing HALCYON palette. No game code or folder changes by Sol.

| Request | Export | Dimensions |
|---|---|---|
| ART-010 wrap banner | creative/art/exports/ART-010_wrap_banner_2048x512_v01.png | 2048x512 RGBA |
| ART-013 blank director card | creative/art/exports/ART-013_director_card_blank_1024x256_v01.png | 1024x256 RGBA |
| ART-013 revealed director card | creative/art/exports/ART-013_director_card_4471_1024x256_v01.png | 1024x256 RGBA |
| ART-016 overtime board | creative/art/exports/ART-016_overtime_menu_1024_v01.png | 1024x1024 RGBA |

Banner has transparent outer margin and flat artwork for a plane. Chair backs and menu are opaque. Name cards share identical geometry and text baseline for a stable swap. Card blank version reads DIRECTOR: without underscores; the number appears in the second texture. Canvas weave is subtle and procedural.

Board is a front-face texture for the existing frame/MI_LunchSpecials pipeline, not a new 3D frame; use an Act 3 material instance rather than replacing earlier lunch content globally. Text includes required coffee/cake and closing line. Additional proposed copy: HALCYON / CRAFT SERVICES; AFTER HOURS. SAME COMMITMENT.; PLEASE REMAIN AVAILABLE. Director may revise this copy.

Proposed Unreal names: T_WrapBanner, T_DirectorCard_Blank, T_DirectorCard_4471, T_OvertimeMenu, adapting to project conventions. Import as sRGB color textures; preserve alpha on banner. Keep readable from actual camera. Verify UV orientation/aspect ratios; original lunch art is portrait while requested overtime export is square, so test existing board UVs for stretching. Do not add a second border/mesh frame from the texture.

Acceptance: director selects drafts, exact copy legible at gameplay distance, no clipping/mirroring, card swap stable, menu applies only where intended, banner alpha clean. Unresolved: human visual/copy approval and actual material/UV tests. No import or integration claimed.

Editable source: creative/art/export_ending_signs_v01.ps1, drawing geometry and exact typography through System.Drawing. Uses installed Arial rendered to pixels; no font files redistributed. Full source/provenance: creative/provenance/ART_ending_signs_v01.json. Logo is a procedural redraw based on project mark, not pixel-identical.

Remaining requested artwork: ART-011 cake, ART-012 monitor dailies, ART-014 skyline, optional ART-015 soundstage. These have not been produced in this batch.
