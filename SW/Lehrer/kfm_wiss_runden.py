# Programm vergleicht das kaufmännische Runden mit dem wissenschaftlichen Runden
# Zitat aus https://docs.python.org/3/library/functions.html#round
# "... if two multiples are equally close, rounding is done toward the even choice
# (so, for example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2)."

# Beispiel
radius = 41
distance = radius/10
# Überschrift
print("i  orig  kfm  wiss")
# Faktoren
factors = [0, 3, 5, 7, 9]

# Tabelle drucken
for i in factors:
    orig = distance * i
    kfm = int(orig + 0.5)
    wiss = round(orig)
    print(f"{i}  {orig:4.1f}   {kfm:2d}    {wiss:2d}")
