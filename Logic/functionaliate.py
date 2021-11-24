from Domain.apartamente import getId,getNrapartament,getSuma,getData,getTipul, CreareAsocitatie
import datetime


def data():
    dataceruta=input("Dati data separata prin punct")
    data=dataceruta.split(".")
    an=int(data[0])
    luna=int(data[1])
    zi= int((data[2]))
    dataint=datetime.date(zi, luna, an)
    return dataint


def StergeToateChelt(lista, nrapartament, undoOp, redoOp):
    """
    Sterge toate cheltuielile unui apartament dat.
    :param lista: lista apartementelor
    :param nrapartament: int
    :return:
    """
    if(undoOp is not None) & (redoOp is not None):
        undoOp.append(lista)
        redoOp.clear()
    rezultat= []
    for aparatment in lista:
        if getNrapartament(aparatment) == nrapartament:
            cheltuialanoua=CreareAsocitatie(
                getId(aparatment),
                getNrapartament(aparatment),
                0,
                getData(aparatment),
                getTipul(aparatment)
            )
            rezultat.append(cheltuialanoua)
        else:
            rezultat.append(aparatment)
    return rezultat

def AdaugaValoare(lista, data, val,redoOp, undoOp):
    '''
    Adaugare valoare (la suma) tuturor cheltuielilor pentru o data aleasa.
    :param lista: lista
    :param data: string
    :param val: float
    :return:
    '''
    if (undoOp is not None) & (redoOp is not None):
        undoOp.append(lista)
        redoOp.clear()
    result = []
    for apartament in lista:
        dataceruta= getData(apartament)
        if dataceruta==data:
            cheltuialanoua= CreareAsocitatie(
                getId(apartament),
                getNrapartament(apartament),
                getSuma(apartament)+ val ,
                getData(apartament),
                getTipul(apartament)
            )
            result.append(cheltuialanoua)
        else:
            result.append(apartament)
    return result


def CeaMaiMareChelt(lista):
    '''
    :param lista: lista
    :return: cea mai mare cheltuiala a unui anumit tip de cheltuiala
    '''
    tipcheltuiala= {}
    for apartament in lista:
        tip = getTipul(apartament)
        cheltuiala= getSuma(apartament)
        if tip in tipcheltuiala:
            if getSuma(tipcheltuiala[tip]) < cheltuiala:
                tipcheltuiala[tip]= apartament
        else:
            tipcheltuiala[tip]=apartament
    return tipcheltuiala


def SortareCheltDescr(lista, undoOp, redoOp):
    '''
    Sortare cheltuieli descrescator
    :param lista: lista
    :return: lista cheltuieli descrescator
    '''
    if (undoOp is not None) & (redoOp is not None):
        undoOp.append(lista)
        redoOp.clear()
    return sorted(lista, key = lambda lista: getSuma(lista), reverse = True)



def SortareChletCresc(lista, redoOp, undoOp):
    """
    Sortare cheltuieli crescator
    :param lista: lista
    :return: lista cheltuieli crescator
    """
    if (undoOp is not None) & (redoOp is not None):
        undoOp.append(lista)
        redoOp.clear()
    return sorted(lista, key= lambda lista: getSuma(lista))


def SumeLunare(lista):
    '''

    :param lista:
    :return:
    '''
    rezultat={}
    for apartament in lista:
        data=getData(apartament)
        luna= int(data.split(".")[1])
        if luna not in rezultat:
            rezultat[luna]=[]
            rezultat[luna].append(getSuma(apartament))
        else:
            rezultat[luna].append(getSuma(apartament))
    return rezultat


def Undo(lista, undoOp, redoOp):
    if undoOp:
        redoOp.append(lista)
        return undoOp.pop()
    return lista


def Redo(lista, undoOp, redoOp):
    if redoOp:
        undoOp.append(lista)
        return redoOp.pop()
    return lista


    
