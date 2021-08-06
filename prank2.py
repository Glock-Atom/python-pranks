import winsound
from random import randrange
frequency = randrange(5000)
duration = randrange(5000)
winsound.Beep(frequency, duration)
