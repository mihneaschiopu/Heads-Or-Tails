import random
heads = 0
tails = 0

for x in range(0, 10000):

    num = random.randrange(0, 2)

    if (num == 0):
        heads += 1
    else:
        tails += 1




print (" You got Heads", heads, " You got Tails", tails)
