from machine import Pin, I2C, ADC, PWM
import dht

# configuração do i2c da placa
board_I2C = I2C(0, scl=Pin(22), sda=Pin(21))

# sensor de temperatura
temperature_sensor = dht.DHT22(Pin(23))

# sensor de gás
gas_sensor = ADC(Pin(34))

# pinos seletores de modo
glp_pin = Pin(17, Pin.IN, Pin.PULL_DOWN)
co_pin = Pin(16, Pin.IN, Pin.PULL_DOWN)

# buzzer
buzzer_pin = PWM(Pin(19), freq=437, duty_u16=32768)
buzzer_pin.deinit()

# tela
from screen import OledScreen
oled_screen = OledScreen()

# limites
GAS_CO_SAFE = 40793
GAS_CO_ALERT = 48523
GAS_CO_DANGER = 55965

GAS_GLP_SAFE = 55965
GAS_GLP_ALERT = 60206
GAS_GLP_DANGER = 62671

TEMP_HOT = 45.0