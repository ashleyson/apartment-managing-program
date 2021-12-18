from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2

        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                apartmentList[k] = lefthalf[i]
                i += 1 
            else:
                apartmentList[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j += 1
            k += 1

def ensureSortedAscending(apartmentList):
    asc = True
    i = 0
    while asc == True and i < len(apartmentList) - 1:
        current = apartmentList[i]
        nxt = apartmentList[i+1]
        if nxt < current:
            asc = False
        i += 1

    return asc

def getNthApartment(apartmentList, n):
    if n > len(apartmentList)-1:
        return "(Apartment) DNE"
    
    return "(Apartment) " + apartmentList[n].getApartmentDetails()

def getTopThreeApartments(apartmentList):
    mergesort(apartmentList)
    output = ''
    top3 = apartmentList[0:3]

    for i in range(len(top3)):
        if i == 0:
            x = "1st: (Apartment) "

        if i == 1:
            x = "2nd: (Apartment) "

        if i == 2:
            x = "3rd: (Apartment) " 

        output = output + x + top3[i].getApartmentDetails() + '\n'                 
    return output.rstrip()