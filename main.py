#!/usr/bin/env python3
"""make.fun entry: Sum up 24 November's world news in one image.

Writes the pre-rendered front page to /output/entry.png.
Deterministic by construction: it copies fixed bytes from assets/entry.png,
uses no network, no clock and no randomness, so two runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
