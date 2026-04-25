from globals import board_I2C
import ssd1306

class OledScreen():
  def __init__(self):        
    self.oled_screen = ssd1306.SSD1306_I2C(128, 64, board_I2C)
      
  def showNormal(self, current_mode, temperature_value=0):
    self.oled_screen.fill(0)
    self.oled_screen.text(f"GAS: Normal", 0, 0, 1)
    if current_mode.upper() == "GLP":
      self.oled_screen.text(f"Temp.: {str(temperature_value)}C", 0, 36, 1)
    self.oled_screen.show()
    
  def showAlert(self, current_mode, temperature_value=0):
    self.oled_screen.fill(0)
    self.oled_screen.text("GAS DETECTADO", 0, 0, 1)
    self.oled_screen.text("VERIFIQUE AS", 0, 10, 1)
    self.oled_screen.text("SAIDAS DE GAS", 0, 20, 1)
    if current_mode.upper() == "GLP":
      self.oled_screen.text(f"Temp: {str(temperature_value)}C", 0, 36, 1)
    self.oled_screen.show()
    
  def showHotTempAlert(self, temperature_value=0):
    self.oled_screen.fill(0)
    self.oled_screen.text("Gas: Normal", 0, 0, 1)
    self.oled_screen.text(f"Temp. ALTA:", 0, 36, 1)
    self.oled_screen.text(f"{str(temperature_value)}C", 0, 46, 1)
    self.oled_screen.show()
    
  def showDanger(self):
    self.oled_screen.fill(0)
    self.oled_screen.text("PERIGO!!!!", 0, 0, 1)
    self.oled_screen.text(f"GAS DETECTADO EM", 0, 10, 1)
    self.oled_screen.text(f"GRANDE VOLUME!", 0, 20, 1)
    self.oled_screen.show()
    
  def showError(self):
    self.oled_screen.fill(0)
    self.oled_screen.text("Houve um erro", 0, 0, 1)
    self.oled_screen.text("ao checar os", 0, 10, 1)
    self.oled_screen.text("sensores...", 0, 20, 1)
    self.oled_screen.show()