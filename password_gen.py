
import random

print("------PASSWORD GENERATOR------")

pwd_count=int(input("Enter the Number of password do you  needed :"))
pwd_chars=int(input("Enter the length of your  password :"))


password='''ABCDEFGHIJKLMNOPQRSTUVWXYZ\n
abcdefghijklmnopqrstuvwxyz\n
0123456789\n!@#$%&'''

print("\nThe Password is :-")
print("-----------------------")


for i in range(pwd_count):
    pass_word=""
   
    for x in range(pwd_chars):
        pass_word=pass_word+random.choice(password)

    print("Password#"+str(i+1)+": "+pass_word)    

print("-----------------------")
print("your password is successfully generated :) \n")