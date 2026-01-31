import time
from motion.config import *

def stand(pca):
    pca.set_pwm(LEG_LEFT_HIP,  0, SERVO_MID)
    pca.set_pwm(LEG_RIGHT_HIP, 0, SERVO_MID)
    pca.set_pwm(LEG_LEFT_KNEE, 0, SERVO_MID)
    pca.set_pwm(LEG_RIGHT_KNEE,0, SERVO_MID)
    time.sleep(0.5)

def idle(pca):
    pca.set_pwm(HEAD_YAW, 0, SERVO_MID)
