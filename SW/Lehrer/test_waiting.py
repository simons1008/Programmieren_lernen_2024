from neotimer_win import *

print("Start")
myTimer = Neotimer(500)
myTimer.start()

myTimer.start()

while myTimer.waiting():
    print('.')

print("Stop")
