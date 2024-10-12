import random

num = random.randint(1,100)
print("guess what num i am thinking")
guess = -1
while(guess != num):
    guess = int(input("Enter the num: "))
    if guess < num:
        print("higher number please")
    elif guess > num:
        print("lower number please")

print("you are genius you guessed my num")