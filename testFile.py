from Apartment import Apartment
from lab06 import *
def test_Apartment():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1200, 200, "average")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800,250, "excellent")

    assert (a1 == a0) == False
    assert a2.getApartmentDetails() == "Rent: $1000, Distance From UCSB: 100m, Condition: average"
    assert (a1>a0) == True
    assert (a5>a4) == True
    assert (a0<= a3) == True
    assert (a0 == a3) == True
    assert (a0>= a3) == True
    assert a5.getApartmentDetails() == "Rent: $800, Distance From UCSB: 250m, Condtion: excellent"

def test_lab():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")

    mergesort(alist)
    assert alist == [a5,a4,a3,a2,a1,a0]
    assert ensureSortedAscending(alist) == True
    assert getNthApartment(alist,7) == "(Apartment) DNE"
    assert getNthApartment(alist,2) == "(Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: average"
    assert getNthApartment(alist, 4) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"
    alist = [a0,a1,a2,a3,a4,a5]
    assert getTopThreeApartments(alist) == "1st: (Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad\n2nd: (Apartment) Rent: $800, Distance From UCSB: 250m, Condition: average\n3rd: (Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: average"

