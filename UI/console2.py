from UI.console import showAll
from Logic.CRUD import adaugaApartament, stergeApartament, modificaCheltuiala


def Help():
    '''
    E un nou meniu prin care comenzile se separa prin ; si prin ,iar comenzile sunt urm:add
    Showall, Delete, Update
    :return:
    '''
    print("add,id,titlu,gen,pret,tipReducere")
    print("Delete,id")
    print("Showall")
    print("Update,id,titlu,gen,pret,reducere")
    print("Stop")


def MENU(lista):

    while True:
            option = input(" Introduceti comanda: ")
            action = option.split(";")
            for line in action:
                command=line.split(",")
                if command[0] == "Help":
                    help()
                elif command[0] == "Add":
                    try:
                        lista= adaugaApartament(command[1],command[2],command[3],float(command[4]),command[5],lista)
                    except ValueError as ve:
                        print("Eroare {}".format(ve))
                elif command[0] == "delete":
                    lista=stergeApartament(command[1],lista)
                elif command[0] == "Update":
                    try:
                        lista=modificaCheltuiala(command[1],command[2],command[3],float(command[4]),command[5],lista)
                    except ValueError as ve:
                        print("Eroare {}".format(ve))
                elif command[0] == "Showall":
                    showAll(lista)
                elif command[0] == "Stop":
                    break


