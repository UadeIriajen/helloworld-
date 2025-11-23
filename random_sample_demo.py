import random

cards = ["Queen","King","Jack"]

def main():
   random.seed(1)
   choice = random.sample(cards, k = 2)
   print(choice)
main()