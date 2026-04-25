from globals import board_I2C
import ssd1306

class OledScreen():
    def __init__(self):        
        self.oled_screen = ssd1306.SSD1306_I2C(128, 64, board_I2C)
      
    def showNormal(self):
        self.oled_screen.fill(0)
        self.oled_screen.text("Teste 01", 0, 0, 1)
        self.oled_screen.show()