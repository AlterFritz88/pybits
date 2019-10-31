import random


for i in range(1000):
    random.seed(i)
    a = random.randint(0, 10)
    if a == 5:
        print(i)
        break