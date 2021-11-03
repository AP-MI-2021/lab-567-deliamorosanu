from Tests.testCRUD import testAdaugaApartament,testStergeCheltuiala, testModificaCheltuaiala
from Tests.testDomain import testApartament


def runAllTests():
    testApartament()
    testAdaugaApartament()
    testStergeCheltuiala()
    testModificaCheltuaiala()