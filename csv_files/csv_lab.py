import csv 

class PhoneContact: 
    def __init__(self, name, phone): 
        self.name = name
        self.phone = phone 

class Phone: 
    def __init__(self): 
        self.contacts = []

    def load_contacts_from_csv(self, contacts):
        with open(contacts, newline="") as contacts: 
            contacts = csv.DictReader(contacts)
            
            for contact in contacts: 
                name = contact['Name']
                phone = contact['Phone']

                new_contact = PhoneContact(name, phone)
                self.contacts.append(new_contact)

    def search_contacts(self):
        desired_contact = input("Search contacts: ")
        desired_contact = desired_contact.lower().strip()
        
        found = False 

        for contact in self.contacts: 
            if contact.name.find(desired_contact) != -1:  
                print(f"{contact.name} ({contact.phone})")

                found = True 
                continue 


            if contact.phone.find(desired_contact) != -1: 
                print(f"{contact.name} ({contact.phone})")

                found = True 
                continue 

        if not found: 
            print("No contacts found")


phone = Phone()
phone.load_contacts_from_csv("contacts.csv")
phone.search_contacts()
phone.search_contacts()