from unihiker_k10 import screen, speaker, rgb
import time

# Initialize
screen.init(dir=2)

# Show Tokki is alive!
screen.draw_text(text="Alana", line=0)
screen.show_draw()

# Pretty pink lights!
rgb.write(num=0, R=255, G=192, B=203)  # Pink
rgb.write(num=1, R=255, G=182, B=193)  # Light pink  
rgb.write(num=2, R=255, G=105, B=180)  # Hot pink

# Play music
speaker.play_tf_music("music.wav")