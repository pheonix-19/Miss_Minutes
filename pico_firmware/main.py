from machine import Pin, I2C
from display.ssh1106 import SSH1106_I2C
from display.faces import FACE_FUNCS
import sys, select, time

try:
    import usb_cdc
except ImportError:
    usb_cdc = None


# ---------------- I2C INIT ----------------
i2c = None
try:
    i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)
    time.sleep(0.1)
    print("[PICO] I2C initialized")
except Exception as e:
    print("[ERROR] I2C init failed:", e)


# ---------------- OLED INIT ----------------
oled = None
if i2c:
    for addr in (0x3C, 0x3D):
        try:
            oled = SSH1106_I2C(128, 64, i2c, addr=addr)
            break
        except:
            pass


# ---------------- HUD ----------------
def draw_hud(oled, command, emotion, speaking):
    oled.text("CMD:", 0, 0)
    oled.text(command or "--", 30, 0)
    oled.text("EMO:", 0, 10)
    oled.text(emotion or "--", 30, 10)
    oled.text("SPK" if speaking else "LST", 100, 0)


# ---------------- USB SERIAL ----------------
data_serial = None
if usb_cdc and usb_cdc.data:
    data_serial = usb_cdc.data
    data_serial.timeout = 0
else:
    poll = select.poll()
    poll.register(sys.stdin, select.POLLIN)


# ---------------- STATE ----------------
command = ""
emotion = ""
timeout_counter = 0
speaking_ticks = 0
heartbeat = 0

blink_timer = 0
blink = False


# ================== MAIN LOOP ==================
while True:
    try:
        got_data = False

        if data_serial:
            raw = data_serial.readline()
            if raw:
                data = raw.decode().strip()
                got_data = True
        else:
            if poll.poll(0):
                data = sys.stdin.readline().strip()
                got_data = True

        if got_data and data.startswith("SHOW:"):
            data = data.replace("SHOW:", "")
            if "(" in data and ")" in data:
                cmd, emo = data.split("(")
                command = cmd.strip()[:12]
                emotion = emo.replace(")", "").strip()[:10]
            else:
                command = data[:12]
                emotion = ""

            timeout_counter = 0
            speaking_ticks = 50

        # ---------- animation state ----------
        blink_timer += 1
        if blink_timer > 30:
            blink = not blink
            if not blink:
                blink_timer = 0

        look = [-1, 0, 1][heartbeat % 3]
        mouth_level = speaking_ticks % 4 if speaking_ticks > 0 else 0
        speaking = speaking_ticks > 0

        face_x = 35 + (heartbeat % 3 - 1)
        face_y = 15 + (heartbeat % 2)

        if speaking_ticks > 0:
            speaking_ticks -= 1

        # ---------- display ----------
        if oled:
            oled.fill(0)
            draw_hud(oled, command, emotion, speaking)

            face = FACE_FUNCS.get(emotion.upper(), FACE_FUNCS["NEUTRAL"])
            face(
                oled,
                x=face_x,
                y=face_y,
                mouth_level=mouth_level,
                blink=blink,
                look=look,
                tick=heartbeat,
                speaking=speaking
            )
            oled.show()

        heartbeat += 1
        time.sleep(0.1)

    except Exception as e:
        print("[ERROR]", e)
        time.sleep(1)
