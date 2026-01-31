from robot_link.serial_comm import PicoDisplay
import time

# CHANGE PORT NAME
try:
    pico = PicoDisplay(port="COM5")  # Windows: COM5
    # pico = PicoDisplay(port="/dev/ttyACM0")  # Linux
    
    pico.show("HELLO")
    time.sleep(2)
    
    pico.show("LISTENING")
    time.sleep(2)
    
    pico.show("CONNECTED")
    
except Exception as e:
    print(f"[ERROR] Could not connect to Pico on COM5: {e}")
    print("Make sure:")
    print("  1. Pico is connected via USB")
    print("  2. Check Device Manager for the correct COM port")
    print("  3. Update the port in test_pico_display.py")
