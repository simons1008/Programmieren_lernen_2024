# Berechnung der Wahrscheinlichkeiten einer binomialverteilten Zufallsgröße X
# Lambacher Schweizer Mathematik Kursstufe Leistungsfach
# Seite 313 Beispiele 1 und 2

# Bibliotheken importierten
# P(X = k):  pmf(k, n, p, loc=0)
# P(X <= k): cdf(k, n, p, loc=0)
import matplotlib.pyplot as plt
import math as m
import numpy as np
from scipy.stats import binom

# Seite 317 Beispiel 1
""" 
Gegeben: Ein Glücksrad mit 5 Sektoren wird achtmal gedreht. 
Die Zufallsvariable X gibt an, wie oft 'Rot' erscheint. 
Gesucht: Erwartungswert von X, Wahrscheinlichkeitsverteilung,
Histogramm
""" 
print("\nBeispiel 1")
n = 8
p = 1/5
print("Anzahl der Drehungen n =", n)
print("Trefferwahrscheinlichkeit p =", p)
# Erwartungswert berechen
E = n * p
print("Erwartungswert E =", E)

# Anzahl 'Rot', Datentyp: numpy.ndarray
X = np.arange(n+1)
# Wahrscheinlichkeit für genau X-mal 'Rot', Datentyp: numpy.ndarray
P = binom.pmf(X, n, p)

# Tabelle drucken
print("Wahrscheinlichkeitsverteilung")
print("X     P")
for x, p in zip(X, P):
    print("{:5.3f} {:5.3f}".format(x, p))

# Histogramm plotten
plt.bar(X, P, width=1)
plt.xlabel("Anzahl 'Rot'")
plt.ylabel("Wahrscheinlichkeit")
plt.show()
             
# Seite 317 Beispiel 2
"""
Gegeben: Zwiebeln mit Keimwahrscheinlicheit 0.85, n = 130
Die Zufallsvariable X gibt die Anzahl der Zwiebeln an, die keimen.
P_sigma_rule = 0.683 für sigma > 3
Gesucht: Wahrscheinlichkeit des sigma-Intervalls P_sigma,
Verhältnis P_sigma_rule/ P_sigma
"""
print("\nBeispiel 2")
n = 130
p = 0.85
P_sigma_rule = 0.683
print("Anzahl der Pflanzungen n =", n)
print("Keimwahrscheinlichkeit p =", p)
print("Wahrscheinlichkeit gemäß Sigma-Regel P_sigma_rule =", P_sigma_rule)
# Erwartungswert berechen
E = n * p
print("Erwartungswert E =", E)
# Standardabweichung berechnen
sigma = m.sqrt(n * p * (1-p))
print("Standardabweichung sigma = {:5.3f}".format(sigma))
# Sigma-Intervall bestimmen
sigma_lo = E - sigma
sigma_hi = E + sigma
print("Sigma Intervall {:5.3f} {:5.3f}".format(sigma_lo, sigma_hi))
# zur Berechnung der Wahrscheinlichkeit benötigt man Integerwerte
print("Sigma Intervall Integerwerte", m.ceil(sigma_lo), m.floor(sigma_hi))

# Wahrscheinlichkeit bestimmen, dass X im Sigma-Intervall liegt
# P(sigma_lo <= X <= sigma_hi)
# Integerwerte verwenden
P_sigma = binom.cdf(m.floor(sigma_hi), n, p) - binom.cdf(m.ceil(sigma_lo) - 1, n, p)
print("Wahrscheinlichkeit des sigma-Intervalls P_sigma = {:5.3f}".format(P_sigma))
# Verhältnis P_sigma_rule/ P_sigma
ratio = P_sigma_rule/P_sigma
print("Verhältnis P_sigma_rule/ P_sigma = {:5.3f}".format(ratio))

# Ende
input("Weiter? ")
