"""
import tkinter as tk

root = tk.Tk()
root.title("GUI tkinter")
#root.iconbitmap("image.ico")
root.geometry("640x480")
root.resizable(True,True)
root.minsize(320,240)
root.maxsize(1920,1080)

label_title = tk.Label (root, text = "Hellow Student!",
                        font=("Arial", 10, "bold italic"),
                        fg='#8B0000',
                        bg='#E9967A',
                        width=28,
                        height=3,
                        anchor="center",
                        relief="solid",
                        bd=5,
                        justify="center",)


label_title.pack()

button_play = tk.Button (master=root,
                         text="Click me!",
                         font=("Arial", 10, "bold italic"),
                         fg='#8B0000',
                         bg='#E9967A',
                         width=30,
                         height=3,
                         anchor="center",
                         relief="solid",
                         bd=5,)
button_play.pack()

img = tk.PhotoImage(file="img.gif")
label_img = tk.Label (master=root,
                      image=img,
                      )
label_img.pack()

root.mainloop()
"""


