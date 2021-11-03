from Domain.apartament import CreareAsocitatie, getId, getNrapartament, getSuma, getData, getTipul

def testApartament():
    apartament = CreareAsocitatie("1",1, 200, "25.03.2002" , "intretinere")

    assert getId(apartament)== "1"
    assert getNrapartament(apartament) ==1
    assert getSuma(apartament) == 200
    assert getData(apartament) == "25.03.2002"
    assert getTipul(apartament) == "intretinere"