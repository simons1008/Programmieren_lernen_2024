from neotimer_win import *

mytimer = Neotimer(1000)

while True:
    if mytimer.repeat_execution():
        print(ticks_ms())
    
