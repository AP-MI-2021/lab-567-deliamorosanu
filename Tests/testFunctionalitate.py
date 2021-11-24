from Domain.apartamente import  CreareAsocitatie, getSuma
from Logic.CRUD import  getById
from Logic.functionaliate import SumeLunare, StergeToateChelt,AdaugaValoare, CeaMaiMareChelt, SortareCheltDescr, SortareChletCresc


def testStergeToateChelt():
    lista1= CreareAsocitatie("1", 1, 22, "03.03.2002", "gaz")
    lista2= CreareAsocitatie("2", 2, 33, "02.02.2002", "gaz")
    lista3= CreareAsocitatie("3", 3, 44, "04.04.2004", "gaz")
    lista=[lista1, lista2, lista3]
    undoOp=[]
    redoOp=[]
    StergeToateChelt(lista, 1,redoOp, undoOp)
    assert getSuma(lista1)==22

def testAdaugavaloare():
    lista1= CreareAsocitatie("1", 1, 22, "12.12.2021", "gaz")
    lista2= CreareAsocitatie("2", 2, 33, "12.12.2021", "gaz")
    lista3= CreareAsocitatie("3", 3, 44, "12.12.2021", "gaz")
    lista = [lista1, lista2, lista3]
    undoOp=[]
    redoOp=[]
    lista=AdaugaValoare(lista, "12.12.2021",10, undoOp, redoOp)
    assert getSuma(getById("1", lista))==32
    assert getSuma(getById("2", lista))==43

def testCeaMaiMareChelt():
    lista1= CreareAsocitatie("1", 1, 22, "03.03.2002", "gaz")
    lista2= CreareAsocitatie("2", 2, 33, "02.02.2002", "apa")
    lista3= CreareAsocitatie("3", 3, 44, "04.04.2004", "intretinere")
    lista=[lista1, lista2, lista3]
    rez=CeaMaiMareChelt(lista)
    assert rez["gaz"]==lista1
    assert rez["apa"]==lista2
    assert rez["intretinere"]==lista3


def testSortareDescr():
    lista1 = CreareAsocitatie("1", 1, 22, "03.03.2002", "gaz")
    lista2 = CreareAsocitatie("2", 2, 33, "02.02.2002", "apa")
    lista3 = CreareAsocitatie("3", 3, 44, "04.04.2004", "intretinere")
    lista = [lista1, lista2, lista3]
    undoOp=[]
    redoOp=[]
    rez=SortareCheltDescr(lista, undoOp, redoOp)
    assert rez[0]==lista3
    assert rez[1]==lista2
    assert rez[2]==lista1


def testSortareCresc():
    lista1 = CreareAsocitatie("1", 1, 22, "03.03.2002", "gaz")
    lista2 = CreareAsocitatie("2", 2, 33, "02.02.2002", "apa")
    lista3 = CreareAsocitatie("3", 3, 44, "04.04.2004", "intretinere")
    lista = [lista1, lista2, lista3]
    undoOp = []
    redoOp = []
    rez=SortareChletCresc(lista,undoOp, redoOp)
    assert rez[0]==lista1
    assert rez[1]==lista2
    assert rez[2]==lista3


def testSumeLunare():
    lista1 = CreareAsocitatie("1", 1, 22, "12.12.2021", "gaz")
    lista2 = CreareAsocitatie("2", 2, 33, "12.12.2021", "gaz")
    lista3 = CreareAsocitatie("3", 3, 44, "12.12.2021", "gaz")
    lista = [lista1, lista2, lista3]
    undoOp = []
    redoOp = []
    rezsume= SumeLunare(lista)
    rez={}
    rez[12]=[22,33,44]
    assert len(rezsume)==len(rez)
    assert rezsume==rez
    assert (rezsume==rez)==True





