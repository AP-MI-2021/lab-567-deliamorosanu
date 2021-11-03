from Domain.apartament import CreareAsocitatie, getNrapartament


def adaugaApartament(id,nrapartament, suma, data, tipul,lista):
    '''
    adauga un apartament intr-o lista
    :param id: string
    :param nrapartament:int
    :param suma:int
    :param data:string
    :param tipul:string
    :param lista: lista de apartamente
    :return: o lista continand elementele vechi si noul apartament
    '''
    apartament =  CreareAsocitatie(id,nrapartament, suma, data, tipul)
    return lista + [apartament]

def getByNrApartament(nrapartament ,lista):
    '''
    Gaseste un apartament cu numarul dat dintr-o lista
    :param nrapartament: int
    :param lista: lista de prajituri
    :return: Apartamentul cu numarul dat din lista sau None,daca acesta nu exista
    '''
    for apartament in lista:
        if getNrapartament(apartament) == nrapartament:
            return apartament
    return None

def stergeApartament(nrapartament, lista):
    '''
    Sterge apartamentul din lista
    :param nrapartament: nr apartamentului sters
    :param lista: lista de apartamente
    :return: Lista apartamentelor fara elementul cu numarul dat
    '''
    return[apartament for apartament in lista if getByNrApartament(apartament, lista) != nrapartament]

def modificaCheltuiala(id,nrapartament, suma, data, tipul,lista):
    '''
    Modifica un apartament cu id-ul dat
    :param id: id-ul apartamentului
    :param nrapartament: numarul apartamentui
    :param suma: cheltuiala ce trebuie platita
    :param data: data cheltuielii
    :param tipul: tipul de cheltuiala
    :return:lista modificata
    '''
    listaNoua=[]
    for apartament in lista:
        if getNrapartament(apartament)== nrapartament:
            cheltuialaNoua= CreareAsocitatie(id,nrapartament, suma, data, tipul)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(apartament)
        return listaNoua