import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter = int(input("How many letters, would like to have in your password: "))
number = int(input("How many numbers, would like to have in your password: "))
symbol = int(input("How many symbols, would like to have in your password: "))
lis=[]

for i in range(1,letter+1):
    lis.append(random.choice(letters))
for j in range(1,number+1):
    lis.append(random.choice(numbers))
for k in range(1,symbol+1):
    lis.append(random.choice(symbols))

random.shuffle(lis)
print(lis)

password=" "
for char in lis:
    password+=char
print(f"Your Password is : {password}")