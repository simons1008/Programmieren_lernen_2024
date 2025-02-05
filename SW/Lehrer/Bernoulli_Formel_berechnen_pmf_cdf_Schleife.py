# Bernoulli-Formel berechnen pmf, cdf, Schleife

# Bibliothek importierten
from scipy.stats import binom

print("Wahrscheinlichkeit P(X = k)")
print("Funktion: pmf(k, n, p, loc=0)   Probability mass function")

# Beispiel
k = 1
n = 3
p = 0.25
print(f"k = {k}, n = {n}, p = {p}")
P = binom.pmf(k, n, p)
print("P =", P)
print()

print("Wahrscheinlichkeit P(X <= k)")
print("Funktion: cdf(k, n, p, loc=0)    Cumulative distribution function")

# Beispiel
k = 2
n = 4
p = 0.4
print(f"k = {k}, n = {n}, p = {p}")
P = binom.cdf(k, n, p)
print("P =", P)
print()

print("P für verschiedene n in einer Schleife berechnen")
print("Dazu einen Startwert für n wählen")

# Beispiel
k = 1
n = 10 # Startwert
p = 0.3
while n <= 15:
    P = binom.cdf(k, n, p)
    print(f"k = {k}, n = {n}, p = {p}, P = {P}")
    n += 1

