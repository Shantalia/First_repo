# task 1/15
name = "Kate"
age = 28

print(f'{name}, {age}') # не надо в автопроверке

# task 2/15
rate = 1.68
value = 200
payment = rate*value

print(f'Вартість: {payment}') # не надо в автопроверке

# task 3/15
rate = 1.68
value_day = 220
value_night = 150
payment = (rate*value_day)+((rate/2)*value_night)

print(f'Вартість: {payment}') # не надо в автопроверке

# task 4/15
first_name = "Kate"
last_name = "Kozachenko"

print(f'{first_name}, {last_name}') # не надо в автопроверке

# task 5/15
full_name = first_name + ' ' + last_name

print(f'{full_name}')

# task 6/15
length = 2.75
width = 1.75
area = length*width
show = f"With width {width} and length {length} of the room, its area is equal to {area}"

print(show)
# task 7/15
is_active = True
is_delete = False

# task 8/15
name = str("Kate")
age = int(28)
is_active = bool(True)
subscription = None

print(f'{name}, {age}, {is_active}, {subscription}') # не надо в автопроверке

# task 9/15
length = "2.75"
width = "1.75"
area = float(length)*float(width)
show = f"With width {float(width)} and length {float(length)} of the room, its area is equal to {area}"

print(show) # не надо в автопроверке

# task 10/15
name = input("Your name? ")
email = input("Your email? ")
age = int(input("Your age? "))
height = float(input("Your height? "))
is_active = bool(input("Do you want a subscription? "))

print(f'{is_active}') # не надо в автопроверке

# task 11/15
length = float(input("Length of the room? "))
width = float(input("Width of the room? "))
area = length*width

print(f"With width {float(width)} and length {float(length)} of the room, its area is equal to {area}") # не надо в автопроверке

# task 12/15
my_list = []
my_list.insert(0, 2024)
my_list.insert(1, 'Python')
my_list.insert(2, 3.12)

print(my_list) # не надо в автопроверке

# task 13/15
my_list = [2024, 3.12]
some_data = ['Python']
my_list.extend(some_data)
my_list.insert(1, 'Python')
my_list.reverse()

print(my_list) # не надо в автопроверке

# task 14/15
data = {}
data = {'year':2024, 'lang':'Python', 'version':3.12}

print(data) # не надо в автопроверке

# task 15/15
cat = {}
info = {"status": "vaccinated", "breed": True}
cat = {"nick":"Vasya", "age":17, "characteristics":["лагідний", "грайливий", "муркотун"]}
age = cat.get("age")
cat.update(info)

print(age)
print(cat)