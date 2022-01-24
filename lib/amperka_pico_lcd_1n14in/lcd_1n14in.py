from machine import Pin, SPI, PWM
import framebuf

PIN_BL = 13
PIN_DC = 8
PIN_RST = 12
PIN_MOSI = 11
PIN_SCK = 10
PIN_CS = 9

PIN_KEY0 = 15
PIN_KEY1 = 17
PIN_KEY2 = 2
PIN_KEY3 = 3

pwm = PWM(Pin(PIN_BL))
pwm.freq(1000)


class LCD_1n14in(framebuf.FrameBuffer):
    def __init__(self):
        self.width = 240
        self.height = 135

        self.cs = Pin(PIN_CS, Pin.OUT)
        self.rst = Pin(PIN_RST, Pin.OUT)

        self.cs(1)
        self.spi = SPI(1)
        self.spi = SPI(1, 1000_000)
        self.spi = SPI(1, 10000_000, polarity=0, phase=0,
                       sck=Pin(PIN_SCK), mosi=Pin(PIN_MOSI), miso=None)
        self.dc = Pin(PIN_DC, Pin.OUT)
        self.dc(1)
        self.buffer = bytearray(self.height * self.width * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.init_display()

        self.red = 0x07E0
        self.green = 0x001f
        self.blue = 0xf800
        self.white = 0xffff

        self.key0 = Pin(PIN_KEY0, Pin.IN)
        self.key1 = Pin(PIN_KEY1, Pin.IN)
        self.key2 = Pin(PIN_KEY2, Pin.IN)
        self.key3 = Pin(PIN_KEY3, Pin.IN)

    def _write_cmd(self, cmd):
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def _write_data(self, buf):
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(bytearray([buf]))
        self.cs(1)

    def init_display(self):
        """Initialize dispaly"""
        self.rst(1)
        self.rst(0)
        self.rst(1)

        self._write_cmd(0x36)
        self._write_data(0x70)

        self._write_cmd(0x3A)
        self._write_data(0x05)

        self._write_cmd(0xB2)
        self._write_data(0x0C)
        self._write_data(0x0C)
        self._write_data(0x00)
        self._write_data(0x33)
        self._write_data(0x33)

        self._write_cmd(0xB7)
        self._write_data(0x35)

        self._write_cmd(0xBB)
        self._write_data(0x19)

        self._write_cmd(0xC0)
        self._write_data(0x2C)

        self._write_cmd(0xC2)
        self._write_data(0x01)

        self._write_cmd(0xC3)
        self._write_data(0x12)

        self._write_cmd(0xC4)
        self._write_data(0x20)

        self._write_cmd(0xC6)
        self._write_data(0x0F)

        self._write_cmd(0xD0)
        self._write_data(0xA4)
        self._write_data(0xA1)

        self._write_cmd(0xE0)
        self._write_data(0xD0)
        self._write_data(0x04)
        self._write_data(0x0D)
        self._write_data(0x11)
        self._write_data(0x13)
        self._write_data(0x2B)
        self._write_data(0x3F)
        self._write_data(0x54)
        self._write_data(0x4C)
        self._write_data(0x18)
        self._write_data(0x0D)
        self._write_data(0x0B)
        self._write_data(0x1F)
        self._write_data(0x23)

        self._write_cmd(0xE1)
        self._write_data(0xD0)
        self._write_data(0x04)
        self._write_data(0x0C)
        self._write_data(0x11)
        self._write_data(0x13)
        self._write_data(0x2C)
        self._write_data(0x3F)
        self._write_data(0x44)
        self._write_data(0x51)
        self._write_data(0x2F)
        self._write_data(0x1F)
        self._write_data(0x1F)
        self._write_data(0x20)
        self._write_data(0x23)

        self._write_cmd(0x21)

        self._write_cmd(0x11)

        self._write_cmd(0x29)

    def show(self):
        self._write_cmd(0x2A)
        self._write_data(0x00)
        self._write_data(0x28)
        self._write_data(0x01)
        self._write_data(0x17)

        self._write_cmd(0x2B)
        self._write_data(0x00)
        self._write_data(0x35)
        self._write_data(0x00)
        self._write_data(0xBB)

        self._write_cmd(0x2C)

        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(self.buffer)
        self.cs(1)

    def set_brightness(self, brightness):
        pwm.duty_u16(brightness)

