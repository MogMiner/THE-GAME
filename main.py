import time
import random
import turtle
from pygame import mixer
pat=turtle.Turtle()
mixer.init()
mixer.music.load('song.mp3')
print("music started playing....")
mixer.music.set_volume(0.2)
mixer.music.play()
