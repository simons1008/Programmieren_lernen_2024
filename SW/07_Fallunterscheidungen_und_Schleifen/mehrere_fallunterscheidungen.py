# Funktionen mit Fallunterscheidungren - unterschiedliches Verhalten
# Quellen:
# https://stackoverflow.com/questions/11479816/what-is-the-python-equivalent-for-a-case-switch-statement
# https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching

# Ausschließliche Abfrage!
# Es wird 1. Zweig mit einer gültigen Bedingung ausgeführt
# Was passiert wenn sich die Besdingungen überlappen?
# Input der Funktion ist eine Zahl
def beispiel_mit_elif(x):
    if x > 0:
        print('positive')
    elif x < 0:
        print('negative')
    elif x == -15: # keine ausschließliche Bedingung!
        print('special case!')
    else:
        print('zero')

# Mehrere Abfragen.
# Es werden alle Zweige mit einer gültigen Bedingung ausgeführt. 
# Input der Funktion ist eine Zahl
def beispiel_mit_if(x):
    if x > 0:
        print('positive')
    if x < 0:
        print('negative')
    if x == -15:
        print('special case!')
    if x == 0:
        print('zero')

# Passendes Muster finden
# Es wird der 1. Zweig mit einem passenden Muster ausgeführt
# Input der Funktion ist eine Zahl oder eine Zeichenkette
def beispiel_mit_match_case(x):
    match x:
        case 23:
            print('23')
        case -3:
            print('-3')
        case -15:
            print('-15')
        case 0:
            print('0')
        case "Hallo":
            print("Hallo") 
        case _:
            print('unknown pattern')

# Passendes Muster finden
# Es wird der 1. Zweig mit einem passenden Muster ausgeführt
# point ist ein (x, y) Tuple
# Input der Funktion ist eine Zahl oder eine Zeichenkette
def beispiel_mit_match_case_point(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

# Erste Funktion aufrufen
print("beispiel_mit_elif(23)")
beispiel_mit_elif(23)
print("beispiel_mit_elif(-3)")
beispiel_mit_elif(-3)
print("beispiel_mit_elif(-15)") # Der Zweig mit x == -15 wird nicht erreicht
beispiel_mit_elif(-15)
print("beispiel_mit_elif(0)")
beispiel_mit_elif(0)

# Zweite Funktion aufrufen
print()
print("beispiel_mit_if(23)")
beispiel_mit_if(23)
print("beispiel_mit_if(-3)")
beispiel_mit_if(-3)
print("beispiel_mit_if(-15)")
beispiel_mit_if(-15)
print("beispiel_mit_if(0)")
beispiel_mit_if(0)

# Dritte Funktion aufrufen
print()
print("beispiel_mit_match_case(23)")
beispiel_mit_match_case(23)
print("beispiel_mit_match_case(-3)")
beispiel_mit_match_case(-3)
print("beispiel_mit_match_case(-15)")
beispiel_mit_match_case(-15)
print("beispiel_mit_match_case(0)")
beispiel_mit_match_case(0)
print("beispiel_mit_match_case(\"Hallo\")")
beispiel_mit_match_case("Hallo")
print("beispiel_mit_match_case(100)")
beispiel_mit_match_case(100)

# Vierte Funktion aufrufen
print()
print("beispiel_mit_match_case_point((0, 0))")
beispiel_mit_match_case_point((0, 0))
print("beispiel_mit_match_case_point((0, 3))")
beispiel_mit_match_case_point((0, 3))
print("beispiel_mit_match_case_point((5, 0))")
beispiel_mit_match_case_point((5, 0))
print("beispiel_mit_match_case_point((-20, 10))")
beispiel_mit_match_case_point((-20, 10))
