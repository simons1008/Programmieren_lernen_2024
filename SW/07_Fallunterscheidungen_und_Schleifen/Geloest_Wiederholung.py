#
# Python - Wiederholung
#

# Erstelle eine Variable
# - die eine Zahl enthält
# - die einen Text enthält
meine_zahl = 12
mein_text = "Hallo Programmierkurs!"

# Erstelle eine Liste mit 3 Vornamen
meine_liste = ["Emilia", "Rowena", "Xaver"]

# Erstelle ein Dictionary mit 3 Einträgen Englisch - Deutsch
englisch_deutsch = {"cat": "Katze", "mouse": "Maus", "rat": "Ratte"}

# Der Computer soll nach deinem Namen fragen und einen Text mit deinem Namen ausgeben
mein_name = input("Wie heißt du? ")
print("Hallo", mein_name)

# Der Computer soll nach einer Zahl fragen und ausgeben
# - die Zahl ist größer als 10 
#     oder 
# - die Zahl ist kleiner oder gleich 10
meine_zahl = input("Nenne eine Zahl: ")
meine_zahl = float(meine_zahl)
if meine_zahl > 10:
    print("Die Zahl ist größer als 10")
else:
    print("Die Zahl ist kleiner oder gleich 10")

# Programmiere eine While-Schleife
# - die zehnmal die Zahl 10 ausgibt
# - die die Zahlen 1 bis 10 ausgibt
i = 0
while i < 10:
    print("10")
    i = i + 1

i = 1
while i <= 10:
    print(i)
    i = i + 1


