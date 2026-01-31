import time
from motion.config import *

def step_left(pca):
    pca.set_pwm(LEG_LEFT_HIP, 0, SERVO_MIN)
    pca.set_pwm(LEG_RIGHT_HIP,0, SERVO_MAX)
    time.sleep(0.4)

def step_right(pca):
    pca.set_pwm(LEG_RIGHT_HIP,0, SERVO_MIN)
    pca.set_pwm(LEG_LEFT_HIP, 0, SERVO_MAX)
    time.sleep(0.4)

def walk_forward(pca, steps=3):
    for _ in range(steps):
        step_left(pca)
        step_right(pca)

    # Return to neutral
    pca.set_pwm(LEG_LEFT_HIP, 0, SERVO_MID)
    pca.set_pwm(LEG_RIGHT_HIP,0, SERVO_MID)
