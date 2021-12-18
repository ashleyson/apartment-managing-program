#Apartment.py
class Apartment:
    def __init__(self, rent = 0, metersFromUCSB = 0, condition = "N/A"):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "Rent: ${}, Distance From UCSB: {}m, Condition: {}".format(self.rent,self.metersFromUCSB,self.condition)
    def __gt__(self,rhs):
        if self.rent == rhs.rent:
            if self.metersFromUCSB == rhs.metersFromUCSB:
                x = self.condition
                y = rhs.condition
                return x[1] < y[1]
            return self.metersFromUCSB > rhs.metersFromUCSB

        return self.rent > rhs.rent 

    def __lt__(self,rhs):
        if self.rent == rhs.rent:
            if self.metersFromUCSB == rhs.metersFromUCSB:
                x = self.condition
                y = rhs.condition
                return x[1] > y[1]
            return self.metersFromUCSB < rhs.metersFromUCSB

        return self.rent < rhs.rent
    def __ge__(self,rhs):
        if self.rent == rhs.rent:
            if self.metersFromUCSB == rhs.metersFromUCSB:
                x = self.condition
                y = rhs.condition
                return x[1] <= y[1]
            return self.metersFromUCSB >= rhs.metersFromUCSB

        return self.rent >= rhs.rent 

    def __le__(self,rhs):
        if self.rent == rhs.rent:
            if self.metersFromUCSB == rhs.metersFromUCSB:
                x = self.condition
                y = rhs.condition
                return x[1] >= y[1]
            return self.metersFromUCSB <= rhs.metersFromUCSB

        return self.rent <= rhs.rent

    def __eq__(self,rhs):
        if self.rent == rhs.rent and self.condition == rhs.condition and self.metersFromUCSB == rhs.metersFromUCSB:
            return True
        return False

