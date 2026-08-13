"""Build the one-page CV from cv/CV.md.

Run from any directory with:
    python cv/build_cv.py

The builder deliberately supports only the small Markdown subset used by CV.md.
It uses ReportLab's invariant mode so identical sources and ReportLab versions
produce identical PDF bytes.
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from reportlab import rl_config

rl_config.invariant = 1

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    PageTemplate,
    Paragraph,
    Spacer,
)


ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = ROOT / "CV.md"
DEFAULT_OUTPUT = ROOT / "Chih-Kai-Wang-CV.pdf"

INK = colors.HexColor("#18202A")
MUTED = colors.HexColor("#4B5867")
ACCENT = colors.HexColor("#315C78")
RULE = colors.HexColor("#B7C5CF")
LINK = colors.HexColor("#245A7A")


def inline_markup(text: str) -> str:
    """Convert the controlled inline Markdown used by CV.md to ReportLab markup."""
    tokens: list[str] = []

    def stash(value: str) -> str:
        tokens.append(value)
        return f"@@TOKEN{len(tokens) - 1}@@"

    linked = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda match: stash(
            f'<link href="{html.escape(match.group(2), quote=True)}" '
            f'color="{LINK.hexval()}"><u>{html.escape(match.group(1))}</u></link>'
        ),
        text,
    )
    escaped = html.escape(linked)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"_(.+?)_", r"<i>\1</i>", escaped)
    for index, token in enumerate(tokens):
        escaped = escaped.replace(f"@@TOKEN{index}@@", token)
    return escaped


def styles() -> dict[str, ParagraphStyle]:
    return {
        "name": ParagraphStyle(
            "Name",
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=24,
            textColor=INK,
            alignment=TA_CENTER,
            spaceAfter=1.5 * mm,
        ),
        "tagline": ParagraphStyle(
            "Tagline",
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=12,
            textColor=ACCENT,
            alignment=TA_CENTER,
            spaceAfter=1.2 * mm,
        ),
        "contact": ParagraphStyle(
            "Contact",
            fontName="Helvetica",
            fontSize=8.9,
            leading=10.8,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceAfter=2.5 * mm,
        ),
        "section": ParagraphStyle(
            "Section",
            fontName="Helvetica-Bold",
            fontSize=9.2,
            leading=11,
            textColor=ACCENT,
            spaceBefore=1.8 * mm,
            spaceAfter=0.9 * mm,
            uppercase=True,
        ),
        "body": ParagraphStyle(
            "Body",
            fontName="Helvetica",
            fontSize=8.5,
            leading=10.3,
            textColor=INK,
            spaceAfter=1.2 * mm,
        ),
        "entry": ParagraphStyle(
            "Entry",
            fontName="Helvetica",
            fontSize=8.7,
            leading=10.4,
            textColor=INK,
            spaceBefore=0.6 * mm,
            spaceAfter=0.55 * mm,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            fontName="Helvetica",
            fontSize=8.25,
            leading=9.9,
            textColor=INK,
            leftIndent=3.3 * mm,
            firstLineIndent=-2.2 * mm,
            bulletIndent=0,
            spaceAfter=0.35 * mm,
        ),
        "footer": ParagraphStyle(
            "Footer",
            fontName="Helvetica-Oblique",
            fontSize=7.5,
            leading=9,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceBefore=1.5 * mm,
        ),
    }


def parse_markdown(source: str) -> list:
    cv_styles = styles()
    flowables: list = []
    lines = source.splitlines()
    index = 0

    while index < len(lines):
        raw = lines[index].strip()
        index += 1
        if not raw:
            continue
        if raw.startswith("# "):
            flowables.append(Paragraph(inline_markup(raw[2:]), cv_styles["name"]))
            continue
        if raw.startswith("## "):
            flowables.extend(
                [
                    Spacer(1, 0.35 * mm),
                    HRFlowable(width="100%", thickness=0.45, color=RULE, spaceBefore=0, spaceAfter=0),
                    Paragraph(inline_markup(raw[3:].upper()), cv_styles["section"]),
                ]
            )
            continue
        if raw.startswith("- "):
            flowables.append(
                Paragraph(inline_markup(raw[2:]), cv_styles["bullet"], bulletText="-")
            )
            continue
        if raw.startswith("_") and raw.endswith("_"):
            flowables.append(Paragraph(inline_markup(raw), cv_styles["footer"]))
            continue

        if len(flowables) == 1 and raw.startswith("**"):
            flowables.append(Paragraph(inline_markup(raw), cv_styles["tagline"]))
            continue
        if len(flowables) == 2 and ("mailto:" in raw or "GitHub" in raw):
            flowables.append(Paragraph(inline_markup(raw), cv_styles["contact"]))
            continue
        style = "entry" if raw.startswith("**") else "body"
        flowables.append(Paragraph(inline_markup(raw), cv_styles[style]))

    return flowables


class OnePageCV(BaseDocTemplate):
    def __init__(self, output: Path) -> None:
        super().__init__(
            str(output),
            pagesize=A4,
            leftMargin=15 * mm,
            rightMargin=15 * mm,
            topMargin=11.5 * mm,
            bottomMargin=10.5 * mm,
            title="Chih-Kai Wang - Curriculum Vitae",
            author="Chih-Kai Wang",
            subject="AI for Mathematics and verifiable reasoning",
            creator="cv/build_cv.py",
            pageCompression=1,
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="cv",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
            showBoundary=0,
        )
        self.addPageTemplates(PageTemplate(id="cv", frames=[frame]))

    def afterPage(self) -> None:
        if self.page > 1:
            raise RuntimeError("CV overflowed one page; shorten content or adjust spacing")


def build(source_path: Path, output_path: Path) -> None:
    source = source_path.read_text(encoding="utf-8")
    if any(character in source for character in ("\u2011", "\u2013", "\u2014")):
        raise ValueError("CV source must use ASCII hyphens only")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    document = OnePageCV(output_path)
    document.build(parse_markdown(source))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    build(args.source.resolve(), args.output.resolve())
    print(f"Wrote {args.output.resolve()}")


if __name__ == "__main__":
    main()
