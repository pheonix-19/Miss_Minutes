import time
from motion.config import *

def handshake(pca):
    # Raise arm
    pca.set_pwm(ARM_RIGHT, 0, SERVO_MIN)
    time.sleep(0.5)

    # Shake motion
    for _ in range(3):
        pca.set_pwm(ARM_RIGHT, 0, SERVO_MAX)
        time.sleep(0.3)
        pca.set_pwm(ARM_RIGHT, 0, SERVO_MIN)
        time.sleep(0.3)

    # Back to rest
    pca.set_pwm(ARM_RIGHT, 0, SERVO_MID)
