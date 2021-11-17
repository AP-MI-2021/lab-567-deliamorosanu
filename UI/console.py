from Domain.apartament import toString, getId,getSuma,getData,getTipul
from Logic.CRUD import adaugaApartament, stergeApartament, modificaCheltuiala, getByNrApartament
from Logic.functionalitate import StergeToateChelt, AdaugaValoare,CeaMaiMareChelt,SortareCheltDescr, SortareChletCresc


def printMenu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere apartament")
    print("3. Modificare cheltuiala")
    print("4. Sterge toate cheltuielile unui apartament dat")
    print("5. Adauga o valoare la suma tututot cheltuielilor pentru o data aleasa")
    print("6. Arata cea mai mare cheltuiala a unui anumit tip de cheltuiala")
    print("7. Sorteaza lista cheltuielilor descrescator")
    print("8. Sorteaza lista cheltuielilor crescator")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare apartamente")
    print("x. Iesire")


def uiAdaugaAparatment(lista, undoOp, redoOp):
    try:
        id = input("Dati id-ul: ")
        nrapartament= int( input("Dati numarul apartamentului: "))
        suma = float(input("Dati suma ce trebuie platitia: "))
        data = input("Dati data platii: ")
        tipul=input("Dati tipul de cheltuiala ceruta: ")
        rezultat= adaugaApartament(id, nrapartament,suma, data, tipul,lista)
        undoOp.append([
            lambda : stergeApartament(nrapartament,rezultat),
            lambda : adaugaApartament(id, nrapartament, suma, data,tipul, lista)
        ])
        redoOp.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeApartament(lista, undoOp, redoOp):
    try:
        nrapartament=int(input("Dati numarul apartamentui ce trebuie sters din lista"))
        rezultat= stergeApartament(nrapartament, lista)
        apartamentSters= getByNrApartament(nrapartament, lista)
        undoOp.append([
            lambda :adaugaApartament(
                nrapartament,
                getId(apartamentSters),
                getData(apartamentSters),
                getSuma(apartamentSters),
                getTipul(apartamentSters),
                rezultat),
            lambda: stergeApartament(nrapartament, lista)
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
        cheltuialaVeche=  getByNrApartament(nrapartament,lista)
        undoOp.append([
            lambda :modificaCheltuiala(
                nrapartament,
                getId(cheltuialaVeche),
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


def uiStergetoatechelt(lista):
    """

    :param lista:
    :return:
    """
    Nrap= int(input("Dati nr ap a caror cheltuieli le vreti sterse"))
    cheltnoua= StergeToateChelt(lista, Nrap)
    print("A fost sters")
    return cheltnoua


def uiAdaugavaloare(lista):
    """

    :param lista:
    :return:
    """
    val=float(input("Dati "))
    data=input("Dati data aleasa")
    lista= AdaugaValoare(lista, val, data)
    print("Valoarea a fost adaugata cu succes")
    return lista


def uiCeamaimareChelt(lista):
    rezultat= CeaMaiMareChelt(lista)


def uiSortareDescr(lista):
    """

    :param lista:
    :return:
    """
    lista= SortareCheltDescr(lista)
    print("S-a sortat descrescator")
    return lista

def uiSortareCresc(lista):
    """

    :param lista:
    :return:
    """
    lista= SortareChletCresc(lista)
    print("S-a sortat crescator")
    return lista


def runMenu(lista):
    undoOp=[]
    redoOp=[]
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaAparatment(lista, undoOp,redoOp)
        elif optiune == "2":
            lista = uiStergeApartament(lista, undoOp, redoOp)
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista, undoOp, redoOp)
        elif optiune == "4":
            lista = uiStergetoatechelt(lista)
        elif optiune == "5":
            lista=uiAdaugavaloare(lista)
        elif optiune == "6":
            lista= uiCeamaimareChelt(lista)
        elif optiune == "7":
            uiSortareDescr(lista)
        elif optiune == "8":
            uiSortareCresc(lista)
        elif optiune == "u":
            if len(undoOp) > 0:
                operations = undoOp.pop()
                redoOp.append(operations)
                lista = operations[0]()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoOp) > 0:
                operations = redoOp.pop()
                undoOp.append(operations)
                lista = operations[1]()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")