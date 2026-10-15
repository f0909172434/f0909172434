"""Build the one-page CV from cv/CV.md.

Run from any directory with:
    python cv/build_cv.py

CV.md uses a small, fixed Markdown grammar (see cv/README.md). Anything outside
that grammar is rejected rather than silently rendered as body text. ReportLab's
invariant mode makes identical sources and ReportLab versions produce identical
PDF bytes.
"""

from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass, field
from pathlib import Path

from reportlab import rl_config

rl_config.invariant = 1

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = ROOT / "CV.md"
DEFAULT_OUTPUT = ROOT / "Chih-Kai-Wang-CV.pdf"

INK = colors.HexColor("#16191D")
MUTED = colors.HexColor("#5B636C")
FAINT = colors.HexColor("#8B929A")
RULE = colors.HexColor("#D2D6DA")
WASH = colors.HexColor("#F4F1EC")
ACCENT = colors.HexColor("#B4441F")

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_X = 17 * mm
MARGIN_TOP = 15 * mm
MARGIN_BOTTOM = 15 * mm
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN_X
LABEL_WIDTH = 29 * mm
GUTTER = 5 * mm
BODY_WIDTH = CONTENT_WIDTH - LABEL_WIDTH - GUTTER
META_WIDTH = 50 * mm
DATE_WIDTH = 20 * mm
STACK_GAP = 2.6 * mm
TERM_WIDTH = 20 * mm
CONTACT_WIDTH = 62 * mm

HIGHLIGHTS = "Highlights"


# ---------------------------------------------------------------- source model


@dataclass
class Block:
    """One renderable unit inside a section."""

    kind: str  # "entry", "sub", "body", "bullet", "term"
    text: str
    right: str = ""
    term: str = ""


@dataclass
class Section:
    title: str
    blocks: list[Block] = field(default_factory=list)


@dataclass
class CV:
    name: str = ""
    target: str = ""
    contact: list[str] = field(default_factory=list)
    lede: list[str] = field(default_factory=list)
    sections: list[Section] = field(default_factory=list)
    footer: str = ""


def split_right(text: str) -> tuple[str, str]:
    """Split 'left | right' on the last separator; right is optional."""
    if " | " not in text:
        return text, ""
    left, right = text.rsplit(" | ", 1)
    return left.strip(), right.strip()


def parse(source: str) -> CV:
    cv = CV()
    section: Section | None = None
    previous = ""

    for number, line in enumerate(source.splitlines(), start=1):
        raw = line.strip()
        if not raw:
            continue

        def fail(reason: str) -> None:
            raise ValueError(f"CV.md line {number}: {reason}: {raw!r}")

        if raw.startswith("# "):
            if cv.name:
                fail("only one '# ' name heading is allowed")
            cv.name = raw[2:].strip()
            kind = "name"
        elif raw.startswith("> "):
            if cv.target or section is not None:
                fail("a single '> ' target line is allowed, directly under the name")
            cv.target = raw[2:].strip()
            kind = "target"
        elif raw.startswith("## "):
            section = Section(raw[3:].strip())
            cv.sections.append(section)
            kind = "section"
        elif raw.startswith("### "):
            if section is None:
                fail("'### ' entries must sit inside a '## ' section")
            title, right = split_right(raw[4:].strip())
            section.blocks.append(Block("entry", title, right))
            kind = "entry"
        elif raw.startswith("- "):
            item = raw[2:].strip()
            if section is None:
                fail("bullets must sit inside a '## ' section")
            term = re.fullmatch(r"\*\*([^\[\]*]+)\*\*:\s*(.+)", item)
            if section.title == HIGHLIGHTS:
                value, label = split_right(item)
                if not label:
                    fail("highlights need the form '- value | label'")
                section.blocks.append(Block("bullet", label, value))
            elif term:
                section.blocks.append(Block("term", term.group(2), term=term.group(1)))
            else:
                text, right = split_right(item)
                section.blocks.append(Block("bullet", text, right))
            kind = "bullet"
        elif raw.startswith("_") and raw.endswith("_") and len(raw) > 2:
            cv.footer = raw[1:-1].strip()
            kind = "footer"
        elif re.match(r"(#{4,}|[*+] |\d+\. |\||```|>)", raw):
            fail("unsupported Markdown construct")
        elif section is None:
            if not cv.contact and previous in ("name", "target") and " | " in raw:
                cv.contact = [part.strip() for part in raw.split(" | ")]
                kind = "contact"
            else:
                cv.lede.append(raw)
                kind = "lede"
        else:
            kind = "sub" if previous == "entry" else "body"
            section.blocks.append(Block(kind, raw))
        previous = kind

    if not cv.name:
        raise ValueError("CV.md needs a '# ' name heading")
    return cv


# ---------------------------------------------------------------- typography


def inline_markup(text: str) -> str:
    """Convert the controlled inline Markdown used by CV.md to ReportLab markup."""
    tokens: list[str] = []

    def stash(value: str) -> str:
        tokens.append(value)
        return f"@@TOKEN{len(tokens) - 1}@@"

    linked = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda match: stash(
            f'<link href="{html.escape(match.group(2), quote=True)}">'
            f"{html.escape(match.group(1))}</link>"
        ),
        text,
    )
    escaped = html.escape(linked)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    # Word-bounded underscores only, so identifiers like HCI004_ZERO_TESTS survive.
    escaped = re.sub(r"(?<![A-Za-z0-9])_(.+?)_(?![A-Za-z0-9])", r"<i>\1</i>", escaped)
    for index, token in enumerate(tokens):
        escaped = escaped.replace(f"@@TOKEN{index}@@", token)
    return escaped


def style(name: str, **values) -> ParagraphStyle:
    base = {"fontName": "Helvetica", "textColor": INK}
    base.update(values)
    return ParagraphStyle(name, **base)


STYLES = {
    "name": style("Name", fontName="Helvetica-Bold", fontSize=25, leading=27),
    "target": style("Target", fontName="Helvetica-Bold", fontSize=9.4, leading=12, textColor=ACCENT, spaceBefore=2.4 * mm),
    "contact": style("Contact", fontSize=8.4, leading=11.6, alignment=TA_RIGHT),
    "lede": style("Lede", fontSize=9.7, leading=13.8),
    "figure": style("Figure", fontName="Helvetica-Bold", fontSize=17, leading=19),
    "figure_label": style("FigureLabel", fontSize=7.6, leading=9.4, textColor=MUTED, spaceBefore=1.1 * mm),
    "label": style("Label", fontName="Helvetica-Bold", fontSize=8.6, leading=11),
    "entry": style("Entry", fontName="Helvetica-Bold", fontSize=10, leading=12.5),
    "meta": style("Meta", fontSize=8, leading=12.5, textColor=ACCENT, alignment=TA_RIGHT),
    "sub": style("Sub", fontSize=8, leading=10.6, textColor=MUTED, spaceAfter=0.7 * mm),
    "body": style("Body", fontSize=8.9, leading=12),
    "bullet": style(
        "Bullet",
        fontSize=8.9,
        leading=11.9,
        leftIndent=3.8 * mm,
        bulletIndent=0,
        bulletFontName="Helvetica-Bold",
        bulletColor=ACCENT,
        spaceAfter=0.55 * mm,
    ),
    "date": style("Date", fontSize=8, leading=11.9, textColor=FAINT, alignment=TA_RIGHT),
    "term": style("Term", fontSize=8.4, leading=12, textColor=MUTED),
    "footer": style("Footer", fontSize=7.2, leading=9, textColor=FAINT),
}

FLUSH = [
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
]


def plain(text: str) -> str:
    return re.sub(r"\*\*|\[([^\]]+)\]\([^)]+\)", lambda match: match.group(1) or "", text)


def fits_inline(title: str, sub: str) -> bool:
    """True when the sub line fits on the entry's title row beside its title."""
    entry, small = STYLES["entry"], STYLES["sub"]
    width = (
        stringWidth(plain(title), entry.fontName, entry.fontSize)
        + STACK_GAP
        + stringWidth(plain(sub), small.fontName, small.fontSize)
    )
    return width <= BODY_WIDTH - META_WIDTH


def para(text: str, key: str, **kwargs) -> Paragraph:
    return Paragraph(inline_markup(text), STYLES[key], **kwargs)


def row(cells: list, widths: list[float], extra: list | None = None, valign: str = "TOP") -> Table:
    table = Table([cells], colWidths=widths)
    table.setStyle(TableStyle(FLUSH + [("VALIGN", (0, 0), (-1, -1), valign)] + (extra or [])))
    return table


# ---------------------------------------------------------------- layout


def masthead(cv: CV) -> list:
    left = [para(cv.name, "name")]
    if cv.target:
        left.append(para(cv.target, "target"))
    right = [para(item, "contact") for item in cv.contact]
    header = row(
        [left, right],
        [CONTENT_WIDTH - CONTACT_WIDTH, CONTACT_WIDTH],
        [
            ("LINEBELOW", (0, 0), (-1, 0), 0.8, INK),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 4.2 * mm),
        ],
        valign="BOTTOM",
    )
    flowables: list = [header]
    for text in cv.lede:
        flowables += [Spacer(1, 4.6 * mm), para(text, "lede")]
    return flowables


def highlights(section: Section) -> list:
    width = CONTENT_WIDTH / len(section.blocks)
    cells = [[para(block.right, "figure"), para(block.text, "figure_label")] for block in section.blocks]
    table = Table([cells], colWidths=[width] * len(cells))
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), WASH),
                ("LINEABOVE", (0, 0), (-1, 0), 0.5, RULE),
                ("LINEBELOW", (0, 0), (-1, 0), 0.5, RULE),
                ("LINEBEFORE", (1, 0), (-1, 0), 0.5, RULE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3.4 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2.4 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 2.6 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2.8 * mm),
            ]
        )
    )
    return [Spacer(1, 5 * mm), table]


def section_body(section: Section) -> list:
    flowables: list = []
    blocks = section.blocks
    for index, block in enumerate(blocks):
        if block.kind == "entry":
            if index:
                flowables.append(Spacer(1, 2.6 * mm))
            title = inline_markup(block.text)
            following = blocks[index + 1] if index + 1 < len(blocks) else None
            if following and following.kind == "sub" and fits_inline(block.text, following.text):
                small = STYLES["sub"]
                title += (
                    f'<font name="{small.fontName}" size="{small.fontSize}" color="{MUTED.hexval()}">'
                    f"&nbsp;&nbsp;&nbsp;{inline_markup(following.text)}</font>"
                )
                following.kind = "inline"
            flowables.append(
                row(
                    [Paragraph(title, STYLES["entry"]), para(block.right, "meta")],
                    [BODY_WIDTH - META_WIDTH, META_WIDTH],
                    valign="BOTTOM",
                )
            )
            if following and following.kind == "inline":
                flowables.append(Spacer(1, 0.9 * mm))
        elif block.kind == "inline":
            continue
        elif block.kind == "sub":
            flowables.append(para(block.text, "sub"))
        elif block.kind == "body":
            flowables.append(para(block.text, "body"))
        elif block.kind == "term":
            flowables.append(
                row(
                    [para(block.term, "term"), para(block.text, "body")],
                    [TERM_WIDTH, BODY_WIDTH - TERM_WIDTH],
                    [("BOTTOMPADDING", (0, 0), (-1, -1), 0.6 * mm)],
                )
            )
        elif block.right:
            flowables.append(
                row(
                    [para(block.text, "bullet", bulletText="–"), para(block.right, "date")],
                    [BODY_WIDTH - DATE_WIDTH, DATE_WIDTH],
                )
            )
        else:
            flowables.append(para(block.text, "bullet", bulletText="–"))
    return flowables


def labelled(section: Section) -> list:
    table = Table(
        [[para(section.title, "label"), "", section_body(section)]],
        colWidths=[LABEL_WIDTH, GUTTER, BODY_WIDTH],
    )
    table.setStyle(
        TableStyle(
            FLUSH
            + [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LINEABOVE", (0, 0), (0, 0), 1.3, ACCENT),
                ("LINEABOVE", (2, 0), (2, 0), 0.5, RULE),
                ("TOPPADDING", (0, 0), (-1, -1), 2.3 * mm),
            ]
        )
    )
    return [Spacer(1, 4.8 * mm), table]


def layout(cv: CV) -> list:
    flowables = masthead(cv)
    for section in cv.sections:
        flowables += highlights(section) if section.title == HIGHLIGHTS else labelled(section)
    return flowables


class OnePageCV(BaseDocTemplate):
    def __init__(self, output: Path, footer: str) -> None:
        super().__init__(
            str(output),
            pagesize=A4,
            leftMargin=MARGIN_X,
            rightMargin=MARGIN_X,
            topMargin=MARGIN_TOP,
            bottomMargin=MARGIN_BOTTOM,
            title="Chih-Kai Wang - Curriculum Vitae",
            author="Chih-Kai Wang",
            subject="Software engineering internships and research tools",
            creator="cv/build_cv.py",
            pageCompression=1,
        )
        self.footer = footer
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
        self.addPageTemplates(PageTemplate(id="cv", frames=[frame], onPage=self.draw_footer))

    def draw_footer(self, canvas, document) -> None:
        if not self.footer:
            return
        canvas.saveState()
        canvas.setFont(STYLES["footer"].fontName, STYLES["footer"].fontSize)
        canvas.setFillColor(FAINT)
        canvas.drawString(MARGIN_X, 8.5 * mm, self.footer)
        canvas.restoreState()

    def afterPage(self) -> None:
        if self.page > 1:
            raise RuntimeError("CV overflowed one page; shorten content or adjust spacing")


def check_source(source: str) -> None:
    if any(character in source for character in ("‑", "–", "—")):
        raise ValueError("CV source must use ASCII hyphens only")
    try:
        source.encode("cp1252")
    except UnicodeEncodeError as error:
        character = source[error.start]
        raise ValueError(
            f"CV source contains {character!r} (U+{ord(character):04X}), which the "
            "built-in Helvetica cannot draw; use a cp1252 character instead"
        ) from None


def build(source_path: Path, output_path: Path) -> None:
    source = source_path.read_text(encoding="utf-8")
    check_source(source)
    cv = parse(source)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    document = OnePageCV(output_path, cv.footer)
    document.build(layout(cv))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    build(args.source.resolve(), args.output.resolve())
    print(f"Wrote {args.output.resolve()}")


if __name__ == "__main__":
    main()
