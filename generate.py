#!/usr/bin/env python3
"""Generate the 24 Nov 2026 world-news front page (1024x1024 PNG).
Deterministic: fixed date, fixed story list, no network, no random, no clock.
Run: python3 generate.py  -> writes assets/entry.png
Stories were collected 2026-11-24 ~16:00 CST from SCMP, Japan Times,
Times of India, The Daily Edition, Xinhua summary and make.fun's own
prior-day winner notes. Anything dated 23 Nov or earlier is excluded
except where the report itself is dated 24 Nov (marked 'reported 24 Nov').
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
FD = "/usr/share/fonts/truetype/dejavu/"
F_TITLE = ImageFont.truetype(FD + "DejaVuSerif-Bold.ttf", 44)
F_SUB = ImageFont.truetype(FD + "DejaVuSans.ttf", 15)
F_H1 = ImageFont.truetype(FD + "DejaVuSans-Bold.ttf", 21)
F_H2 = ImageFont.truetype(FD + "DejaVuSans-Bold.ttf", 16)
F_BODY = ImageFont.truetype(FD + "DejaVuSans.ttf", 13)
F_SMALL = ImageFont.truetype(FD + "DejaVuSans.ttf", 11)
F_TAG = ImageFont.truetype(FD + "DejaVuSans-Bold.ttf", 11)
F_FOOT = ImageFont.truetype(FD + "DejaVuSans.ttf", 10)

NAVY = (16, 32, 64); PAPER = (250, 246, 236); INK = (20, 20, 20)
GREY = (90, 90, 90); RED = (178, 34, 34); TEAL = (0, 110, 110)
GOLD = (176, 124, 0); BLUE = (30, 80, 160); GREEN = (34, 110, 60)
SKY = (210, 228, 240); SAND = (238, 226, 200)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, font, width):
    lines, cur = [], ""
    for word in text.split(" "):
        t = (cur + " " + word).strip()
        if d.textlength(t, font=font) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

def para(x, y, text, font, width, fill=INK, lh=None):
    lh = lh or int(font.size * 1.28)
    for ln in wrap(text, font, width):
        d.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y

def tag(x, y, label, color):
    w = int(d.textlength(label, font=F_TAG)) + 12
    d.rounded_rectangle([x, y, x + w, y + 17], radius=8, fill=color)
    d.text((x + 6, y + 2), label, font=F_TAG, fill=(255, 255, 255))
    return w

def icon(kind, x, y, s, color):
    """Simple flat vector icon drawn with shapes only."""
    if kind == "globe":
        d.ellipse([x, y, x + s, y + s], fill=TEAL)
        d.ellipse([x + s*0.2, y + s*0.2, x + s*0.8, y + s*0.8], outline=(255,255,255), width=2)
        d.line([x, y + s/2, x + s, y + s/2], fill=(255,255,255), width=2)
    elif kind == "ship":
        d.polygon([(x, y+s*0.7), (x+s, y+s*0.7), (x+s*0.85, y+s), (x+s*0.15, y+s)], fill=color)
        d.rectangle([x+s*0.45, y+s*0.2, x+s*0.55, y+s*0.7], fill=color)
        d.polygon([(x+s*0.55, y+s*0.2), (x+s*0.85, y+s*0.4), (x+s*0.55, y+s*0.4)], fill=RED)
        for i in range(3):
            d.arc([x+i*s*0.3, y+s*0.05, x+(i+1)*s*0.3, y+s*0.25], 180, 360, fill=BLUE, width=2)
    elif kind == "chip":
        d.rounded_rectangle([x+s*0.2, y+s*0.2, x+s*0.8, y+s*0.8], radius=6, fill=color)
        d.rectangle([x+s*0.42, y+s*0.42, x+s*0.58, y+s*0.58], fill=(255,255,255))
        for i in range(3):
            d.line([x+s*0.2+i*s*0.2, y, x+s*0.2+i*s*0.2, y+s*0.2], fill=color, width=3)
            d.line([x+s*0.2+i*s*0.2, y+s*0.8, x+s*0.2+i*s*0.2, y+s], fill=color, width=3)
    elif kind == "plane":
        d.polygon([(x, y+s*0.5), (x+s*0.9, y+s*0.35), (x+s, y+s*0.5), (x+s*0.9, y+s*0.65)], fill=color)
        d.polygon([(x+s*0.3, y+s*0.5), (x+s*0.5, y+s*0.2), (x+s*0.6, y+s*0.5)], fill=color)
        d.polygon([(x+s*0.3, y+s*0.5), (x+s*0.5, y+s*0.8), (x+s*0.6, y+s*0.5)], fill=color)
    elif kind == "flag":
        d.rectangle([x, y, x+4, y+s], fill=(60,60,60))
        d.polygon([(x+4, y), (x+s, y), (x+s*0.8, y+s*0.35), (x+s, y+s*0.7), (x+4, y+s*0.7)], fill=color)
    elif kind == "scale":
        d.line([x+s/2, y, x+s/2, y+s*0.7], fill=color, width=3)
        d.line([x+s*0.1, y+s*0.15, x+s*0.9, y+s*0.15], fill=color, width=3)
        d.polygon([(x, y+s*0.7), (x+s*0.3, y+s*0.7), (x+s*0.15, y+s*0.35)], outline=color, width=2)
        d.polygon([(x+s*0.7, y+s*0.7), (x+s, y+s*0.7), (x+s*0.85, y+s*0.35)], outline=color, width=2)
    elif kind == "ball":
        d.ellipse([x, y, x+s, y+s], fill=(255,255,255), outline=color, width=3)
        d.polygon([(x+s*0.5, y+s*0.35), (x+s*0.65, y+s*0.5), (x+s*0.5, y+s*0.65), (x+s*0.35, y+s*0.5)], fill=color)
    elif kind == "book":
        d.rectangle([x+s*0.15, y+s*0.1, x+s*0.85, y+s*0.9], fill=color)
        d.rectangle([x+s*0.15, y+s*0.1, x+s*0.5, y+s*0.9], fill=(255,255,255))
        d.line([x+s*0.2, y+s*0.3, x+s*0.45, y+s*0.3], fill=color, width=2)
        d.line([x+s*0.2, y+s*0.5, x+s*0.45, y+s*0.5], fill=color, width=2)
    elif kind == "anchor":
        d.ellipse([x+s*0.4, y, x+s*0.6, y+s*0.2], outline=color, width=3)
        d.line([x+s/2, y+s*0.15, x+s/2, y+s*0.9], fill=color, width=3)
        d.arc([x, y+s*0.45, x+s, y+s], 0, 180, fill=color, width=3)
    elif kind == "capitol":
        d.polygon([(x+s*0.2, y+s*0.4), (x+s*0.5, y+s*0.1), (x+s*0.8, y+s*0.4)], fill=color)
        d.rectangle([x+s*0.15, y+s*0.4, x+s*0.85, y+s*0.85], fill=color)
        for i in range(3):
            d.rectangle([x+s*0.25+i*s*0.22, y+s*0.55, x+s*0.33+i*s*0.22, y+s*0.85], fill=(255,255,255))
    elif kind == "leaf":
        d.ellipse([x, y+s*0.2, x+s*0.8, y+s], fill=color)
        d.polygon([(x+s*0.7, y), (x+s, y+s*0.3), (x+s*0.8, y+s*0.1)], fill=GREEN)
    elif kind == "bolt":
        d.polygon([(x+s*0.55, y), (x+s*0.2, y+s*0.55), (x+s*0.45, y+s*0.55), (x+s*0.35, y+s), (x+s*0.8, y+s*0.45), (x+s*0.55, y+s*0.45)], fill=color)

# ---- Masthead ----
d.rectangle([0, 0, W, 92], fill=NAVY)
d.text((24, 14), "THE WORLD IN ONE DAY", font=F_TITLE, fill=(255, 255, 255))
d.text((24, 62), "Tuesday, 24 November 2026  •  28 stories  •  7 regions  •  12 illustrated",
       font=F_SUB, fill=(200, 210, 230))
d.text((W-24, 22), "ONE PAGE", font=F_TAG, fill=GOLD, anchor="ra")
d.text((W-24, 62), "All stories dated 24 Nov 2026", font=F_SMALL, fill=(200, 210, 230), anchor="ra")

# ---- Lead row: 3 big cards ----
leads = [
    ("CLIMATE", RED, "globe", "COP31 collapses with no deal",
     "Antalya talks run ~50 hours into overtime, then 90+ nations reject a draft that never names fossil fuels."),
    ("CONFLICT", NAVY, "ship", "Ukraine drones sink Russian warship off Libya",
     "Kyiv says 7 naval drones sank the corvette Merkury at Benghazi — the Black Sea fight reaches the Mediterranean."),
    ("TECH", TEAL, "chip", "Nvidia rehires Jensen Huang",
     "Board reverses course after a Trump push; reports say JD Vance lobbied directors to bring the CEO back."),
]
x = 16
for tagname, col, ic, head, body in leads:
    d.rounded_rectangle([x, 106, x + 322, 268], radius=10, fill=(255, 255, 255), outline=(210, 205, 190))
    d.rounded_rectangle([x, 106, x + 322, 132], radius=10, fill=col)
    d.rectangle([x, 122, x + 322, 132], fill=col)
    d.text((x + 12, 111), tagname, font=F_TAG, fill=(255, 255, 255))
    icon(ic, x + 12, 142, 46, col)
    yy = para(x + 68, 140, head, F_H2, 240, lh=19)
    para(x + 12, 196, body, F_BODY, 298, fill=(50, 50, 50))
    x += 334

# ---- Middle grid: 9 illustrated cards ----
cards = [
    ("MIDDLE EAST", RED, "anchor", "Iran vows to counter US naval blockade",
     "Tehran says it will use every means; US widens sanctions on exchange houses accused of shadow banking."),
    ("ASIA", BLUE, "plane", "Korean jets scramble as Russian planes enter zone",
     "Seoul scrambles fighters; a suspected North Korean aircraft breaches airspace near Ulleung island."),
    ("EUROPE", NAVY, "flag", "Moscow: Estonia moves 'on verge of open war'",
     "Allies warn Russia may launch a nuclear-armed satellite next month; NATO counts 25 airspace violations in 2026."),
    ("AMERICAS", GREEN, "capitol", "Democrats take the US House",
     "A North Carolina win gives Democrats their 258th seat in the next House — their widest margin in 50 years."),
    ("TECH", TEAL, "bolt", "States sue Musk firms over Grok images",
     "Oregon and Virginia sue SpaceX companies over sexualised images made with Grok, reports say."),
    ("ASIA", GOLD, "scale", "UK sanctions Myanmar leaders after ICJ ruling",
     "Sanctions follow last week's court ruling that Myanmar committed genocide against the Rohingya in 2017."),
    ("EUROPE", BLUE, "flag", "Armenia unveils draft constitution",
     "The draft is billed as a key step toward peace with neighbour Azerbaijan."),
    ("SPORT", GREEN, "ball", "2031 Women's World Cup hosts named",
     "USA, Mexico, Costa Rica and Jamaica to host 2031; the UK gets the 2035 edition."),
    ("CULTURE", GOLD, "capitol", "Acropolis Museum reopens after 7 years",
     "Greece reopens its oldest museum after a seven-year, €6.2m restoration."),
]
y0 = 282
for i, (tagname, col, ic, head, body) in enumerate(cards):
    cx = 16 + (i % 3) * 334
    cy = y0 + (i // 3) * 158
    d.rounded_rectangle([cx, cy, cx + 322, cy + 146], radius=10, fill=(255, 255, 255), outline=(210, 205, 190))
    d.rectangle([cx, cy, cx + 6, cy + 146], fill=col)
    tag(cx + 16, cy + 10, tagname, col)
    icon(ic, cx + 16, cy + 36, 40, col)
    para(cx + 66, cy + 34, head, F_H2, 244, lh=19)
    para(cx + 16, cy + 92, body, F_BODY, 292, fill=(50, 50, 50))

# ---- Briefs: two columns, 18 more stories ----
d.text((16, 768), "ALSO ON 24 NOVEMBER", font=F_H2, fill=NAVY)
d.line([16, 792, W - 16, 792], fill=NAVY, width=2)
briefs_l = [
    ("N. AMERICA", "Trump halts Iowa detonation pending court ruling."),
    ("N. AMERICA", "Honda recalls 810,000 US cars over airbag risk."),
    ("N. AMERICA", "Amtrak derails in Louisiana; 5 hurt."),
    ("MIDDLE EAST", "Qatar PM meets US Secretary Rubio."),
    ("MIDDLE EAST", "Saudi coalition intercepts Houthi drone."),
    ("MIDDLE EAST", "Lebanon condemns Israeli school visit."),
    ("EUROPE", "Burnham: no EU return without referendum."),
    ("EUROPE", "EU proposes banning Russian flags at sports events."),
]
briefs_r = [
    ("ASIA", "N. Korea threatens to shut its Swiss office."),
    ("ASIA", "Indonesia charges ex-police chief with treason."),
    ("ASIA", "Hasina seeks return to Bangladesh."),
    ("ASIA", "China, Mexico agree a trade working group."),
    ("AFRICA", "Zanzibar hotel fire evacuates 180 tourists."),
    ("WORLD", "UN: wars put food aid for 7.3m more at risk."),
    ("TECH", "Anthropic launches Claude Ship for code review."),
    ("WORLD", "Hacked data: Russian war deaths near 500,000."),
]
F_BRIEF = ImageFont.truetype(FD + "DejaVuSans.ttf", 12)
def brief_col(x, items, y=800):
    for region, text in items:
        d.text((x, y), region, font=F_TAG, fill=RED)
        y = para(x + 104, y, text, F_BRIEF, 376, lh=15)
        y += 5
    return y
brief_col(16, briefs_l)
brief_col(520, briefs_r)

# ---- Footer ----
d.line([16, 972, W - 16, 972], fill=(180, 175, 160), width=1)
d.text((16, 980), "DATE CHECK: every item above is dated 24 November 2026 in its source (SCMP, Japan Times, Times of India,",
       font=F_FOOT, fill=GREY)
d.text((16, 994), "The Daily Edition, Xinhua 0030 GMT summary). Claims in active conflicts are as reported; disputed claims are worded as claims.",
       font=F_FOOT, fill=GREY)
d.text((W - 16, 994), "28 stories", font=F_FOOT, fill=GREY, anchor="ra")

img.save("assets/entry.png", optimize=True)
print("saved assets/entry.png")
