# Task 13/16
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

class Cat(Animal):
    def say(self):
        return "Meow"

class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
        
    def say(self):
        return "meow"

    def change_weight(self, weight):
        self.weight = weight

# Task 14/16
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {'id':Contacts.current_id, 'name':name,'phone':phone, 'email':email,'favorite':favorite}
        self.contacts.append(contact)
        Contacts.current_id+=1
        return "contact added"
    
contact = Contacts()
print(contact.add_contacts("Mini", "575858", "knlknl@bk.jv", True))
print(contact.add_contacts("Miki", "000111", "kl@bk.jv", False))
print(contact.list_contacts())

# Task 15/16
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for rec in self.contacts:
            if rec:
                for key in rec:
                    if rec[key] == id:
                        return rec
                    else: 
                        continue
            else:
                return None
            
# Task 16/16
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        for rec in self.contacts:
            if rec:
                for key in rec:
                    if rec[key] == id:
                        self.contacts.remove(rec)
                    else: 
                        continue
            else:
                pass