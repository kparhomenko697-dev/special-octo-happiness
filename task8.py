from datetime import date

year = int(input("Введіть  будь ласка рік: "))
month = int(input("Введіть будь ласка  місяць: "))
day = int(input("Введіть будь ласка день: "))

today = date.today()
future = date(year, month, day)

difference = future - today
days = difference.days

months = days // 30
days_left = days % 30

print("До цієї дати залишилось:", months, "місяців і", days_left, "днів")
