from unihiker_k10 import screen,camera,tf_card
from unihiker_k10 import temp_humi,light,acce
from unihiker_k10 import rgb,button
from unihiker_k10 import mic,speaker
import time

class Tokki:
    def __init__(self, name="Tokki 토끼"):
        self.name = name
        self.happiness = 50
        self.hunger = 50
        self.clean = 50
        self.health = 100
        
    def display(self):
        screen.clear()
        screen.draw_text(self.name, line=0)
        screen.show_draw()
        
    def play(self):
        self.happiness += 10
        self.hunger += 5
        self.clean -= 5
    
    def eat(self):
        self.hunger -= 10
    
    def bathe(self):
        self.clean += 10
            
    def sick(self):
        pass
            
        
def main():
    
    # Initialize screen 
    screen.init(dir=2)
    
    # Draw Tokki
    tokki = Tokki() 
    tokki.display()
    
    # Pretty pink lights!
    rgb.write(num=0, R=255, G=192, B=203)  # Pink
    rgb.write(num=1, R=255, G=182, B=193)  # Light pink  
    rgb.write(num=2, R=255, G=105, B=180)  # Hot pink
    
    # Play startup sound
    speaker.play_tf_music("music.wav")
    
    while True:
        time.sleep(1)

if __name__ == "__main__": 
    main()