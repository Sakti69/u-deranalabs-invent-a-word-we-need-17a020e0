"""Miswave — entry for make.fun "Invent a Word We Need".

Writes the one-line coinage to /output/entry.txt.

Run: python3 main.py
"""

from pathlib import Path

ENTRY = "Miswave — the embarrassment of waving back at a stranger who was waving at someone behind you."

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(ENTRY, encoding="utf-8")
