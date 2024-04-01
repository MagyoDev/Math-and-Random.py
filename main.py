# Square root
import math, random

N = float(input("Number: "))
print("Square root:")
R = math.sqrt(N)
print("The root of {} is equal to {:.2f}".format(N, R),'\n')

# Factorial
print("Factorial:")
F = math.factorial(int(N))
print("The factorial is {}".format(F),'\n')

#Square root and Factorial
print("Square root and Factorial:")
FR = math.factorial(int(math.sqrt(N)))
print(FR,'\n')

#Random
print("Random")
NUM = random.randint(1,10)
print(NUM)

