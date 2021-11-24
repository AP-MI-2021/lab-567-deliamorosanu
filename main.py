from Tests.testAll import runAllTests
from UI.console import runMenu
from Tests.testCRUD import testStergeCheltuiala, testModificaCheltuaiala


def main():
    runAllTests()
    testStergeCheltuiala()
    testModificaCheltuaiala()
    lista=[]
    undoOp=[]
    redoOp=[]
    runMenu(lista, undoOp, redoOp)

main()