from globals import *

print("Teste")

while True:
  # pega informação de gás
  gas_value = gas_sensor.read_u16()

  oled_screen.showNormal(gas_value)