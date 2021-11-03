from Domain.apartament import CreareAsocitatie, getId, getNrapartament, getSuma,getData,getTipul
from Logic.functionalitati import StergeCheltuieliAp, AdaugaCheltuieliAp,MaximaSumaChelt
from Logic.CRUD import adaugaApartament

def testStergeCheltuieli():
    apartament=[]
    chelt1= CreareAsocitatie("1",1 , 23.3, "23.12.2002", "gaz")
    chelt2= CreareAsocitatie("2", 2, 111, "7.10.2001", "gaz")
    chelt3= CreareAsocitatie("3", 2, 121, "12.12.2012", "gaz")
    apartament= AdaugaCheltuieliAp(apartament, getNrapartament(chelt1), getData(chelt1), getTipul(chelt1))
    apartament= AdaugaCheltuieliAp(apartament, getNrapartament(chelt2), getData(chelt2), getTipul(chelt2))
    apartament= AdaugaCheltuieliAp(apartament, getNrapartament(chelt3), getData(chelt3), getTipul(chelt3))
    apartament= StergeCheltuieliAp(apartament,2)
    assert apartament == chelt1

def testAdaugareCheltuieli():
    apartament=[]
    chelt1 = CreareAsocitatie("1", 1, 23.3, "23.12.2002", "gaz")
    chelt2 = CreareAsocitatie("2", 2, 111, "7.10.2001", "gaz")
    chelt3 = CreareAsocitatie("3", 2, 121, "12.12.2012", "gaz")
    apartament = AdaugaCheltuieliAp(apartament, getNrapartament(chelt1), getData(chelt1), getTipul(chelt1))
    apartament = AdaugaCheltuieliAp(apartament, getNrapartament(chelt2), getData(chelt2), getTipul(chelt2))
    apartament = AdaugaCheltuieliAp(apartament, getNrapartament(chelt3), getData(chelt3), getTipul(chelt3))
    apartament = AdaugaCheltuieliAp(apartament, "23.02.2002", 5)
    chelt4=     CreareAsocitatie("2",2, "23.02.2002","gaz")
    chelt5= CreareAsocitatie("3",3,21,"23.02.2002", "gaz")
    assert apartament==[chelt1, chelt4, chelt5]
