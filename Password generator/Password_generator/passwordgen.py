import random as rd

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOL = ['&', '#', '@', "%", "$", '-', '_', '=', '+', '^', '>', '<']

FIRST = rd.randint(1, 9)
SECOND = rd.randint(1, 9)
THIRD = rd.randint(1, 9)
FOURTH = rd.randint(1, 9)
FIRST_L = rd.choice(LETTERS)
SECOND_L = rd.choice(LETTERS)
THIRD_L = rd.choice(LETTERS)
FOURTH_L = rd.choice(LETTERS)
SYMBOL1 = rd.choice(SYMBOL)
SYMBOL2 = rd.choice(SYMBOL)

pwd = str(FIRST) + str(SECOND) + str(SYMBOL1) + str(THIRD) + str(FIRST_L) + str(SECOND_L) + str(SYMBOL2) + str(FOURTH) + THIRD_L + FOURTH_L


pwdn = input("Name of pwd: ")

with open(f'{pwdn}.pwd', 'x') as pwdf:
    pwdf.write(str(pwd)) 


print("We have generated a random password with letters, numbers and symbols for you!")
print(f'Password: {pwd} and in lowercase {pwd.lower()}')

