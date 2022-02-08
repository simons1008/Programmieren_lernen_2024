# Funktion berechnet rekursiv die Fakultät von x 
def factorial(x:int) -> int:
    if x <= 1:
        return 1

    return x * factorial(x - 1)
