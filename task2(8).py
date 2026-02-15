a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
action = input("Введіть дію яку потрібно зробити (+, -, *, / ): ")
if action == "+":
    print(a + b)
elif action == "-":
    print(a - b)
elif action == "*":
    print(a * b)
elif action == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        print(a / b)
else:
    print("Невірна вийшла дія. Спробуйте ще раз! ")