import tenant
class Tenant_db:
    def __init__(self):
        self.tenants = list()

    def addTenant(self,tenant):
        self.tenants.append(tenant)

    def getTenant(self,aptNum):
        for x in self.tenants:
            if x.get_tenant_aptNum() == aptNum:
                return x
        return ''

    def countTenants(self):
        return len(self.tenants)

    def removeTenant(self,aptNum):
        for i in range(len(self.tenants)):
            if self.tenants[i].get_tenant_aptNum() == aptNum:
                x = self.tenants[i]
                del self.tenants[i]
                return x
        return ''

    def getAllTenants(self):
        return self.tenants[:]
                
            
        
        
