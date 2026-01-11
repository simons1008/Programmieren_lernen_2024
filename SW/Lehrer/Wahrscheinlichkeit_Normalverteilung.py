# Berechnung der Wahrscheinlichkeiten einer normalverteilten Zufallsgröße X
# Lambacher Schweizer Mathematik Kursstufe Leistungsfach
# Seite 363 Beispiel 1 und Seite 364 Beispiel 2

# Bibliothek importierten
# P(X = x):  pdf(x, loc=0, scale=1)
# P(X <= x): cdf(x, loc=0, scale=1)
# loc is mean and scale is standard deviation
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Seite 363 Beispiel 1
"""
Gegeben: Brötchen haben eine Masse die normalverteil ist mit mu = 73 und sigma = 6. 
Gesucht a): Wahrscheinlichkeit, dass ein Brötchen wenige als 70 g hat
Wahrscheinlichkeit, dass ein Brötchen auf Gramm gerundet 75 g hat
Wahrscheinlichkeit, dass ein Brötchen exakt 50 g hat
Gesucht b): n = 200 Wahrscheinlichkeit, dass weniger als 50 Brötchen weniger als 70 g haben 
"""
print("\nBeispiel 1")
mu = 73
sigma = 6
print("Erwartungswert mu =", mu)
print("Standardabweichung sigma =", sigma)

# Teilaufgabe a)
# P(X <= 70)
ergebnis_70 = stats.norm.cdf(70, mu, sigma)
print("Wahrscheinlichkeit für Masse weniger als 70 g = {:5.3f}".format(ergebnis_70))
 
# P(74.5 <= X < 75.5)
ergebnis = stats.norm.cdf(75.5, mu, sigma) - stats.norm.cdf(74.5, mu, sigma)
print("Wahrscheinlichkeit für Masse auf Gramm gerundet 75 g = {:5.3f}".format(ergebnis))

# P(X = 75)
# Bei der Normalverteilung gilt: P(X = a) = 0
ergebnis = 0
print("Wahrscheinlichkeit für Masse exakt 75 g = {}".format(ergebnis))

# Masse des Brötchens - 50 Werte im gleichen Abstand im 
# Intervall mu - 3*sigma, mu + 3*sigma, Datentyp: numpy.ndarray
x = np.linspace(mu - 3*sigma, mu + 3*sigma)
# Wahrscheinlichkeitsdichte für die Masse, Datentyp: numpy.ndarray 
phi = stats.norm.pdf(x, mu, sigma)

# Teilaufgabe b) 
# Binomialverteilung berechnen
k = 49
n = 200
p = ergebnis_70 # aus Teilaufgabe a)
ergebnis = stats.binom.cdf(k, n, p)
print("Wahrscheinlichkeit für weniger als 50 Brötchen leichter als 70 g = {:5.3f}".format(ergebnis)) 

# Normalverteilung plotten
plt.plot(x, phi)
plt.xlabel("Masse des Brötchens")
plt.ylabel("Wahrscheinlichkeitsdichte")
plt.show()

# Seite 364 Beispiel 2
print("\nBeispiel 2")
"""
Gegeben: Tabelle mit Körpergrößen
Gesucht: a) Warum kann man Normalverteilung annehmen?
b) mit dem WTR mu und sigma ermitteln
c) P(X <= 170) und die relative Häufigkeit für X <= 170
"""
# Körpergrößen
samples = [165, 168, 169, 169, 169, 170, 170, 170, 172, 172, 172, 172, 172, \
           172, 172, 174, 174, 174, 174, 175, 175, 175, 177, 179, 179]
anzahl = len(samples)
print("Anzahl der Spielerinnen =", anzahl)

# Teilaufgabe a) 
"""
Bei 172 ist ein Maximum erkennbar. Die weiteren Daten liegen näherungsweise symmetrisch um diesen Wert und werden mit zunehmendem Abstand zur Maximumstelle kleiner. 
"""

# Teilaufgabe b)
# mu und sigma der Normalverteilung berechnen
mu, sigma = stats.norm.fit(samples, method="MLE")
print("Erwartungswert mu = {:5.3f}".format(mu))
print("Standardabweichung sigma = {:5.3f}".format(sigma))

# Teilaufgabe c)
ergebnis = stats.norm.cdf(170, mu, sigma)
print("Wahrscheinlichkeit für Körpergröße kleiner 170 = {:5.3f}".format(ergebnis))

# Histogramm berechnen
counts, bins = np.histogram(samples, bins = 14)
print("counts =", counts)
print("bins =", bins)
# relative Häufigkeit berechnen
# Index 4 enthält die Summe der Anzahlen < 170
ergebnis = counts.cumsum()[4]/anzahl 
print("Relative Häufigkeit der Körpergröße kleiner 170 = {:5.3f}".format(ergebnis))

# Körpergröße - 50 Werte im gleichen Abstand im 
# Intervall mu - 3*sigma, mu + 3*sigma, Datentyp: numpy.ndarray
x = np.linspace(mu - 3*sigma, mu + 3*sigma)
# Wahrscheinlichkeitsdichte für die Masse, Datentyp: numpy.ndarray 
phi = stats.norm.pdf(x, mu, sigma)

# Normalverteilung plotten
plt.plot(x, phi)
# relative Häufigkeit plotten
plt.stairs(counts/anzahl, bins) 
plt.xlabel("Körpergröße")
plt.ylabel("Wahrscheinlichkeitsdichte")
plt.show()

# Ende
input("Weiter? ")
