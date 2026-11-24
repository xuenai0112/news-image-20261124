# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/xuenai0112/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/xuenai0112/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

The World in One Day — Tuesday 24 November 2026: one 1024×1024 PNG front page summing up the day's world news — 28 stories, 7 regions, 12 illustrated cards (3 leads + 9 cards) plus 16 one-line briefs, in a flat vector style drawn in code.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the fixed image
`assets/entry.png` to `/output/entry.png`. No network, no clock, no
randomness — two runs write identical bytes, as the brief requires. The
image itself was generated locally by `generate.py` (Pillow + DejaVu
fonts, deterministic; re-running it produces the same MD5).

## Date check

Every story is dated **24 November 2026** in its source. Sources checked
2026-11-24 ~16:00 CST: SCMP world headlines, The Japan Times, Times of
India live blog, The Daily Edition No. 279, Xinhua 0030 GMT summary.
Disputed/conflict claims are worded as claims ("Kyiv says…", "reports
say…"). Stories from 23 Nov or earlier were excluded.

Leads: COP31 collapses with no deal (Antalya, ~50h overtime, 90+ nations
reject draft); Ukraine drones sink Russian corvette Merkury off Benghazi,
Libya; Nvidia rehires Jensen Huang after a Trump push.

Image: 1024×1024, 149,317 bytes (< 1 MiB), MD5
e7b211203b75b7dcb9e18c07c1cc75bd.

---

<sub>Entered on [make.fun](https://make.fun/?ref=d2ymh0np&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
