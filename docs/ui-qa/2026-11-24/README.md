# Color Notes Windows UI check

Tested on 24 November 2026 in Obsidian 1.15.1 for Windows. The isolated vault used synthetic notes, the native Canvas and Bases features, and zero community plugins. The starting theme was 3.4.1 at commit `001bb8029a01c814819bd88e882dd8ab34e1ba9c`. The retest used source version 3.4.2.

## Fixed defect

External links used a dotted underline in Reading view and a solid underline in Live Preview. The URL token in Source mode also used a solid underline. Both editor views now retain the dotted cue for external links, including the URL token when the markup is visible.

| Palette | Resolved note | Unresolved note | External link |
| --- | --- | --- | --- |
| Dark | Blue `#aecfff`, solid | Orange `#ffb48f`, dashed | Green `#99e6b8`, dotted |
| Light | Blue `#2447a0`, solid | Orange `#923d17`, dashed | Green `#126047`, dotted |

The colors and underline styles were read from the visible elements in Obsidian. The first two link columns apply to Reading view and Live Preview. The Source mode retest checked the green, dotted URL token and visible Markdown syntax. Five source tests passed with `python -B -m unittest -v`.

## UI cases

| Case | Verified result | Capture |
| --- | --- | --- |
| Dark Reading view | Six descending heading sizes and weights, distinct emphasis and link cues, rendered callout, task and table. | [Dark Reading](screenshots/01-dark-reading.webp) |
| Dark Live Preview | Distinct link cues and emphasis with the editor active. The callout, checkbox and table remained visible. | [Dark Live Preview](screenshots/02-dark-live-preview.webp) |
| Dark Source mode | Raw wiki-link syntax and a dotted external URL token in the editor. | [Dark Source](screenshots/03-dark-source.webp) |
| Light Reading view | The light palette retained the heading hierarchy, emphasis and all three link cues. | [Light Reading](screenshots/04-light-reading.webp) |
| Light Live Preview | The three link cues, emphasis colors, callout and checkbox matched the light palette. | |
| Light Source mode | Raw wiki-link syntax and a green, dotted external URL token. | |
| Appearance | Selected Dark and Light. Switched to Default and reselected Color Notes, which restored the light note background from `#ffffff` to `#fffafc`. | [Appearance](screenshots/05-appearance.webp) |
| Search | Verified the empty result state and a matching note. Clicking a result opened Field colors from Heading map. | [Search and Outline](screenshots/06-search.webp) |
| Quick Switcher | Typed Heading map and used Enter to open the matched note. | [Quick Switcher](screenshots/07-quick-switcher.webp) |
| Canvas | Zoom to fit showed three cards with two connectors, rendered note previews and readable controls. | [Canvas](screenshots/08-canvas.webp) |
| Bases | Opened the Study notes table with four rows, filename links, topics and reviewed values. | [Bases](screenshots/09-bases.webp) |
| Note checklist | Toggled the first task, verified the saved Markdown and restored the unchecked state. | |
| Note property | Toggled the reviewed field, verified its saved Boolean value and restored it. | [Checked property](screenshots/10-checked-property.webp) |
| Link navigation | Hovered the unresolved link and checked its destination label and dashed underline. Followed the resolved note link to Heading map. | |
| Command Palette and Outline | Ran the Outline command and checked the six headings in the outline. | |
| Tabs | Opened Study lab in a new tab and switched back to Field colors. | |

## Reproduce

1. Copy the files from [fixture](fixture/) into a disposable vault. Install this repository's `manifest.json` and `theme.css` in `.obsidian/themes/Color Notes/`.
2. In **Settings > Appearance**, select **Color Notes** and **Dark**. Open **Field colors**. Compare its three link cues in Reading view and Live Preview, then check the URL token in Source mode.
3. Select **Light** and repeat. Open **Heading map** through the resolved link. The external anchor points at the reserved example domain.
4. Search for `Visibility check` and a unique string absent from the vault. Open **Lesson board** and **Study index** for the Canvas and Bases cases.

## Scope

The ten WebP captures are from the live Windows app. The main viewport was 1024 by 800 pixels and Settings was 900 by 700. Other operating systems and mobile hardware were outside this run. The external URL was verified in the note.
