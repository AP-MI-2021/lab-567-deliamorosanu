from Domain.apartament import getId, getNrapartament, getSuma, getData, getTipul
from Logic.CRUD import adaugaApartament, getByNrApartament, stergeApartament, modificaCheltuiala


def testAdaugaApartament():
    lista = []
    lista = adaugaApartament("1", 1, 200, "25.03.2002", "intretinere", lista)

    assert len(lista) == 1
    assert getId(getByNrApartament(1, lista)) == "1"
    assert getNrapartament(getByNrApartament(1, lista)) == 1
    assert getSuma(getByNrApartament(1, lista)) == 200
    assert getData(getByNrApartament(1, lista)) == "25.03.2002"
    assert getTipul(getByNrApartament(1, lista)) == "intretinere"


def testStergeCheltuiala():
    lista = []
    lista = adaugaApartament("1", 1, 200, "25.03.2002", "intretinere", lista)
    lista = adaugaApartament("2", 2, 200, "25.03.2002", "intretinere", lista)
    lista = stergeApartament(1, lista)

    lista = stergeApartament(3, lista)


def testModificaCheltuaiala():
    lista = []
    lista = adaugaApartament("1", 1, 200, "25.03.2002", "intretinere", lista)
    lista = adaugaApartament("2", 2, 200, "25.03.2002", "intretinere", lista)
    lista = modificaCheltuiala("1", 1, 300, "25.03.2021", "gaz", lista)

    cheltuialaUpdatata = getByNrApartament(1, lista)
    assert getId(cheltuialaUpdatata) == "1"
    assert getNrapartament(cheltuialaUpdatata) == 1
    assert getSuma(cheltuialaUpdatata) == 200
    assert getData(cheltuialaUpdatata) == "25.03.2002"
    assert getTipul(cheltuialaUpdatata) == "intretinere"

    cheltuialaNeupdatata = getByNrApartament(2, lista)
    assert getId(cheltuialaNeupdatata) == "2"
    assert getNrapartament(cheltuialaNeupdatata) == 2
    assert getSuma(cheltuialaNeupdatata) == 200
    assert getData(cheltuialaNeupdatata) == "25.03.2002"
    assert getTipul(cheltuialaUpdatata) == "intretinere"

    lista = []
    lista = adaugaApartament("1", 1, 200, "25.03.2002", "intretinere", lista)
    lista = modificaCheltuiala("1", 1, 300, "25.03.2021", "gaz", lista)

    cheltuialaNeupdatata = getByNrApartament(1, lista)
    assert getId(cheltuialaNeupdatata) == "1"
    assert getNrapartament(cheltuialaNeupdatata) == 1
    assert getSuma(cheltuialaNeupdatata) == 200
    assert getData(cheltuialaNeupdatata) == "25.03.2002"
    assert getTipul(cheltuialaNeupdatata) == "intretinere"