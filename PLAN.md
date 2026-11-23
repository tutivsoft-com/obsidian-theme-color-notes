# Color Notes

An Obsidian theme with useful semantic colours and polished defaults.

This is the original design plan from 13 November 2026. The project has since shipped. See the [README](README.md) for current installation and testing instructions.

Search keywords: Obsidian theme, colourful headings, coloured links, bold, italics, no setup.

## Who this is for

People who want visual structure through colour without configuring extra plugins.

## User need and evidence

Users request different colours for headings, bold, italics and links, but report difficulty finding and configuring the right settings.

- [Requests for colourful text and simpler configuration](https://www.reddit.com/r/ObsidianMD/comments/1us4sr1/theme_wants/)

The Reddit thread records individual requests for these features. Other themes and snippets may already address some of these needs.

## Planned appearance and features

- Give heading levels, bold, italics, internal links and external links distinct coordinated treatments.
- Make default light and dark palettes useful immediately, without mandatory plugins or CSS snippets.
- Keep body prose calm and reserve stronger accents for meaningful structure.
- Keep unresolved links, callouts and task states clear and distinguishable.
- Preserve heading size and weight differences so colour is not the only cue.
- Offer only a small optional set of later customisation controls.

## Mode scope

Plan both light and dark modes.

## Original implementation and release plan

1. Confirm the final palette and layout against the requirements above.
2. Build the theme only after Rahul authorises implementation. Prefer supported Obsidian CSS variables and keep source readable.
3. Test representative notes, navigation, tabs, properties, menus, settings, search, Canvas and Bases where applicable. Include focus, selection, hover and error states.
4. Run the theme-specific checks below and record the actual Obsidian versions, devices and modes tested.
5. Prepare the root manifest, stylesheet, licence and real screenshots. Decide the first release version and minimum app version from actual testing.
6. Follow the current Obsidian submission guidance when a release is separately authorised. Commit source and screenshots, tag the intended revision, attach matching release assets and verify the published listing.

Keep assets offline, respect font and third-party licences, and avoid required plugins for the core appearance. Do not configure GitHub Actions or automatic deployment.

Official references used for planning

- [Build a theme](https://docs.obsidian.md/Themes/App%20themes/Build%20a%20theme)
- [Submit a theme](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme)
- [Developer policies](https://docs.obsidian.md/community-directory/developer-policies)

## Original acceptance checklist

- [ ] Verify each semantic text style in editing, Live Preview and Reading view.
- [ ] Check that many coloured elements on one page remain readable.
- [ ] Test without any community settings plugins installed.
- [ ] Confirm every claimed feature has been implemented and tested before replacing the planning-only status.
- [ ] Review screenshots for private information and verify all published documentation and asset paths.
- [ ] Verify the default branch, release revision and uploaded assets before calling any future release complete.
