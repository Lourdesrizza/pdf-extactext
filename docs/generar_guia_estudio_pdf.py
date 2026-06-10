from pathlib import Path
import re
import textwrap

import fitz


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "guia_estudio_repositorio.md"
OUTPUT = ROOT / "guia_estudio_repositorio.pdf"

PAGE_WIDTH = 595
PAGE_HEIGHT = 842
MARGIN_X = 48
MARGIN_TOP = 52
MARGIN_BOTTOM = 48
LINE_HEIGHT = 14


def clean_markdown(line: str) -> tuple[str, int, bool]:
    stripped = line.rstrip()
    if stripped.startswith("# "):
        return stripped[2:], 18, True
    if stripped.startswith("## "):
        return stripped[3:], 15, True
    if stripped.startswith("### "):
        return stripped[4:], 13, True
    if stripped.startswith("- "):
        return "• " + stripped[2:], 11, False
    if re.match(r"^\d+\. ", stripped):
        return stripped, 11, False
    return stripped, 11, False


def wrap_line(text: str, font_size: int, in_code: bool) -> list[str]:
    if not text:
        return [""]
    width = 74 if font_size <= 11 else 58
    if in_code:
        width = 82
    return textwrap.wrap(
        text,
        width=width,
        replace_whitespace=False,
        drop_whitespace=False,
        break_long_words=False,
    ) or [""]


def add_footer(page: fitz.Page, page_number: int) -> None:
    footer = f"Guia de estudio pdf-extactext - pagina {page_number}"
    page.insert_text(
        (MARGIN_X, PAGE_HEIGHT - 24),
        footer,
        fontsize=9,
        fontname="helv",
        color=(0.35, 0.35, 0.35),
    )


def main() -> None:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    doc = fitz.open()
    page = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)
    page_number = 1
    y = MARGIN_TOP
    in_code = False

    for raw_line in lines:
        if raw_line.strip().startswith("```"):
            in_code = not in_code
            y += LINE_HEIGHT * 0.6
            continue

        text, font_size, bold = clean_markdown(raw_line)
        font = "cour" if in_code else ("helv" if not bold else "hebo")
        color = (0.08, 0.08, 0.08) if not in_code else (0.18, 0.18, 0.18)
        extra_before = 7 if bold else 0

        if y + extra_before > PAGE_HEIGHT - MARGIN_BOTTOM:
            add_footer(page, page_number)
            page = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)
            page_number += 1
            y = MARGIN_TOP

        y += extra_before

        for wrapped in wrap_line(text, font_size, in_code):
            if y > PAGE_HEIGHT - MARGIN_BOTTOM:
                add_footer(page, page_number)
                page = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)
                page_number += 1
                y = MARGIN_TOP

            page.insert_text(
                (MARGIN_X, y),
                wrapped,
                fontsize=font_size,
                fontname=font,
                color=color,
            )
            y += LINE_HEIGHT + max(font_size - 11, 0) * 0.4

        if not text:
            y += 3

    add_footer(page, page_number)
    doc.save(OUTPUT)
    doc.close()


if __name__ == "__main__":
    main()
