import tkinter as tk

desserts = [
    {"hint": "Він зроблений із лимона і тіста", "answer": "лимонний пиріг", "image": "lemon_pie.png"},
    {"hint": "Холодний десерт з молока і цукру", "answer": "морозиво", "image": "icecream.png"},
    {"hint": "Солодкий десерт з кремом і коржами", "answer": "торт", "image": "cake.png"}
]

current = 0

def check():
    guess = entry.get().lower()

    if guess == desserts[current]["answer"]:
        result.config(text="Правильно! ")

        img = tk.PhotoImage(file=desserts[current]["image"])
        image_label.config(image=img)
        image_label.image = img

    else:
        result.config(text="Неправильно, спробуй ще")

def next_dessert():
    global current
    current += 1

    if current < len(desserts):
        hint.config(text=desserts[current]["hint"])
        entry.delete(0, tk.END)
        result.config(text="")
        image_label.config(image="")
    else:
        hint.config(text="Гра завершена ")

window = tk.Tk()
window.title("Вгадай десерт")
window.geometry("400x350")

title = tk.Label(window, text="Вгадай який десерт я купила")
title.pack()

hint = tk.Label(window, text=desserts[current]["hint"])
hint.pack()

entry = tk.Entry(window)
entry.pack()

check_btn = tk.Button(window, text="Перевірити", command=check)
check_btn.pack()

next_btn = tk.Button(window, text="Наступна загадка", command=next_dessert)
next_btn.pack()

result = tk.Label(window, text="")
result.pack()

image_label = tk.Label(window)
image_label.pack()

window.mainloop()