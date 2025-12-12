from tkinter import *
from tkinter.filedialog import askopenfilename
import numpy as np


char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # awalnya 26 karakter
def decrypt(x) :
    return char[x]
def encrypt(x) :
    return char.index(x)

def convert(msg, pw, l_msg, l_pw) :
    result = ''
    for i in range(0, l_msg) :
        key = i % l_pw
        if msg[i] in char :
            final = encrypt(msg[i]) + encrypt(pw[key]) + 1
            if final>25 :
                final = final%25-1
            result = result + decrypt(final)
        else :
            result = result + msg[i];
    return result

def encryption(plaintext) :
    #plaintext = "".join(str(entry1.get()).lower().strip().split(" "))
    kata = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    key_matrix = np.array([[5, 3], [3, 2]])
    # menentukan determinan matriks kunci
    determinant = round(np.linalg.det(key_matrix))
    # menentukan faktor reciprocal/kebalikan dari matriks kunci
    for i in range(1,26) :
        if ((determinant*i)%26==1) :
            reciprocal = i
            break

    # definisi matriks kunci untuk enkripsi
    if len(plaintext)%2!=0:
        plaintext += plaintext[-1]
    v = [0,0]
    i = 0
    encrypted_text = ""
    while i+1 <= len(plaintext) :
        if i%2!=0 :
            v = np.array([kata.index(plaintext[i-1]), kata.index(plaintext[i])])
            result = np.matmul(key_matrix, v)
            result = result%26
            encrypted_text = encrypted_text + kata[result[0]] + kata[result[1]]
        i += 1
    return encrypted_text


def btn_clicked():
    password = str(entry1.get()).lower()
    pw_len = len(password)
    raw_file = open(file_name, "r")
    plain_list = raw_file.readlines()
    encrypted_list = []
    for s in plain_list:
        s = "".join(s.lower().strip().split(" "))
        txt = encryption(s)
        str_len = len(txt)
        ciphertext = convert(txt, password, str_len, pw_len)
        encrypted_list += [ciphertext]
    raw_file.close()
    encrypted_file = open("{} - encrypted.txt".format(file_name), "w")
    for x in encrypted_list:
        encrypted_file.write("{}\n".format(x))
    encrypted_file.close()
    text.set("OK - file anda dienkripsi dengan aman")

def submit():
    global file_name
    file_name = askopenfilename()


window = Tk()

text = StringVar()
text.set('')

window.title("Hill Cipher App - An App By Fikri Mulyana Setiawan")
window.geometry("804x386")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 386,
    width = 804,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    608.0, 312.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0, textvariable=text)

entry0.place(
    x = 474.0, y = 266,
    width = 268.0,
    height = 90)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    344.0, 193.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 549, y = 177,
    width = 118,
    height = 32)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    608.0, 138.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 474.0, y = 122,
    width = 268.0,
    height = 30)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = submit,
    relief = "flat")

b1.place(
    x = 98, y = 132,
    width = 205,
    height = 140)

window.resizable(False, False)
window.mainloop()
