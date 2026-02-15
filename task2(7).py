points = int(input("Введіть ваш бал: "))
if   points >= 0 and points <= 49:
    print("Незадовільно! Пройдіть ще раз!")
elif points >= 50 and points <= 69:
    print("Задовільно! Якщо бажаєте пройдіть ще раз!")
elif points >= 70 and points <= 89:
    print("Добре! Якщо бажаєте пройдіть ще раз!")
elif points >= 90 and points <= 100:
    print("Відмінно! На цей результат перездачі немає!")
else:
    print("Помилка! Спробуйте ще раз!")


