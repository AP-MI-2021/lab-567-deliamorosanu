from Domain.apartament import toString
from Logic.CRUD import adaugaApartament, stergeApartament, modificaCheltuiala


def printMenu():
    print("1. Adaugare apartament")
    print("2. Stergere apartament")
    print("3. Modificare cheltuiala")
    print("a. Afisare apartamente")
    print("x. Iesire")


def uiAdaugaAparatment(lista):
    id = input("Dati id-ul: ")
    nrapartament= int( input("Dati numarul apartamentului: "))
    suma = int(input("Dati suam ce trebuie platitia: "))
    data = input("Dati data platii: ")
    tipul=input("Dati tipul de cheltuiala ceruta: ")
    return adaugaApartament(id, nrapartament, suma, data, tipul, lista)



def uiStergeApartament(lista):
    nraparatament=int( input("Dati numarul apartamentului de sters: "))
    return stergeApartament(nraparatament, lista)


def uiModificaCheltuiala(lista):
    id = input("Dati id-ul: ")
    nrapartament = int(input("Dati numarul apartamentului: "))
    suma = int(input("Dati suam ce trebuie platitia: "))
    data = input('Dati data platii: ')
    tipul = input("Dati tipul de cheltuiala ceruta: ")
    return modificaCheltuiala(id, nrapartament, suma, data, tipul, lista)




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