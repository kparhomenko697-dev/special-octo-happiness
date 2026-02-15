n = int(input("Введіть любе число: "))
result = 1
i = 1
while i <= n:
    result = result * i
    i = i + 1
print("Факторіал:", result)