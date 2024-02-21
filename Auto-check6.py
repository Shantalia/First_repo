# Task 7/16
class Animal1:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def info(self):
        inf = {}
        inf["name"] = self.name
        inf["age"] = self.age
        inf["address"] = self.address
        return inf
        

class Dog(Animal1):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()

owner = Owner("Mike", 18, "London")
dog = Dog("Mimi", 15, "Labr", owner)
print(dog.who_is_owner())

# Task 8/16
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"
    
class CatDog(Cat, Dog):
    def info(self):
        return f"{self.nickname}-{self.weight}"

class DogCat(Dog, Cat):
    def info(self):
        return f"{self.nickname}-{self.weight}"

cat = CatDog("Mimi", 2)
dog = DogCat("Laki", 5)
print(cat.say())
print(dog.say())

# Task 9/16
from collections import UserDict

class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys
    
some_dict = {1:2, 2:1, 3:2}
find = LookUpKeyDict(some_dict)
print(find.lookup_key(2))

# Task 10/16
from collections import UserList

class AmountPaymentList(UserList):
    def amount_payment(self):
        sum = 0
        for value in self.data:
            if value > 0:
                sum = sum + value
        return sum

payment = [1, -3, 4]
pay = AmountPaymentList(payment)
print(pay.amount_payment())

# Task 11/16
from collections import UserString

class NumberString(UserString):
    def number_count(self):
        sum = 0
        for el in self.data:
            if el.isdigit():
                sum+=1
        return sum

some_str = "a0bc321+i7ii2"
num_in_str = NumberString(some_str)
print(num_in_str.number_count())

# Task 12/16
class IDException(Exception):
    pass

def add_id(id_list:list, employee_id):
    if employee_id[:2] == '01':
        id_list.append(employee_id)
        return id_list
    else:
        raise IDException

id_list = []
while True:
    employee_id = input("Enter id: ")
    try:
        print(add_id(id_list, employee_id))
    except IDException:
        print("Wrong eid!")

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
    pass