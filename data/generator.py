#To Run: python generator.py [k]
# k = number of chars in the alphabet
# must be in \data directory in terminal

import random
import sys

#Validating Input
try:
    k = int(sys.argv[1])

except:
    print("Invalid Alphabet Size")
    quit()

if not (k>=1):
    print("Alphabet Size cannot be less than 1")
    quit()

if not (k<=26):
    print("Alphabet Size cannot be more than 26")
    quit()



#Initializing Alphabet
#Randomly generate list of letters

full_alphabet = "abcdefghijklmnopqrstuvwxyz"
full_alpha_list = list(full_alphabet)
k_alpha_list = random.sample(full_alpha_list,k)

#randomly generate value for each letter
k_value_list = [random.randint(0, 50) for _ in range(k)]


#randomly generate strings of at least length 25
a_length = random.randint(25, 35)
b_length = random.randint(25, 35)
a_list = [random.choice(k_alpha_list) for _ in range(a_length)]
b_list = [random.choice(k_alpha_list) for _ in range(b_length)]

a = ''.join(a_list)
b = ''.join(b_list)


#Writing File
with open(f"{k}_{k_alpha_list[0]}{k_value_list[0]}.in", 'w') as f:
    f.write(f"{k}\n")
    for letter in k_alpha_list:
        f.write(str(letter))
        f.write(" ")
        f.write(str(k_value_list[k_alpha_list.index(letter)]))
        f.write("\n")
    f.write(f"{a}\n")
    f.write(f"{b}")
