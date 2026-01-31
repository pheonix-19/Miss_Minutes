import serial
import time

class PicoDisplay:
    def __init__(self, port, baud=115200):
        try:
            self.ser = serial.Serial(port, baud, timeout=1)
            time.sleep(2)
            print(f"[OK] Connected to Pico on {port}")
        except Exception as e:
            print(f"[ERROR] Could not connect to Pico on {port}: {e}")
            raise

    def show(self, text):
        msg = f"SHOW:{text}\n"
        try:
            written = self.ser.write(msg.encode())
            self.ser.flush()  # Force send immediately
            print(f"[SERIAL] Sent {written} bytes: {msg.strip()}")
        except Exception as e:
            print(f"[ERROR] Failed to send: {e}")
