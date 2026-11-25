#!/usr/bin/env python3
"""Generate the 24 Nov 2026 world-news front page v2 (1024x1024 PNG).
Deterministic: fixed assets, fixed story list, no network, no clock, no random.
Run: python3 generate.py -> writes assets/entry.png
Layout: AI-illustrated triptych of the three lead stories on top,
code-typeset headlines, cards and briefs below (27 stories, 7 regions).
Stories as collected 2026-11-24 from SCMP, Japan Times, Times of India,
The Daily Edition and Xinhua; all items dated 24 Nov 2026."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W = H = 1024
FD = "/usr/share/fonts/truetype/dejavu/"
def F(name, size): return ImageFont.truetype(FD + name, size)
F_TITLE = F("DejaVuSerif-Bold.ttf", 40)
F_SUB   = F("DejaVuSans.ttf", 14)
F_H1    = F("DejaVuSans-Bold.ttf", 19)
F_H2    = F("DejaVuSans-Bold.ttf", 15)
F_BODY  = F("DejaVuSans.ttf", 12)
F_SMALL = F("DejaVuSans.ttf", 11)
F_TAG   = F("DejaVuSans-Bold.ttf", 11)
F_FOOT  = F("DejaVuSans.ttf", 10)

NAVY = (16, 32, 64); PAPER = (250, 246, 236); INK = (20, 20, 20)
GREY = (90, 90, 90); RED = (178, 34, 34); TEAL = (0, 110, 110)
GOLD = (176, 124, 0); BLUE = (30, 80, 160); GREEN = (34, 110, 60)

LEADS = [
    ("CLIMATE", RED, "COP31 collapses with no deal",
     "Antalya talks run ~50 hours into overtime, then 90+ nations reject a draft that never names fossil fuels."),
    ("CONFLICT", NAVY, "Ukraine drones sink Russian warship off Libya",
     "Kyiv says 7 naval drones sank the corvette Merkury at Benghazi - the Black Sea fight reaches the Mediterranean."),
    ("TECH", TEAL, "Nvidia rehires Jensen Huang",
     "Board reverses course after a Trump push; reports say JD Vance lobbied directors to bring the CEO back."),
]
CARDS = [
    ("MIDDLE EAST", RED, "Iran vows to counter US naval blockade",
     "Tehran says it will use every means; US widens sanctions on shadow-banking exchange houses."),
    ("ASIA", BLUE, "Korean jets scramble as Russian planes enter zone",
     "Seoul scrambles fighters as a suspected North Korean aircraft breaches airspace near Ulleung."),
    ("EUROPE", NAVY, "Moscow: Estonia moves 'on verge of open war'",
     "Allies warn Russia may launch a nuclear-armed satellite next month; 25 airspace violations in 2026."),
    ("AMERICAS", GREEN, "Democrats take the US House",
     "A North Carolina win gives Democrats their 258th seat in the next House - their widest margin in 50 years."),
    ("TECH", TEAL, "States sue Musk firms over Grok images",
     "Oregon and Virginia sue SpaceX companies over sexualised images made with Grok, reports say."),
    ("ASIA", GOLD, "UK sanctions Myanmar leaders after ICJ ruling",
     "After last week's ruling that Myanmar committed genocide against the Rohingya in 2017."),
]
BRIEFS = [
    ("EUROPE", "Armenia unveils draft constitution."),
    ("SPORT", "Women's World Cup 2031 hosts: USA, Mexico, Costa Rica, Jamaica."),
    ("CULTURE", "Acropolis Museum reopens after 7 years."),
    ("N. AMERICA", "Trump halts Iowa detonation pending court ruling."),
    ("N. AMERICA", "Honda recalls 810,000 US cars over airbag risk."),
    ("N. AMERICA", "Amtrak derails in Louisiana; 5 hurt."),
    ("MIDDLE EAST", "Qatar PM meets US Secretary Rubio."),
    ("MIDDLE EAST", "Saudi coalition intercepts Houthi drone."),
    ("MIDDLE EAST", "Lebanon condemns Israeli school visit."),
    ("EUROPE", "Burnham: no EU return without referendum."),
    ("EUROPE", "EU proposes banning Russian flags at sports events."),
    ("ASIA", "N. Korea threatens to shut its Swiss office."),
    ("ASIA", "Indonesia charges ex-police chief with treason."),
    ("ASIA", "Hasina seeks return to Bangladesh."),
    ("ASIA", "China, Mexico agree a trade working group."),
    ("AFRICA", "Zanzibar hotel fire evacuates 180 tourists."),
    ("WORLD", "UN: wars put food aid for 7.3m more at risk."),
    ("TECH", "Anthropic launches Claude Ship for code review."),
]

def wrap(d, text, font, width):
    lines, cur = [], ""
    for word in text.split(" "):
        t = (cur + " " + word).strip()
        if d.textlength(t, font=font) <= width:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = word
    if cur: lines.append(cur)
    return lines

def para(d, x, y, text, font, width, fill=INK, lh=None):
    lh = lh or int(font.size * 1.3)
    for ln in wrap(d, text, font, width):
        d.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y

def cover_crop(im, tw, th, cy_frac=0.5):
    sw, sh = im.size
    scale = max(tw / sw, th / sh)
    nw, nh = int(sw * scale + 0.5), int(sh * scale + 0.5)
    im2 = im.resize((nw, nh), Image.LANCZOS)
    x = (nw - tw) // 2
    y = int((nh - th) * cy_frac)
    return im2.crop((x, y, x + tw, y + th))

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# Masthead
d.rectangle([0, 0, W, 88], fill=NAVY)
d.text((24, 12), "THE WORLD IN ONE DAY", font=F_TITLE, fill=(255, 255, 255))
d.text((24, 58), "Tuesday, 24 November 2026  -  27 stories  -  7 regions",
       font=F_SUB, fill=(200, 210, 230))
d.text((W - 24, 20), "ONE PAGE", font=F_TAG, fill=GOLD, anchor="ra")
d.text((W - 24, 58), "All stories dated 24 Nov 2026", font=F_SMALL,
       fill=(200, 210, 230), anchor="ra")

# Hero: triptych of the three leads
hero = Image.open(os.path.join(HERE, "assets", "hero_triptych.jpg")).convert("RGB")
img.paste(cover_crop(hero, 992, 340, 0.46), (16, 98))

# Lead strip aligned to panels
y = 446
for i, (tagname, col, head, body) in enumerate(LEADS):
    x = 16 + i * 334
    d.rectangle([x, y, x + 322, y + 5], fill=col)
    d.text((x + 2, y + 10), tagname, font=F_TAG, fill=col)
    yy = para(d, x + 2, y + 24, head, F_H1, 316, lh=21)
    para(d, x + 2, yy + 2, body, F_BODY, 316, fill=(50, 50, 50), lh=14)

# Cards: 2 rows x 3
y0 = 560
for i, (tagname, col, head, body) in enumerate(CARDS):
    cx = 16 + (i % 3) * 334
    cy = y0 + (i // 3) * 112
    d.rounded_rectangle([cx, cy, cx + 322, cy + 108], radius=10,
                        fill=(255, 255, 255), outline=(210, 205, 190))
    d.rectangle([cx, cy, cx + 6, cy + 108], fill=col)
    wtag = int(d.textlength(tagname, font=F_TAG)) + 12
    d.rounded_rectangle([cx + 14, cy + 8, cx + 14 + wtag, cy + 25], radius=8, fill=col)
    d.text((cx + 20, cy + 10), tagname, font=F_TAG, fill=(255, 255, 255))
    yy = para(d, cx + 14, cy + 30, head, F_H2, 294, lh=17)
    para(d, cx + 14, yy + 1, body, F_BODY, 294, fill=(50, 50, 50), lh=14)

# Briefs: heading + 2 cols x 9 one-liners
by = 788
d.text((16, by), "ALSO ON 24 NOVEMBER", font=F_H1, fill=NAVY)
d.text((W - 16, by + 4), "18 briefs", font=F_SMALL, fill=GREY, anchor="ra")
d.line([16, by + 24, W - 16, by + 24], fill=NAVY, width=2)
half = 9
for col_i, chunk in enumerate((BRIEFS[:half], BRIEFS[half:])):
    x = 16 if col_i == 0 else 520
    yy = by + 32
    for region, text in chunk:
        d.text((x, yy), region, font=F_TAG, fill=RED)
        lines = wrap(d, text, F_SMALL, 388)
        assert len(lines) == 1, (region, text, lines)
        d.text((x + 100, yy + 1), lines[0], font=F_SMALL, fill=INK)
        yy += 19
d.line([16, 988, W - 16, 988], fill=(180, 175, 160), width=1)
d.text((16, 995), "Every item dated 24 Nov 2026 in its source (SCMP, Japan Times, Times of India, The Daily Edition, Xinhua). Conflict claims as reported.",
       font=F_FOOT, fill=GREY)
d.text((W - 16, 995), "27 stories", font=F_FOOT, fill=GREY, anchor="ra")

p = os.path.join(HERE, "assets", "entry.png")
img.save(p, optimize=True)
print("saved", p, os.path.getsize(p))
