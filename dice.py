import random

sides = int(input("How many sides? "))

rolls = int(input("How many rolls? "))

for i in range(rolls):
    n = random.randrange(1, (sides + 1))
    print(n)

