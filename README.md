# The World in One Day — Tuesday 24 November 2026

make.fun entry for **news-image-20261124** — "Sum up 24 November's world news
in one image". $100 pool, 50 paid places (1st $20). Deadline **2026-11-26
08:00 CST** (2026-11-26 00:00 UTC). No house baseline to beat.

## What it is

One 1024×1024 PNG front page: 28 stories, 7 regions, 12 illustrated cards
(3 leads + 9 cards) plus 16 one-line briefs. Flat vector style, drawn in code.

## How it runs

`main.py` (Python 3.13, stdlib only) copies the fixed image
`assets/entry.png` to `/output/entry.png`. No network, no clock, no random —
two runs write identical bytes, as the brief requires. The image itself was
generated locally by `generate.py` (Pillow + DejaVu fonts, deterministic;
re-running it produces the same MD5).

## Date check

Every story is dated **24 November 2026** in its source. Sources checked
2026-11-24 ~16:00 CST: SCMP world headlines, The Japan Times, Times of
India live blog, The Daily Edition No. 279, Xinhua 0030 GMT summary.
Disputed/conflict claims are worded as claims ("Kyiv says…", "reports say…").
Stories from 23 Nov or earlier were excluded.

Leads: COP31 collapses with no deal (Antalya, ~50h overtime, 90+ nations
reject draft); Ukraine drones sink Russian corvette Merkury off Benghazi,
Libya; Nvidia rehires Jensen Huang after a Trump push.

## Status

- [x] Image built and visually checked: 1024×1024, 149,317 bytes (< 1 MiB)
- [x] `main.py` verified: two runs, identical bytes
- [ ] Needs the user's make.fun account first (register at make.fun, ideally
      with GitHub xuenai0112), then Muse connects its keypair — user approves
      a link + code within 15 minutes
- [ ] Then: public GitHub repo under the user's account (created after the
      competition opened), submit, upload this session's transcript
