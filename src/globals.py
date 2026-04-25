from machine import Pin, I2C, ADC
import dht

# configuração do i2c da placa
board_I2C = I2C(0, scl=Pin(22), sda=Pin(21))

# sensor de gás
gas_sensor = ADC(Pin(34))

# tela
from screen import OledScreen
oled_screen = OledScreen()