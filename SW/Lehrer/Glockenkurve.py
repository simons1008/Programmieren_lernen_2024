# Berechnung der Wahrscheinlichkeiten einer normalverteilten Zufallsgröße X
# Lambacher Schweizer Mathematik Kursstufe Leistungsfach
# Seite 363 Beispiel verallgemeinert

# Bibliothek importierten
# P(X = x):  pdf(x, loc=0, scale=1)
# P(X <= x): cdf(x, loc=0, scale=1)
# loc is mean and scale is standard deviation
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Begrüßung
print("Das Programm berechnet Größen der Glockenkurve und gibt eine Grafik aus.")
# Parameter einlesen
mu_str = input("Erwartungswert mu = ")
sigma_str = input("Standardabweichung sigma = ")

# Parameter umwandeln
mu = float(mu_str)
sigma = float(sigma_str)

# Teilaufgabe a)
print("mu =", mu)
print("sigma =", sigma)
print("2*sigma**2 =", 2*sigma**2)

# Teilaufgabe b)
maximum = stats.norm.pdf(mu, mu, sigma)
wendestelle_1 = stats.norm.pdf(mu-sigma, mu, sigma)
wendestelle_2 = stats.norm.pdf(mu+sigma, mu, sigma)
print("maximum bei mu = {:5.3f} hat den Wert {:5.3f}".format(mu, maximum))
print("wendestelle_1 bei mu-sigma = {:5.3f} den Wert {:5.3f}".format(mu-sigma, wendestelle_1))
print("wendestelle_2 bei mu+sigma = {:5.3f} den Wert {:5.3f}".format(mu+sigma, wendestelle_2))

# Teilaufgabe c) 
# Intervall mu - 3*sigma, mu + 3*sigma, Datentyp: numpy.ndarray
x = np.linspace(mu - 3*sigma, mu + 3*sigma)
# Wahrscheinlichkeitsdichte für die Masse, Datentyp: numpy.ndarray 
phi = stats.norm.pdf(x, mu, sigma)

# Normalverteilung plotten
plt.plot(x, phi)
plt.xlabel("x")
plt.ylabel("phi")
plt.show()
