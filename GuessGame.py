# Guess the number from 1-10.

import random
n = random.randint(1,10)

l = 1
h = 10
attempts = 0

while l <= h:
  guess = int(input("Enter number(b/w 1-10) : "))
  attempts += 1
  
  if guess < n:
    print("Your guess is small, Enter a larger number : ")
    l = guess + 1
  elif guess > n:
    print("guess is large,enter a smaller number")
            h = guess - 1
  else:
            print(f"BINGO!!!-Correct guess in {attempts} attempts")
            break
    
