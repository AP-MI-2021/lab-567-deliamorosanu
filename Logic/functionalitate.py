from Domain.apartament import getId,getNrapartament,getSuma,getData,getTipul, CreareAsocitatie

def StergeToateChelt(lista, nrapartamentsters):
    """
    Sterge toate cheltuielile unui apartament dat.
    :param lista: lista apartementelor
    :param nrapartament: int
    :return:
    """
    rezultat= []
    for lista in lista:
        if getNrapartament(lista) != nrapartamentsters:
            rezultat.append(lista)
    if len(lista)==0:
        raise ValueError("Acest apartament nu are cheltuieli!")
    return rezultat


def AdaugaValoare(lista, data, val):
    '''
    Adaugare valoare (la suma) tuturor cheltuielilor pentru o data aleasa.
    :param lista: lista
    :param data: string
    :param val: float
    :return:
    '''
    result = []
    for lista in lista:
        if getData(lista) == data:
            cheltuialanoua =CreareAsocitatie(getId(lista), getNrapartament(lista), float(getSuma(lista)) +
                                               val, getData(lista), getTipul(lista))
            result.append(cheltuialanoua)
        else:
            result.append(lista)
    return result


def CeaMaiMareChelt(lista):
    '''
    :param lista: lista
    :return: cea mai mare cheltuiala a unui anumit tip de cheltuiala
    '''
    result = {}
    for apartament in lista:
        tip = getTipul(apartament)
        cheltuiala= getSuma(apartament)
        if apartament in result:
            if cheltuiala > getSuma(result[tip]):
                result[tip] = apartament
        else:
            result[tip] = apartament
    return result



def SortareCheltDescr(lista):
    '''
    Sortare cheltuieli descrescator
    :param lista: lista
    :return: lista cheltuieli descrescator
    '''
    return sorted(lista, key = lambda lista: getSuma(lista), reverse = True)

def SortareChletCresc(lista):
    """
    Sortare cheltuieli crescator
    :param lista: lista
    :return: lista cheltuieli crescator
    """
    return sorted(lista, key= lambda lista: getSuma(lista))