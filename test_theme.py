import json
import re
import unittest
from pathlib import Path

import tinycss2


ROOT = Path(__file__).resolve().parent
CSS = (ROOT / "theme.css").read_text(encoding="utf-8")
MANIFEST = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))


def luminance(hex_color):
    channels = [int(hex_color[start:start + 2], 16) / 255 for start in (1, 3, 5)]
    linear = [
        value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4
        for value in channels
    ]
    return sum(value * weight for value, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(text, background):
    darker, lighter = sorted((luminance(text), luminance(background)))
    return (lighter + 0.05) / (darker + 0.05)


class ColorNotesTest(unittest.TestCase):
    def setUp(self):
        self.rules = {}
        for rule in tinycss2.parse_stylesheet(CSS, skip_comments=True, skip_whitespace=True):
            self.assertEqual(rule.type, "qualified-rule", "Expected an offline style rule")
            declarations = tinycss2.parse_declaration_list(
                rule.content, skip_comments=True, skip_whitespace=True
            )
            selector = tinycss2.serialize(rule.prelude).strip()
            values = self.rules.setdefault(selector, {})
            for declaration in declarations:
                self.assertEqual(declaration.type, "declaration", selector)
                values[declaration.name] = tinycss2.serialize(declaration.value).strip()

    def palette(self, mode):
        return self.rules["body"] | self.rules[f"body.theme-{mode}"]

    def color(self, palette, property_name):
        seen = {property_name}
        value = palette[property_name]
        while reference := re.fullmatch(r"var\((--[\w-]+)\)", value):
            name = reference[1]
            self.assertNotIn(name, seen, f"Circular color reference for {property_name}")
            seen.add(name)
            value = palette[name]
        self.assertRegex(value, r"^#[0-9a-fA-F]{6}$")
        return value

    def test_link_types_remain_distinct_and_readable(self):
        properties = ("--link-color", "--link-external-color", "--link-unresolved-color")
        for mode in ("light", "dark"):
            with self.subTest(mode=mode):
                palette = self.palette(mode)
                colors = {self.color(palette, name) for name in properties}
                self.assertEqual(len(colors), len(properties))
                self.assertEqual(palette["--link-unresolved-opacity"], "1")
                self.assertEqual(palette["--link-unresolved-filter"], "none")
                self.assertEqual(palette["--link-unresolved-decoration-style"], "dashed")
                unresolved = self.color(palette, "--link-unresolved-color")
                self.assertEqual(self.color(palette, "--link-unresolved-decoration-color"), unresolved)
                for background in ("--background-primary", "--background-secondary"):
                    for color in colors:
                        self.assertGreaterEqual(contrast(color, self.color(palette, background)), 4.5)

    def test_heading_size_and_emphasis_work_in_both_modes(self):
        for mode in ("light", "dark"):
            with self.subTest(mode=mode):
                palette = self.palette(mode)
                sizes = [float(palette[f"--h{level}-size"].removesuffix("em")) for level in range(1, 7)]
                self.assertTrue(all(upper > lower for upper, lower in zip(sizes, sizes[1:])))
                properties = [f"--h{level}-color" for level in range(1, 7)]
                properties += ["--bold-color", "--italic-color"]
                background = self.color(palette, "--background-primary")
                for name in properties:
                    self.assertGreaterEqual(contrast(self.color(palette, name), background), 4.5, name)
                self.assertNotEqual(self.color(palette, "--bold-color"), self.color(palette, "--italic-color"))

    def test_mobile_padding_preserves_space_inside_focus_outline(self):
        mobile_editor = ".is-mobile .markdown-source-view.mod-cm6 .cm-contentContainer > .cm-content"
        focus_rule = next(values for selector, values in self.rules.items()
                          if ".workspace-leaf-content :focus-visible" in selector)
        padding = int(self.rules[mobile_editor]["padding-inline"].removesuffix("px"))
        outline_offset = int(focus_rule["outline-offset"].removesuffix("px"))
        self.assertGreater(padding, abs(outline_offset))

    def test_version_and_documented_preview_files(self):
        version = MANIFEST["version"]
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertIn(f"/* {MANIFEST['name']} {version}. MIT. */", CSS)
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"Source version {version}.", readme)
        for path in ("screenshot.png", "screenshot-light.png"):
            self.assertIn(f"]({path})", readme)
            self.assertTrue((ROOT / path).is_file())
