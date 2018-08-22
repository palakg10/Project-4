import apartment
import tenant
import tenant_db
import apartment_db



def menu():
    '''display the menu with options that user like to enter'''

    choice = 0
    while choice != 8:
        
        print("Main Choice: Choose 1 of 8 choices  ")
        print("Choose 1 for Rent/Lease Apartment:  ")
        print("Choose 2 for Search Available Apartment:  ")
        print("Choose 3 for Make Apartment Available:  ")
        print("Choose 4 for List Available Aparments:  ")
        print("Choose 5 List Rented/lease Apartments:  ")
        print("Choose 6 for Tenant information:  ")
        print("Choose 7 for Add new Apartment: ")
        print("Choose 8 Exit")
        choice =int(input("choose an option: "))

        if choice == 1:
            rent_lease_apartment()
        elif choice == 2:
            select_available_apartment()
        elif choice == 3:
            make_aparment_available()
        elif choice == 4:
            list_available_apartments()
        elif choice == 5:
            display_rented_apartments()
        elif choice == 6:
            display_tenant_information()
        elif choice == 7:
            add_new_apartment()
        elif choice == 8:
            summary_report()

        else:
            print("Enter a valid choice")

apartments = apartment_db.Apartment_DB()
tenants = tenant_db.Tenant_db()
apartments.loadApartments('apartment_list.txt')

#define functions for each menu options
def summary_report():
    '''this function will print summary of total number of apartments,
    total number of apartments under lease, total number of apartments available, total number of tenants'''
    print('Total Apartments',apartments.getTotalApartments())
    print('Total Apartments lease',apartments.getTotalRented())
    print ('Total APartments Available',apartments.getTotalAvailable())
    print('Total Tenants',tenants.countTenants())

def add_new_apartment():
    '''this function will add new apartment to the db '''
    apartment_number = int(input("Enter Apartment Number: "))
    number_of_bedrooms = int(input("Enter number of bedooms:  "))
    number_of_bathrooms = int(input("Enter number of bathrooms: "))
    rent_amount = int(input("Enter a rent amount : "))
    apartments.addApartment(apartment.Apartment(apartment_number,number_of_bedrooms,number_of_bathrooms,rent_amount,'A'))



def display_tenant_information():
    '''display details about current tenant'''
    aptNum = int(input("Enter apartment number: "))
    renter = tenants.getTenant(aptNum)
    if renter :
        print(renter.get_tenant_id(),renter.get_tenant_fName(),renter.get_tenant_lName(),renter.get_tenant_aptNum())
    else:
        apt = apartments.getApartment(aptNum)
        if apt:
            if apt.get_apt_status() == 'A':
                print("Apartment is availabe to rent")
            else:
                print('Apartment rented but could not find tenant')

        else:
            print('Apartment does not exist')

def display_rented_apartments():
    '''display current rented apartments'''
    rented = apartments.getRentedApartments()
    print('{}'.format("Apt#"),'{}'.format("Bedrms"),'{}'.format("baths"),'{}'.format("rent"),'{}'.format("ID#"),'{}'.format('name'))
    for apt in rented :
        renter = tenants.getTenant(apt.get_apt_num())
        print("%4d %6d %5d %4d %5d %s"%
             (apt.get_apt_num(),apt.get_apt_bedrm(),apt.get_apt_bath(),apt.get_rent_amount(),renter.get_tenant_id(),renter.get_tenant_fName() + renter.get_tenant_lName()))

def list_available_apartments():
    '''displays list of available apartments'''
    available = apartments.getAvailApartments()
    print('{}'.format("Apt#"),'{}'.format("Bedrms"),'{}'.format("baths"),'{}'.format("rent"))
    for apt in available :
        print("%4d %6d %5d %4d"%
             (apt.get_apt_num(),apt.get_apt_bedrm(),apt.get_apt_bath(),apt.get_rent_amount()))
    

def make_aparment_available():
    '''will make any rented apartment available for rent and delete existing tenant'''
    aptNum = int(input("Please enter apartment number: "))
    renter = tenants.getTenant(aptNum)
    if renter :
        tenants.removeTenant(aptNum)
    else:
        print("No Tenant found")

    apt = apartments.getApartment(aptNum)
    if apt :
        if apt.get_apt_status() == 'A':
            print("Aparment already available")
        else:
            apt.set_apt_status('A')
    else:
        print("no such apartment")


def select_search():
    '''function to search aptment per user's criteria'''
    min_bedroom = int(input("how may bedrooms you looking for : "))
    min_baths = int(input("how many baths you lookinf for: "))
    max_rent_amount = int(input("how much rent are you willing to pay: "))
    available = apartments.getAvailApartments()
    result = []
    for apt in available :
        if apt.get_rent_amount()> max_rent_amount:
            continue
        if apt.get_apt_bedrm()< min_bedroom:
            continue
        if apt.get_apt_bath() < min_baths:
            continue
        result.append(apt)
    return result
    
def select_available_apartment():
    '''function to search aptment per user's criteria'''
    search = select_search()
    print('{}'.format("Apt#"),'{}'.format("Bedrms"),'{}'.format("baths"),'{}'.format("rent"))
    for apt in search :
        print("%4d %6d %5d %4d"%
             (apt.get_apt_num(),apt.get_apt_bedrm(),apt.get_apt_bath(),apt.get_rent_amount()))
    if len(search) == 0 :
        print("no apartments found based on your search: ")
        
def rent_lease_apartment():
    '''based on search criteria will allow user to rent apartment'''
    search = select_search()
    print('{}'.format("Sel"),'{}'.format("Apt#"),'{}'.format("Bedrms"),'{}'.format("baths"),'{}'.format("rent"))
    sel = 0 
    for apt in search :
        sel += 1
        print("%2d. %4d %6d %5d %5d"%
             (sel,apt.get_apt_num(),apt.get_apt_bedrm(),apt.get_apt_bath(),apt.get_rent_amount()))
    if len(search) == 0 :
        print("No apartments found based on your search: ")
    else:
        while True:
            sel = int(input("select apartment to rent: "))
            if sel == -1:
                return
            if sel < 1 or sel > len(search):
                print("selection",sel,"not on list")
                continue
            sel -= 1
            break

        while True:
            fname = input("first name")
            if not fname:
                print("first name required")
                continue
            break

        while True:
             lname = input("last name")
             if not lname:
                 print("last name required")
                 continue
             break
        tenants.addTenant(tenant.Tenant(fname,lname,search[sel].get_apt_num() ))
        apartments.setchangeApartmentStatus(search[sel].get_apt_num(),'R')
    
  

    
    
menu()
