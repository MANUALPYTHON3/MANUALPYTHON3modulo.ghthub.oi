#Este código imprimirá 10 números aleatorios entre 1 y 100.

#ramdom
import random

for i in range(10):
    print(random.randint(1, 100))





#Este código imprimirá las 26 letras minúsculas del alfabeto.
#string
import string

for letra in string.ascii_lowercase:
    print(letra)


#Este código creará una ventana con 10 etiquetas, cada una con un número del 0 al 9.

#tkinter

from tkinter import Tk, Label

root = Tk()

for i in range(10):
    label = Label(root, text=str(i))
    label.pack()

root.mainloop()

