from Domain.apartament import CreareAsocitatie, getNrapartament, getSuma, getData, getTipul

def StergeCheltuieliAp(nrapartament, lista):
    '''
    Stergem toate cheltuielile unui apartament
    :param nrapartament: numar apartament
    :param lista: lista cheltuielilor
    :return: cheltuielile ramase
    '''

    nouacheltuiala=[]
    for apartament in lista:
        if getNrapartament(apartament) != nrapartament:
            nouacheltuiala.append(apartament)
    return nouacheltuiala


def AdaugaCheltuieliAp(lista, data, suma2):
    '''
    Adauga o noua cheltuiala la cele initiale
    :param lista: lista cheltuielilor
    :param data: cand se face adaugarea
    :param suma2: suma adaugata
    :return: Lista noilor cheltuieli 
    '''
    noualista=[]
    for apartament in lista:
        if getData(apartament)== data:
            nouacheltuiala= CreareAsocitatie(
                getNrapartament(apartament),
                getSuma(apartament)+suma2,
                getData(apartament),
                getTipul(apartament)
            )
            noualista.append(nouacheltuiala)
        else:
            noualista.append(apartament)
    return noualista

def MaximaSumaChelt(lista):
    '''
    Aflam cea mai mare valoare a unei cheltuieli de la un apartament
    :param lista: lista cheltuielilor
    :return: cea mai mare suma
    '''
    sumacheltuieli= []
    for apartament in lista:
        tipul= getTipul(apartament)
        suma= getSuma(apartament)
        if suma in sumacheltuieli:
            if getSuma(sumacheltuieli[suma]) < suma:
                sumacheltuieli[suma] = apartament
            else:
                sumacheltuieli[suma]= apartament
    return sumacheltuieli
