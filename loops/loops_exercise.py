##### for loops: exercise
## question 1
number = int(input("Enter a number: "))

for i in range(1,number+1):
    multiplication = number * i
    print(f"{number} * {i} = {multiplication}")

## question 2
number = int(input("Enter a number: "))
sum = 0

for i in range(number+1):
    sum = sum + i

print(sum)

## question 3
my_list = [-3, -5, 9, 1]
sum = 0
for item in my_list:
    sum += item

print(sum)

## question 4
mailing_list = [
["Chilli", "chilli@thechihuahua.com"],
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Ivy", "noreply@goldendreamers.xyz"],
]

for item in mailing_list:
    # e.g. item = ["Chilli", "chilli@thechihuahua.com"]
    name = item[0]
    email = item[1]
    print(f"{name}: {email}")

##### while loops: exercise
## question 1
number = 0
sum = 0

while number != "":
    sum += int(number)
    number = input("Enter a number: ")
    
print(sum)

## Alternative using 'break' to avoid inconsistency in the typing of number. 
## Note: We haven't covered this!
sum = 0
while True:
    number = input("Enter a number: ")

    if number == "":
        break
    else:
        sum += int(number)

print(sum)

## question 2
number = int(input("Enter a number: "))
counter = 1

while counter <= number:
    print(counter)
    counter += 2

## alternative 1
number = int(input("Enter a number: "))

counter = 0
while counter <= number:
    if counter % 2 == 1:
        print(counter)
    counter += 1

## alternative 2
number = int(input("Enter a number: "))

for i in range(1,number+1,2):
    print(i)

## question 3
correct_number = 27
number = 0

while number != correct_number:
    number = int(input("Guess the number: "))

    if number > correct_number:
        print("Too high!")
    elif number < correct_number:
        print("Too low!")
    elif number == correct_number: # or just 'else'
        print("Correct!")

### Loops: Exercises (Extension)
## question 1
groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]

for item in groceries:
    # e.g. item = ["Baby Spinach", 2.78]
    name = item[0] # Baby Spinach
    num_units = int(input(f"How many {name}?: "))
    item.append(num_units)

print("===Izzy's Food Emporium===")
total_sum = 0
for item in groceries:
    # e.g. item = ["Baby Spinach", 2.78, 1]
    item_cost = item[1] * item[2]
    total_sum += item_cost
    print(f"{item[0]} \t ${item_cost:.2f}")
print("============================")
print(f"\t \t ${total_sum:.2f}")

## question 2
response = input("Please enter a string: ")

for i in range(len(response)):
    print(f"{i} {response[i]}")

## alternative
response = input("Please enter a string: ")

counter = 0
for letter in response:
    print(f"{counter} {letter}")
    counter += 1

## question 3
size = int(input("Pyramid size: "))

for i in range(1, size+1):
    pyramid_row = "*" * i
    print(pyramid_row)

## question 4
size = int(input("Pyramid size: "))

for i in range(1, size+1):
    pyramid_row = "*" * (i*2 - 1)
    padding_row = " " * (size - i)
    print(f"{padding_row}{pyramid_row}{padding_row}")