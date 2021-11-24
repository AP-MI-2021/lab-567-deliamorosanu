from Logic.functionaliate import Undo, Redo, SortareChletCresc
from Logic.CRUD import adaugaApartament, stergeApartament


def testUndoRedo():
    listatest = []
    testUndo = []
    testRedo = []
    listatest = adaugaApartament(listatest, "1",1 ,22 ,"gaz", "03.03.2002")
    listatest = adaugaApartament(listatest,"2", 2, 33, "02.02.2002", "gaz")
    listatest = adaugaApartament(listatest, "3", 3, 44, "04.04.2004", "gaz")
    listatest = Undo(listatest, testUndo, testRedo)
    assert len(listatest) == 2
    listatest= Undo(listatest, testUndo, testRedo)
    assert len(listatest) == 1
    listatest= Undo(listatest , testUndo , testRedo)
    assert len(listatest) == 0
    listatest = adaugaApartament(listatest, "1", 1, 22, "03.03.2002", "gaz")
    listatest = adaugaApartament(listatest, "2", 2, 33, "02.02.2002", "gaz")
    listatest = adaugaApartament(listatest, "3", 3, 44, "04.04.2004", "gaz")
    assert len(listatest)==3
    listatest= Undo(listatest, testUndo, testRedo)
    listatest= Undo(listatest, testUndo, testRedo)
    assert len(listatest)==1
    listatest= Redo(listatest, testUndo, testRedo)
    assert len(listatest)==2
    listatest= Redo(listatest, testUndo, testRedo)
    assert len(listatest)==3
    listatest = Undo(listatest, testUndo, testRedo)
    listatest = Undo(listatest, testUndo, testRedo)
    assert len(listatest)==1
    listatest=adaugaApartament(listatest, "4", 4, 55, "05.05.2004", "gaz")
    assert len(listatest)==2
    listatest= Undo(listatest, testUndo, testRedo)
    assert len(listatest)==1
    listatest= Undo(listatest, testUndo, testRedo)
    assert len(listatest)==0
    listatest= Redo(listatest, testUndo, testRedo)
    listatest= Redo(listatest, testUndo, testRedo)
    assert len(listatest)==2
    listatest= Redo(listatest, testUndo, testRedo)
    listatest= stergeApartament("1", listatest)
    assert len(listatest)==1
    listatest= Undo(listatest, testUndo, testRedo)
    assert len(listatest)==2
    listatest= SortareChletCresc(listatest, testUndo, testRedo)
    listatest= Undo(listatest, testUndo, testRedo)
    listatest= Redo(listatest, testUndo, testRedo)




