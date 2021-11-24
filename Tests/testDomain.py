from Domain.apartamente import CreareAsocitatie, getSuma,getData,getTipul,getNrapartament

def testDomain():
    lista=  CreareAsocitatie(1,1,10,'12.12.2021',"gaz")
    assert getNrapartament(lista)==1
    assert getSuma(lista)==10
    assert getData(lista)=="12.12.2021"
    assert getTipul(lista)=="gaz"