def CreareAsocitatie(id,nrapartament, suma, data, tipul):
    """
       creeaza un dictionar ce reprezinta un apartament
       :param id: string
       :param nrapartament: int
       :param suma: float
       :param data: string
       :param tipul: string
       :return: dictionarul unui apartament
       """
    return[id, nrapartament, suma, data, tipul]


def getId(apartament):
    '''
    Da id-ul aparatmentului
    :param apartament: dictionar ce contine o prajitura
    :return: id-ul apartamentului
    '''
    return apartament[0]

def getNrapartament(apartament):
    return apartament[1]

def getSuma(apartament):
    return apartament[2]

def getData(apartament):
    return apartament[3]

def getTipul(apartament):
    return apartament[4]

def Set_ID(apartament,id):
    apartament[0]=id


def Set_Nr_Apartement(aparatment,nrapartament):
    '''
    setter pentru nr_apartament
    :param aparatment: apartamentul
    :param nrapartament: nr apartamentului
    :return: se seteaza nr apartamentului
    '''
    aparatment[1]=nrapartament


def Set_Suma(apartament,suma):
    '''
    :param apartament:
    :param suma:
    :return:
    '''
    apartament[2]=suma


def Set_Data(apartament,data):
    '''
    :param apartament:
    :param data:
    :return:
    '''
    apartament[3]=data


def Set_Tipul(apartament,tipul):
    '''
    :param apartament:
    :param tipul:
    :return:
    '''
    apartament[4] = tipul


def toString(apartament):
    return "Id:{}, Nrapartament: {}, Suma: {}, Data: {}, Tipul: {}".format(
        getId(apartament),
        getNrapartament(apartament),
        getSuma(apartament),
        getData(apartament),
        getTipul(apartament)
    )
