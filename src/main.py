from globals import *

print("Teste")


def checkValues(mode, gas_value, temperature_value):
  if mode == "glp":
    if gas_value <= GAS_GLP_SAFE:
      if temperature_value >= TEMP_HOT:
        return "HOT"
      return "OK"
    elif GAS_GLP_SAFE < gas_value and gas_value <= GAS_GLP_ALERT:
      if temperature_value <= TEMP_HOT:
        return "ALERT"
      return "OK"
    if temperature_value <= TEMP_HOT:
      return "DNG"
  elif mode == "co":
    if gas_value <= GAS_CO_SAFE:
      return "OK"
    elif GAS_CO_SAFE < gas_value and gas_value <= GAS_CO_ALERT:
      return "ALERT"
    return "DNG"
  return "ERR"


while True:
  # pega informação de temperatura
  temperature_sensor.measure()
  temp_value = temperature_sensor.temperature()

  # pega informação de gás
  gas_value = gas_sensor.read_u16()

  # seleciona qual o modo para ser exibido no display
  if glp_pin.value() == 1:
    mode = "glp"
  elif co_pin.value() == 1:
    mode = "co"

  # checa os resultados baseados no modo e valores lidos
  result = checkValues(mode, gas_value, temp_value)
  if result == "OK":
    oled_screen.showNormal(mode, temp_value)
  elif result == "HOT":
    oled_screen.showHotTempAlert(temp_value)
  elif result == "ALERT":
    oled_screen.showAlert(mode, temp_value)
  elif result == "DNG":
    oled_screen.showDanger()
  else:
    oled_screen.showError()