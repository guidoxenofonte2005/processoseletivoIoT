from globals import *

print("Teste")

while True:
  # pega informação de temperatura
  temperature_sensor.measure()
  temp_value = temperature_sensor.temperature()

  # pega informação de gás
  gas_value = gas_sensor.read_u16()

  oled_screen.showNormal(temp_value, gas_value)