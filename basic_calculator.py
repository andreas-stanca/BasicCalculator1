def adunare(a, b):
    return a + b
def scadere(a, b):
    return a - b
def inmultire(a, b):
    return a * b
def impartire(a, b):
    return a / b
while True:
    operatie = input("1 - adunare / 2 - scadere / 3 - inmultire / 4 - impartire: ")
    n1 = float(input("Primul numar: "))
    n2 = float(input("Al doilea numar: "))
    rezultat = 0

    if operatie == "1":
        rezultat = adunare(n1, n2)
    elif operatie == "2":
        rezultat = scadere(n1, n2)
    elif operatie == "3":
        rezultat = inmultire(n1, n2)
    elif operatie == "4":
        rezultat = impartire(n1, n2)

    else:
        operatie = input("1 - adunare / 2 - scadere / 3 - inmultire / 4 - impartire: ")

    print("Rezultatul este: ", rezultat)