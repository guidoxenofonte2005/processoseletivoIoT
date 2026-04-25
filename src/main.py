from globals import *
import utime

print("Teste")


def checkValues(mode, gas_value, temperature_value):
  """
  Avalia os valores lidos dos sensores e retorna o estado atual do sistema.

  Estados possíveis:
    OK    — gás seguro e temperatura normal
    HOT   — gás seguro, mas temperatura acima do limite
    ALERT — concentração de gás em nível intermediário
    DNG   — concentração de gás em nível de perigo
    ERR   — modo inválido (nenhum switch ativo)
  """
  if mode == "glp":
    if gas_value <= GAS_GLP_SAFE:
      # Gás seguro — verifica se a temperatura está elevada
      if temperature_value >= TEMP_HOT:
        return "HOT"
      return "OK"
    elif GAS_GLP_SAFE < gas_value and gas_value <= GAS_GLP_ALERT:
      # Gás em nível intermediário — verifica temperatura antes de alertar
      if temperature_value <= TEMP_HOT:
        return "ALERT"
      return "OK"
    # Gás acima do limite de alerta — perigo imediato
    if temperature_value <= TEMP_HOT:
      return "DNG"
  elif mode == "co":
    if gas_value <= GAS_CO_SAFE:
      return "OK"
    elif GAS_CO_SAFE < gas_value and gas_value <= GAS_CO_ALERT:
      return "ALERT"
    # Gás acima do limite de alerta — perigo imediato
    return "DNG"
  # Nenhum modo reconhecido
  return "ERR"


while True:
  # Leitura dos sensores
  temperature_sensor.measure()
  temp_value = temperature_sensor.temperature()
  gas_value = gas_sensor.read_u16()

  # Seleciona qual o modo ativo (GLP/CO)
  if glp_pin.value() == 1:
    mode = "glp"
  elif co_pin.value() == 1:
    mode = "co"

  # Avalia os valores e aciona o atuador e display correspondentes
  result = checkValues(mode, gas_value, temp_value)
  if result == "OK":
    buzzer_pin.deinit()
    oled_screen.showNormal(mode, temp_value)
  elif result == "HOT":
    buzzer_pin.deinit()
    oled_screen.showHotTempAlert(temp_value)
  elif result == "ALERT":
    buzzer_pin.deinit()
    oled_screen.showAlert(mode, temp_value)
  elif result == "DNG":
    buzzer_pin.init()
    oled_screen.showDanger()
  else:
    buzzer_pin.init()
    oled_screen.showError()
  
  utime.sleep_ms(2000)