# CV source and build

`CV.md` is the editable source for the one-page English CV. The committed PDF is generated with a pinned ReportLab version and invariant PDF metadata.

From the repository root:

```console
python -m pip install -r cv/requirements.txt
python cv/build_cv.py
```

The builder writes `cv/Chih-Kai-Wang-CV.pdf` and fails if the content overflows one page. External links are embedded in the PDF. Copy the result to `public/Chih-Kai-Wang-CV.pdf` in the portfolio repository and compare SHA-256 hashes.

## Source grammar

`CV.md` accepts only the constructs below; anything else (other heading levels, `*` or numbered lists, tables, code fences) fails the build instead of rendering as body text.

| Source | Renders as |
| --- | --- |
| `# Name` | Name in the masthead |
| `> Target` | Accent line under the name |
| `a \| b \| c` (first line after the name) | Contact block, one item per line |
| Plain paragraph before the first `##` | Lede across the full width |
| `## Highlights` with `- value \| label` | Figure strip; one cell per item |
| `## Title` | Section with the title in the left column |
| `### Title \| meta` | Entry heading; `meta` is right-aligned in the accent colour |
| Plain line directly after `###` | Stack line; set beside the title when it fits, otherwise below it |
| `- text` / `- text \| date` | Bullet, optionally with a right-aligned date |
| `- **Term**: text` (no link in the term) | Two-column term row |
| `_text_` | Footer at the bottom of the page |

Inline: `**bold**`, `[label](url)` and word-bounded `_italic_`. Identifiers such as `HCI004_ZERO_TESTS` are left alone.

The PDF uses the built-in Helvetica, so the source must stay within cp1252 and use ASCII hyphens only (no U+2011, U+2013 or U+2014); the builder rejects anything else.
