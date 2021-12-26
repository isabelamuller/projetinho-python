from tkinter import *
import tkinter as tk

app = tk.Tk()
app.geometry('500x200')
app.title('short story maker')
name_var = tk.StringVar()
animals_var = tk.StringVar()
profession_var = tk.StringVar()
place_var = tk.StringVar()


def opcoes1():
    name = name_var.get()
    animals = animals_var.get()
    profession = profession_var.get()
    place = place_var.get()

    print(
        'hello ' + name + '! i am here today to tell you a story about a ' + animals + ' who worked as a ' + profession + '. this ' + animals + ' was born in ' + place + '! can you imagine that?!')

    name_var.set("")
    animals_var.set("")
    profession_var.set("")
    place_var.set("")


def opcoes2():

    name = name_var.get()
    animals = animals_var.get()
    profession = profession_var.get()
    place = place_var.get()

    print(
        'hi my friend ' + name + '! what if i told you i know a story about a ' + animals + '? okay okay, ' + 'i guess everyone knows a story about a ' + animals + '... but what if i told you this ' + animals + ' was born in ' + place + '? even better, what if i told you' + ' hes also a ' + profession + '? pretty cool right?')

    name_var.set("")
    animals_var.set("")
    profession_var.set("")
    place_var.set("")



name_label = tk.Label(app, text='enter your name: ', font=('calibre', 20, 'bold'))
name_entry = tk.Entry(app, textvariable=name_var, font=('arial 15'))

animals_label = tk.Label(app, text='enter an animal: ', font=('calibre', 20, 'bold'))
animals_entry = tk.Entry(app, textvariable=animals_var, font=('arial 15'))

profession_label = tk.Label(app, text='enter a profession: ', font=('calibre', 20, 'bold'))
profession_entry = tk.Entry(app, textvariable=profession_var, font=('arial 15'))

place_label = tk.Label(app, text='enter a city: ', font=('calibre', 20, 'bold'))
place_entry = tk.Entry(app, textvariable=place_var, font=('arial 15'))

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
animals_label.grid(row=1, column=0)
animals_entry.grid(row=1, column=1)
profession_label.grid(row=2, column=0)
profession_entry.grid(row=2, column=1)
place_label.grid(row=3, column=0)
place_entry.grid(row=3, column=1)


Button(app, text='story #1', font='arial 15', command=opcoes1, bg='ghost white').place(x=10, y=140)
Button(app, text='story #2', font='arial 15', command=opcoes2, bg='ghost white').place(x=120, y=140)

app.mainloop()
