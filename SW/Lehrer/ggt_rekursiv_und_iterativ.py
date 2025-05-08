# Quelle: C:/Users/marti/Desktop/Programmierung/Python-Programmiersprache/Rekursiv_und_iterativ
# Größter gemeinsamer Teiler - rekursiv
def ggt_reku(m, n):
    if m == n:
        print("m == n", m, n)
        return m
    else:
        if m > n:
            print("m > n", m, n)
            return ggt_reku(m-n, n)
        else:
            print("m < n", m, n)
            return ggt_reku(m, n-m)

# Größter gemeinsamer Teiler - iterativ
def ggt_iter(m, n):
    while True:
        if m == n:
            print("m == n", m, n)
            break
        if m > n:
            print("m > n", m, n)
            m = m - n
        else:
            print("m < n", m, n)
            n = n - m
    return m
        


m = int(input("Zahl m: ")) 
n = int(input("Zahl n: "))

print("GGT´=", ggt_reku(m, n)) 
print("GGT =", ggt_iter(m, n))
