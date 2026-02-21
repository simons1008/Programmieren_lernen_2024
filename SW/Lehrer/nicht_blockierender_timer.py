# Nicht blockierender Timer
# Quelle: https://stackoverflow.com/questions/68444195/how-to-make-non-blocking-timer-in-python

import time

t0 = time.time() # Return the current time in seconds since the Epoch
t1 = time.time() 
while (t1 - t0) < 1:
    print("Timer läuft ...")
    t1 = time.time()
