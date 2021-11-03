from Domain.apartament import toString
from Logic.CRUD import adaugaApartament, stergeApartament, modificaCheltuiala
from Logic.functionalitati import StergeCheltuieliAp, AdaugaCheltuieliAp,MaximaSumaChelt

def printMenu():
    print("1. Adaugare apartament")
    print("2. Stergere apartament")
    print("3. Modificare cheltuiala")
    print("4. Stergerea cheltuielilor unui apartament dat")
    print('6. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială')
    print('7. Ordonarea cheltuielilor descrescator dupa suma')
    print("a. Afisare apartamente")
    print("x. Iesire")

def uiAdaugaAparatment(lista):
    id = input("Dati id-ul: ")
    nrapartament= int( input("Dati numarul apartamentului: "))
    suma = float(input("Dati suam ce trebuie platitia: "))
    data = input("Dati data platii: ")
    tipul=input("Dati tipul de cheltuiala ceruta: ")
    return adaugaApartament(id, nrapartament, suma, data, tipul, lista)



def uiStergeApartament(lista):
    nraparatament= input("Dati numarul apartamentului de sters: ")
    return stergeApartament(nraparatament, lista)


def uiModificaCheltuiala(lista):
    id = input("Dati id-ul: ")
    nrapartament = int(input("Dati numarul apartamentului: "))
    suma = int(input("Dati suam ce trebuie platitia: "))
    data = input('Dati data platii: ')
    tipul = input("Dati tipul de cheltuiala ceruta: ")
    return modificaCheltuiala(id, nrapartament, suma, data, tipul, lista)

def uiStergereCheltuieliAp(lista):
    try:
        nrapartament = int(input('Dați numărul apartamentului pentru care se efectuează ștergerea cheltuielilor: '))
        n = StergeCheltuieliAp(lista, nrapartament)
        print(n)
        print('Cheltuielile au fost șterse!')
        return n
    except ValueError as ve:
        print('Eroare', ve)
        return lista

def uiAdaugaCheluieliAp(lista):
    try:
        data = input('Dați data pentru care se va face adunarea: ')
        valoare = float(input('Dați valoarea care trebuie adăugată: '))
        list_of_cheltuieli = AdaugaCheltuieliAp(lista, data, valoare)
        print(lista)
        print('Adăugare efectuată cu succes!')
        return lista
    except ValueError as ve:
        print('Eroare', ve)
        return lista

def uiShowAll(lista):
    try:
        for apartament in lista:
            print(toString(apartament))
    except Exception:
        print("Eroare")




def showAll(lista):
    for apartament in lista:
        print(toString(apartament))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaAparatment(lista)
        elif optiune == "2":
            lista = uiStergeApartament(lista)
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista)
        elif optiune == "4":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")