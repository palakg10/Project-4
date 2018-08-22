class Tenant :
    def __init__(self,tenant_fName,tlname,tenant_apt_num):
        self.tenant_fName = tenant_fName
        self.tenant_lName = tlname
        self.tenant_aptNum = tenant_apt_num
        self.tenant_id = hash((tenant_fName,tlname,tenant_apt_num))%100000


    def  get_tenant_fName (self):
        return self.tenant_fName

    def get_tenant_lName(self):
        return self.tenant_lName

    def get_tenant_aptNum(self):
        ##print ("hello I am tenant")
        return self.tenant_aptNum

    def get_tenant_id(self):
        #print(tenant_id)
        return self.tenant_id

    
 
