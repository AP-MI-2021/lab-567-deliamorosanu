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
    return{
        "id": id,
        "nrapartament": nrapartament,
        "suma": suma,
        "data": data,
        "tipul": tipul
    }

def getId(apartament):
    '''
    Da id-ul aparatmentului
    :param apartament: dictionar ce contine o prajitura
    :return: id-ul apartamentului
    '''
    return apartament["id"]

def getNrapartament(apartament):
    return apartament["nrapartament"]

def getSuma(apartament):
    return apartament["suma"]

def getData(apartament):
    return apartament["data"]

def getTipul(apartament):
    return apartament["tipul"]

def toString(apartament):
    return "Id:{}, Nrapartament: {}, Suma: {}, Data: {}, Tipul: {}".format(
        getId(apartament),
        getNrapartament(apartament),
        getSuma(apartament),
        getData(apartament),
        getTipul(apartament)
    )
