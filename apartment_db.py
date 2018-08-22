import apartment

class Apartment_DB:
    def __init__(self):
        self.apartDB = list()

    def addApartment(self,apartment):
        self.apartDB.append(apartment)
        print("Apartment sucessfully added")

    def getApartment(self,apt_num):
        for x in self.apartDB:
            if x.get_apt_num()==apt_num:
                return x
        print("Apartment not found") 
        return None
    
    def getAvailApartments(self):
        x = list()
        for a in self.apartDB:
            if a.get_apt_status() == 'A':
                x.append(a)
        return x

    def getRentedApartments(self):
        b = list()
        for c in self.apartDB:
            if c.get_apt_status() == 'R':
                b.append(c)
        return b

        
    def setchangeApartmentStatus(self,apt_num,apt_status):
        for x in self.apartDB:
            if x.get_apt_num() == apt_num:
                if x.get_apt_status() == apt_status:
                    print("apartment status not changed")
                else :
                    x.set_apt_status(apt_status)
                return
        print("apartment not found") 

    def getTotalApartments(self):
        return len(self.apartDB)

    def getTotalAvailable(self):
        return len(self.getAvailApartments())

    def getTotalRented(self):
        return len(self.getRentedApartments())

    def loadApartments(self,apartment_list):
        file = open('list_1.txt','r')
        for line in file:
            columns = line.strip().split()
            self.addApartment(apartment.Apartment(int(columns[0]),int(columns[1]),int(columns[2]),int(columns[3]),columns[4]))

        
