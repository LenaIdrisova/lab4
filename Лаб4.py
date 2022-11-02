import random
import string
import tkinter as tk


def key_generation(pwd_length=4):
    UPPERCASE_CHARACTERS = string.ascii_uppercase
    DIGITS = string.digits

    combined_list = UPPERCASE_CHARACTERS + DIGITS

    rand_upper = random.choice(UPPERCASE_CHARACTERS)
    rand_digit = random.choice(DIGITS)

    temp_pwd = random.sample(combined_list, pwd_length - 2) + [rand_upper, rand_digit]
    random.shuffle(temp_pwd)
    password = "".join(temp_pwd)

    return password


summa = 0
key = (key_generation(pwd_length=4))
key_end = []

for a in key:
    summa +=key.find(a)+1

while len(key_end) < 3:
    summa = 0
    key = (key_generation(pwd_length=4))
    for a in key:
        summa += key.find(a) + 1

    if 3 < summa < 12:
        key_end.append(key)

key_end1 = key_end[0] + '-' + key_end[1] + '-' + key_end[2]


def clicked():
    lbl_result.configure(text=key_end1)


def close():
    window.destroy()


window = tk.Tk()
window.title("Key generation")
window.geometry('360x240')
bg = tk.PhotoImage(file='sunset.png')

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='c')

label_bg = tk.Label(frame, image=bg)
label_bg.place(x=0, y=0)

lbl_YK = tk.Label(frame, text='Your key:', font=("Arial", 15), bg='#999900')
lbl_YK.grid(column=0, row=0, padx=80, pady=80)

lbl_result = tk.Label(frame)
lbl_result.grid(column=2, row=0)

btn = tk.Button(frame, text='Generate', font=("Arial", 15), command=clicked)
btn.grid(column=0, row=3)
exit = tk.Button(frame, text='Cancel', font=("Arial", 15), command=close)
exit.grid(column=2, row=3)

window.mainloop()
