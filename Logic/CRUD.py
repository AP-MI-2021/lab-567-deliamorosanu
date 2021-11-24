from Domain.apartamente import CreareAsocitatie, getId


def adaugaApartament(id,nrapartament, suma, data, tipul,lista):
    '''
    adauga un apartament intr-o lista
    :param id: string
    :param nrapartament:int
    :param suma:float
    :param data:string
    :param tipul:string
    :param lista: lista de apartamente
    :return: o lista continand elementele vechi si noul apartament
    '''
    apartament =  CreareAsocitatie(id,nrapartament, suma, data, tipul)
    return lista + [apartament]

def getById(id, lista):
    """

    :param id:
    :param lista:
    :return:
    """
    for apartament in lista:
        if getId(apartament)==id:
            return id
    return None

def stergeApartament(id, lista):
    '''
    Sterge apartamentul din lista
    :param nrapartament: nr apartamentului sters
    :param lista: lista de apartamente
    :return: Lista apartamentelor fara elementul cu numarul dat
    '''
    return[apartament for apartament in lista if getId(apartament) != id]

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
        if getId(apartament)== id:
            cheltuialaNoua= CreareAsocitatie(id,nrapartament, suma, data, tipul)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(apartament)
    return listaNoua