from tkinter import *

root = Tk()
root.geometry("600x300")
bg = PhotoImage(file="imagem_de_exemplo.png")

canvas1 = Canvas(root, width=400, height=400)
canvas1.pack(fill="both")
canvas1.create_image(0, 0, image=bg, anchor="nw")


root.mainloop()
