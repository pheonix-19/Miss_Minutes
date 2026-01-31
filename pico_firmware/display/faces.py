# ---------------- HELPERS ----------------
def eyes(oled, x, y, blink=False, look=0):
    if blink:
        oled.line(x + 8, y + 14, x + 16, y + 14, 1)
        oled.line(x + 34, y + 14, x + 42, y + 14, 1)
        return

    oled.rect(x + 8, y + 10, 8, 8, 1)
    oled.rect(x + 34, y + 10, 8, 8, 1)
    oled.fill_rect(x + 11 + look*2, y + 13, 2, 2, 1)
    oled.fill_rect(x + 37 + look*2, y + 13, 2, 2, 1)


def mouth(oled, x, y, level):
    if level == 0:
        oled.line(x, y, x+18, y, 1)
    elif level == 1:
        oled.rect(x, y, 18, 4, 1)
    elif level == 2:
        oled.rect(x, y, 18, 6, 1)
    else:
        oled.rect(x, y, 18, 8, 1)


def speaking_waves(oled, x, y, tick):
    phase = tick % 6
    # Simple radiating lines instead of arc (arc not supported)
    oled.line(x + 24 + phase, y + 34, x + 30 + phase, y + 34, 1)
    oled.line(x + 24 + phase, y + 42, x + 32 + phase, y + 42, 1)
    oled.line(x + 26 + phase, y + 36, x + 32 + phase, y + 38, 1)
    oled.line(x + 26 + phase, y + 40, x + 32 + phase, y + 38, 1)


def listening_waves(oled, x, y, tick):
    if tick % 10 < 5:
        oled.line(x - 6, y + 20, x - 2, y + 20, 1)
        oled.line(x + 52, y + 20, x + 56, y + 20, 1)


# ---------------- FACES ----------------
def draw_happy_face(oled, x=35, y=15, **k):
    breathe = k["tick"] % 4
    oled.rect(x, y + breathe//2, 50, 50, 1)
    eyes(oled, x, y, k["blink"], k["look"])

    oled.fill_rect(x + 6, y + 28, 4, 2, 1)
    oled.fill_rect(x + 40, y + 28, 4, 2, 1)

    mouth(oled, x + 16, y + 34, k["mouth_level"])

    if k["speaking"]:
        speaking_waves(oled, x, y, k["tick"])
    else:
        listening_waves(oled, x, y, k["tick"])


def draw_sad_face(oled, x=35, y=15, **k):
    oled.rect(x, y, 50, 50, 1)
    eyes(oled, x, y, k["blink"], k["look"])
    mouth(oled, x + 16, y + 38, 0)

    if k["tick"] % 12 < 6:
        oled.pixel(x + 12, y + 22, 1)

    listening_waves(oled, x, y, k["tick"])


def draw_angry_face(oled, x=35, y=15, **k):
    oled.rect(x, y, 50, 50, 1)
    oled.line(x + 6, y + 10, x + 18, y + 18, 1)
    oled.line(x + 44, y + 10, x + 32, y + 18, 1)

    eyes(oled, x, y, k["blink"], k["look"])
    mouth(oled, x + 16, y + 38, k["mouth_level"])

    if k["speaking"]:
        speaking_waves(oled, x, y, k["tick"])


def draw_excited_face(oled, x=35, y=15, **k):
    oled.rect(x, y, 50, 50, 1)

    oled.rect(x + 6, y + 8, 10, 10, 1)
    oled.rect(x + 34, y + 8, 10, 10, 1)
    oled.fill_rect(x + 10, y + 12, 2, 2, 1)
    oled.fill_rect(x + 38, y + 12, 2, 2, 1)

    mouth(oled, x + 16, y + 32, k["mouth_level"])
    speaking_waves(oled, x, y, k["tick"])


def draw_neutral_face(oled, x=35, y=15, **k):
    oled.rect(x, y, 50, 50, 1)
    eyes(oled, x, y, k["blink"], k["look"])
    mouth(oled, x + 16, y + 38, 0)

    listening_waves(oled, x, y, k["tick"])


FACE_FUNCS = {
    "HAPPY": draw_happy_face,
    "SAD": draw_sad_face,
    "ANGRY": draw_angry_face,
    "EXCITED": draw_excited_face,
    "NEUTRAL": draw_neutral_face,
}
