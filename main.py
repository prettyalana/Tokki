from unihiker_k10 import screen, rgb
import time

screen.init(dir=2)

while True:
	
	# RGB LIGHT SHOW
	rgb.write(num=0, R=255, G=192, B=203)  # Pink
	rgb.write(num=1, R=255, G=182, B=193)  # Light pink  
	rgb.write(num=2, R=255, G=105, B=180)  # Hot pink
	
	screen.draw_text(text="Alana",line=0)
	screen.show_draw()
