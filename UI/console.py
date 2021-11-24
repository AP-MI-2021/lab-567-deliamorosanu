from Domain.apartamente import toString, getNrapartament,getSuma,getData,getTipul
from Logic.CRUD import adaugaApartament, stergeApartament, modificaCheltuiala, getById
from Logic.functionaliate import StergeToateChelt, AdaugaValoare,CeaMaiMareChelt,SortareCheltDescr, SortareChletCresc, SumeLunare, Redo, Undo
import datetime

def printMenu():
    print("1. Adaugare apartament")
    print("2. Stergere apartament")
    print("3. Modificare cheltuiala")
    print("4. Sterge toate cheltuielile unui apartament dat")
    print("5. Adauga o valoare la suma tututot cheltuielilor pentru o data aleasa")
    print("6. Arata cea mai mare cheltuiala a unui anumit tip de cheltuiala")
    print("7. Sorteaza lista cheltuielilor descrescator")
    print("8. Sorteaza lista cheltuielilor crescator")
    print("9. Afisare sume lunare pentru fiecare apartament")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare apartamente")
    print("x. Iesire")

def data():
    dataceruta=input("Dati data separata prin punct")
    data=dataceruta.split(".")
    an=int(data[0])
    luna=int(data[1])
    zi= int((data[2]))
    return datetime.date(zi, luna, an)

def uiAdaugaAparatment(lista, undoOp, redoOp):
    try:
        id = input("Dati id-ul: ")
        nrapartament = int(input("Dati numarul apartamentului: "))
        suma = float(input("Dati suma ce trebuie platitia: "))
        data = input("Dati data platii: ")
        tipul = input("Dati tipul de cheltuiala ceruta: ")
        rezultat = adaugaApartament(id, nrapartament, suma, data, tipul, lista)
        undoOp.append(lista)
        redoOp.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeApartament(lista, undoOp, redoOp):
    try:
        id=input("Dati id-ul apartamentui ce trebuie sters din lista")

        rezultat= stergeApartament(id, lista)
        apartamentSters= getById(id, lista)
        undoOp.append([
            lambda :adaugaApartament(
                id,
                getNrapartament(apartamentSters),
                getData(apartamentSters),
                getSuma(apartamentSters),
                getTipul(apartamentSters),
                rezultat),
            lambda: stergeApartament(id, lista)
        ])
        redoOp.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista





def uiModificaCheltuiala(lista,redoOp, undoOp):
    try:
        id = input("Dati id-ul: ")
        nrapartament = int(input("Dati numarul apartamentului: "))
        suma = float(input("Dati suma ce trebuie platitia: "))
        data = input('Dati data platii: ')
        tipul = input("Dati tipul de cheltuiala ceruta: ")

        rezultat= modificaCheltuiala(id, nrapartament,suma,data, tipul,lista)
        cheltuialaVeche=  getById(id,lista)
        undoOp.append([
            lambda :modificaCheltuiala(
                id,
                getNrapartament(cheltuialaVeche),
                getTipul(cheltuialaVeche),
                getData(cheltuialaVeche),
                getSuma(cheltuialaVeche),
                rezultat),
            lambda :modificaCheltuiala(id, nrapartament, suma, data,tipul, lista)
         ])
        redoOp.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for apartament in lista:
        print(toString(apartament))


def uiStergetoatechelt(lista, undoOp, redoOp):
    """

    :param lista:
    :return:
    """
    Nrap= int(input("Dati nr ap a caror cheltuieli le vreti sterse"))
    print("A fost sters")
    return StergeToateChelt(lista, Nrap, undoOp, redoOp)

def uiAdaugavaloare(lista, undoOp, redoOp):
    """

    :param lista:
    :return:
    """
    data = input("Dati data aleasa")
    val=float(input("Dati valoarea ce vreti sa o adaugati"))
    listanoua= AdaugaValoare(lista, data, val, undoOp,redoOp)
    print("Valoarea a fost adaugata cu succes")
    return listanoua


def uiCeamaimareChelt(lista):
    tipcheltuiala= CeaMaiMareChelt(lista)
    for tip, apartament in tipcheltuiala.items():
        print("{}: {}".format(tip, apartament))


def uiSumeLunare(lista):
    rezultat= SumeLunare(lista)
    for luna in rezultat:
        print(f' Luna {luna} are lista de preturi: {rezultat[luna]}')



def Undolista(lista, redoOp, undoOp):
    rezultat= Undo(lista, undoOp, redoOp)
    if rezultat is not None:
        return rezultat
    return lista


def Redolista(lista, redoOp, undoOp):
    rezultat=Redo(lista, undoOp, redoOp)
    if rezultat is not None:
        return rezultat
    return lista



def runMenu(lista, redoOp, undoOp):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaAparatment(lista, undoOp, redoOp)
        elif optiune == "2":
            lista = uiStergeApartament(lista, undoOp, redoOp)
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista, undoOp, redoOp)
        elif optiune == "4":
            lista=uiStergetoatechelt(lista, redoOp, undoOp)
        elif optiune == "5":
            lista=uiAdaugavaloare(lista, redoOp, undoOp)
        elif optiune == "6":
            print(uiCeamaimareChelt(lista))
        elif optiune == "7":
            lista= SortareCheltDescr(lista,redoOp, undoOp)
        elif optiune == "8":
            lista= SortareChletCresc(lista, redoOp, undoOp)
        elif optiune == "9":
            lista=uiSumeLunare(lista)
        elif optiune == "u":
            lista=Undolista(lista, undoOp, redoOp)
        elif optiune == "r":
            lista=Redolista(lista, redoOp, undoOp)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")