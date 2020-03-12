from tkinter import *
from tkinter.ttk import *

import json

def save_to_file(name, j):
    print("write")
    with open("output/{}.json".format(name), "w") as f:
        enc = json.dumps(j, indent=2, ensure_ascii=False)
        f.write(enc)

def save_to_json():
    name     = name_text_box.get()
    kinryoku = kinryoku_text_box.get()
    power    = power_text_box.get()
    chikara  = chikara_text_box.get()
    yasei    = yasei_text_box.get()
    banana   = banana_text_box.get()
    GP       = GP_text_box.get()
    HP       = HP_text_box.get()
    if "" in [name, kinryoku, power, chikara, yasei, banana, GP, HP]:
        string_var.set("未入力の項目があります")
        return
    if kinryoku.isdecimal() and power.isdecimal() and chikara.isdecimal() \
        and yasei.isdecimal() and banana.isdecimal() and GP.isdecimal() \
        and HP.isdecimal():
        save_to_file(
            name,
            {
                "name": name,
                "kinryoku" : int(kinryoku),
                "power": int(power),
                "chikara" : int(chikara),
                "yasei": int(yasei),
                "banana": int(banana),
                "GP": int(GP),
                "HP": int(HP)
            }
        )
        string_var.set("{}を作成しました!".format(name))
        return
    string_var.set("名前以外は自然数で入力しください")

root = Tk()
root.title("ゴリラメイカー")
root.geometry("820x820")
frame = Frame(root)

name_label = Label(frame, text="ゴリラネーム")
name_text_box = Entry(frame, width=30)

name_label.pack()
name_text_box.pack()

kinryoku_label = Label(frame, text="筋力")
kinryoku_text_box = Entry(frame, width=30)

kinryoku_label.pack()
kinryoku_text_box.pack()

power_label = Label(frame, text="パワー")
power_text_box = Entry(frame, width=30)

power_label.pack()
power_text_box.pack()

chikara_label = Label(frame, text="力")
chikara_text_box = Entry(frame, width=30)

chikara_label.pack()
chikara_text_box.pack()

yasei_label = Label(frame, text="野生")
yasei_text_box = Entry(frame, width=30)

yasei_label.pack()
yasei_text_box.pack()

banana_label = Label(frame, text="バナナ")
banana_text_box = Entry(frame, width=30)

banana_label.pack()
banana_text_box.pack()

GP_label = Label(frame, text="GP")
GP_text_box = Entry(frame, width=30)

GP_label.pack()
GP_text_box.pack()

HP_label = Label(frame, text="HP")
HP_text_box = Entry(frame, width=30)

HP_label.pack()
HP_text_box.pack()

button = Button(frame, text="作成", command=save_to_json)

button.pack()

string_var = StringVar(value="")

error = Label(frame, textvariable=string_var)
error.pack()

frame.pack()
root.mainloop()
