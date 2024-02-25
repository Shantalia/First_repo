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
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite
        contact = {"id":self.current_id, "name":self.name,\
                                             "phone":self.phone, "email":self.email,\
                                                "favorite":self.favorite}
        self.contacts.append(contact)
        print(self.contacts)
        print(self.current_id)
        return "contact added"
    
contact = Contacts()
print(contact.add_contacts("Mini", "575858", "knlknl@bk.jv", True))
print(contact.add_contacts("Mini", "575858", "knlknl@bk.jv", True))
