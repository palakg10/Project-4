class Apartment:
    def __init__(self,apt_num,apt_bedrm,apt_bath,rent_amount,apt_status):
        self.apt_num = apt_num
        self.apt_bedrm = apt_bedrm
        self.apt_bath = apt_bath
        self.rent_amount = rent_amount
        self.apt_status = apt_status

    def  get_apt_status (self):
        return self.apt_status 

    def  set_apt_status(self,apt_status):
         self.apt_status = apt_status

    def get_apt_num(self):
        return self.apt_num

    def set_apt_num(self,apt_num):
         self.apt_num = apt_num


    def get_apt_bedrm(self):
        return self.apt_bedrm

    def set_apt_bedrm(self,apt_bedrm):
         self.apt_bedrm = apt_bedrm


    def get_apt_bath(self):
        return self.apt_bath

    def set_apt_bath(self,apt_bath):
         self.apt_bath = apt_bath

    def get_rent_amount(self):
        return self.rent_amount

    def set_rent_amount(self,rent_amount):
        self.apt_rent_amount = rent_amount
       

    

    
        


    

    
        
