from Domain.apartamente import CreareAsocitatie, getNrapartament, getSuma, getData, getTipul
from Logic.CRUD import  stergeApartament, modificaCheltuiala





def testStergeCheltuiala():
    lista1 = CreareAsocitatie(1, 1, 200, "25.03.2002", "intretinere")
    lista2 = CreareAsocitatie(2, 2, 200, "25.03.2002", "intretinere")
    lista=[lista1, lista2]

    assert stergeApartament(2,lista)




def testModificaCheltuaiala():
    lista1 = CreareAsocitatie(1, 1, 200, "25.03.2002", "intretinere")
    lista2 = CreareAsocitatie(2, 2, 200, "25.03.2002", "intretinere")
    lista=[lista1, lista2]

    idnou=1
    nrapnou= getNrapartament(lista2)
    sumanou= 3
    datanoua="12.12.2002"
    tipnou="intretinere"
    crearenoua= CreareAsocitatie(1,2,3, "12.12.2002", "intretinere")
    assert modificaCheltuiala(lista, idnou, getNrapartament(crearenoua), sumanou,datanoua,tipnou)
    assert getSuma(crearenoua)==sumanou
    assert getData(crearenoua)==datanoua
    assert getTipul(crearenoua)==tipnou