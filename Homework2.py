# task 1/13
is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
else:
    is_next = False

print(f'{is_next}')  # не надо в автопроверке

# task 2/13
work_experience = int(input("Enter your full work experience in years: "))
developer_type = ""
if work_experience <= 1:
    developer_type = "Junior"
elif (work_experience > 1 and work_experience <= 5):
    developer_type = "Middle"
else:
    developer_type = "Senior"

print(f'{developer_type}') # не надо в автопроверке

# task 3/13
num = int(input("Enter a number: "))
result = ""
if num > 0:
    if num%2 == 0:
        result = "Positive even number"
    else:
        result = "Positive odd number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"

print(f'{result}') # не надо в автопроверке

# task 4/13
num = int(input("Enter the integer (0 to 100): "))
sum = 0

while num >= 0:
    sum=sum+num
    num-=1

print(f'{sum}') # не надо в автопроверке

# task 5/13
message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for ch in message:
    if ch == search:
        result+=1

print(f'{result}') # не надо в автопроверке

# task 6/13
pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = int(pool/quantity)
except ZeroDivisionError:
    print('Divide by zero completed!')

# task 7/13
def greeting():
    print("Hello world!")    

greeting()

# task 8/13
def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"

# task 9/13
def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price*(1-discount)
    apply_discount()
    return price

# task 10/13
def get_fullname(first_name, last_name, middle_name=""):
    if middle_name:
        return f'{first_name} {middle_name} {last_name}'
    else:
        return f'{first_name} {last_name}'

# task 11/13
def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        spaces = " "*((length - len(string)) // 2)
        return f'{spaces}{string}'
    
# task 12/13
def first(size, *params):
    return size+len(params)

def second(size, **params):
    return size+len(params)

# task 13/13
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    return int(factorial(n)/(factorial(n-k)*factorial(k)))