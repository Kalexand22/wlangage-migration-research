#!/usr/bin/env python3
"""Assemble the original research chapters into one convenient Markdown file."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(\[[^\]\n]+\]\()([^\s)]+)(\))")


def relative_link(match):
    before, target, after = match.groups()
    if target.startswith(("https://", "http://", "mailto:", "#", "/")):
        return match.group(0)
    path, separator, anchor = target.partition("#")
    resolved = (ROOT / "docs" / path).resolve().relative_to(ROOT).as_posix()
    return before + resolved + (separator + anchor if separator else "") + after


def main():
    chunks = [
        "# Recherche : plateforme compatible WLangage et migration WINDEV\n",
        "Date : 26 octobre 2026. Rapport assemblé à partir des chapitres de `docs/`. "
        "Modifier les chapitres puis relancer `python3 tools/assemble_report.py`.\n",
        "Cette étude décrit un produit à développer. Elle ne certifie aucune compatibilité exécutée. "
        "Le périmètre, les limites et la méthode d'exhaustivité figurent dans les chapitres 00 et 06.\n",
        "[Sommaire du dépôt](README.md) · [Matrice fonctionnelle](data/fonctionnalites.csv)\n",
    ]
    for path in sorted((ROOT / "docs").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        # Keep code fences intact, including headings used inside examples.
        fenced = False
        lines = []
        for line in text.splitlines():
            if line.lstrip().startswith("```"):
                fenced = not fenced
            if not fenced and line.startswith("#"):
                line = "#" + line
            lines.append(line)
        text = LINK.sub(relative_link, "\n".join(lines))
        chunks.append("\n---\n\n" + text + "\n")
    output = ROOT / "RAPPORT_COMPLET.md"
    output.write_text("\n".join(chunks), encoding="utf-8")
    print(f"Rapport assemblé : {len(list((ROOT / 'docs').glob('*.md')))} chapitres")


if __name__ == "__main__":
    main()
