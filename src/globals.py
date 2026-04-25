from machine import Pin, I2C
import dht

# configuração do i2c da placa
board_I2C = I2C(0, scl=Pin(4), sda=Pin(5))

# tela
from screen import OledScreen
oled_screen = OledScreen()