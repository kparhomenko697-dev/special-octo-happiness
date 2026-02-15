import random
number = random.randint(1, 10)
attempt = 1
while attempt <= 3:
    guess = int(input("Вгадайте число: "))
    if guess == number:
        print("Ви вгадали число!")
        break
    else:
        if guess > number:
            print("Менше число виберіть")
        else:
            print("Більше число виберіть")
    attempt = attempt + 1
    if guess != number:
     print("Ви не вгадали число")
