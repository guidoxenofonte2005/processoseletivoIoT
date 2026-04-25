from machine import Pin, I2C, ADC, PWM
import dht

# CONFIGURAÇÃO DO I2C DA PLACA
board_I2C = I2C(0, scl=Pin(22), sda=Pin(21))

# SENSOR DE TEMPERATURA/UMIDADE
temperature_sensor = dht.DHT22(Pin(23))

# SENSOR DE GÁS
gas_sensor = ADC(Pin(34))

# PINOS SELETORES DE MODO
glp_pin = Pin(17, Pin.IN, Pin.PULL_DOWN)
co_pin = Pin(16, Pin.IN, Pin.PULL_DOWN)

# BUZZER
buzzer_pin = PWM(Pin(19), freq=437, duty_u16=32768)
buzzer_pin.deinit()

# TELA OLED 128x64
from screen import OledScreen
oled_screen = OledScreen()

# LIMITES
# Limite de monóxido de carbono
GAS_CO_SAFE = 40793
GAS_CO_ALERT = 48523
GAS_CO_DANGER = 55965

# Limite de gás cozinha
GAS_GLP_SAFE = 55965
GAS_GLP_ALERT = 60206
GAS_GLP_DANGER = 62671

# Limite de temperatura
TEMP_HOT = 45.0