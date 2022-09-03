# Durcheinander im Wörterbuch Englisch - Deutsch

# Modul für das Durcheinander (Zufall) importieren
import random

# Ein Wörterbucheintrag besteht aus:
# - einem englischen Wort
# - einem deutschen Wort

# Ein englisches Wort ist eins der folgenden:
# - cat
# - dog
# - cow
# - bird
# - sheep
englisch = ["cat", "dog", "cow", "bird", "sheep"]

# Ein deutsches Wort ist eins der folgenden:
# - Katze
# - Hund
# - Kuh
# - Vogel
# - Schaf
deutsch = ["Katze", "Hund", "Kuh", "Vogel", "Schaf"]

# Wörterbucheintrag drucken
print("Stimmt das? " +
      random.choice(englisch) +
      " - " +
      random.choice(deutsch))


