from machine import I2C
import time

class PCA9685:
    def __init__(self, i2c, address=0x40):
        self.i2c = i2c
        self.address = address
        self.reset()

    def reset(self):
        self.i2c.writeto_mem(self.address, 0x00, b'\x00')
        time.sleep(0.01)

    def set_pwm_freq(self, freq_hz):
        prescaleval = 25000000.0
        prescaleval /= 4096.0
        prescaleval /= float(freq_hz)
        prescaleval -= 1.0
        prescale = int(prescaleval + 0.5)

        oldmode = self.i2c.readfrom_mem(self.address, 0x00, 1)
        newmode = (oldmode[0] & 0x7F) | 0x10
        self.i2c.writeto_mem(self.address, 0x00, bytes([newmode]))
        self.i2c.writeto_mem(self.address, 0xFE, bytes([prescale]))
        self.i2c.writeto_mem(self.address, 0x00, oldmode)
        time.sleep(0.005)
        self.i2c.writeto_mem(self.address, 0x00, bytes([oldmode[0] | 0x80]))

    def set_pwm(self, channel, on, off):
        self.i2c.writeto_mem(
            self.address,
            0x06 + 4 * channel,
            bytes([on & 0xFF, on >> 8, off & 0xFF, off >> 8])
        )
