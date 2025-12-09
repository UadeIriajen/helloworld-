import random

def random_number ():
  number =  random.randint(1, 20)
  print("Take a guess between 1 and 20")
  attempt = 7

 
  while attempt > 0:
    guess = int(input("Your guess: "))
    if guess == number:
     print("Correct!")
     break 
    elif guess < number:
     print("Too low")
    else:
     print("Too high")

     attempt -= 1
     print(f"You have {attempt} left.\n")

     if attempt == 0:
      print(f"Game over! The number was {number}\n")
random_number()









    