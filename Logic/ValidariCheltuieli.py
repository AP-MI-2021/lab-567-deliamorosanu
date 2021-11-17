def VaidareCheltuiala(id, nrapartament, suma, data, tipul):
    '''

    :param id: string
    :param nrapartament: int
    :param suma: float
    :param data: string
    :param tipul: string
    :return:
    '''
    errors = []
    if id == '':
        errors.append('Id-ul nu poate fi vid')
    try:
        nrapartament = int(nrapartament)
        if nrapartament == None:
            errors.append('Numarul apartamentului nu trebuie sa fie vid')
    except ValueError:
        errors.append('Numarul apartamentului trebuie sa fie intreg')

    try:
        suma = float(suma)
        if suma < 0:
            errors.append('Suma trebuie sa fie un numar pozitiv')
    except ValueError:
        errors.append('Suma trebuie sa fie un numar real')

    if data == '':
        errors.append('Data nu poate fi vida')
    if tipul == '':
        errors.append('Tipul nu poate fi vid')

    if len(errors) != 0:
        raise ValueError(errors)

    return id, nrapartament, suma, data, tipul