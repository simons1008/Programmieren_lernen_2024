from neotimer_win import Neotimer

print("Start")
blinker = Neotimer(1000)

while True:
    if blinker.repeat_execution_times(10):
        print("Toggle")
        print(blinker.repetitions)
