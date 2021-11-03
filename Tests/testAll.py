from Tests.testCRUD import testAdaugaApartament,testStergeCheltuiala, testModificaCheltuaiala
from Tests.testsDomain import testApartament


def runAllTests():
    testApartament()
    testAdaugaApartament()
    testStergeCheltuiala()
    testModificaCheltuaiala()
