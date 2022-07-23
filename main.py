

import random
from random import *
from tkinter import *
from tkinter.messagebox import *
from string import *
from json import *
import pyperclip

email="abenezerangel@gmail.com"





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
uppercase=ascii_uppercase
lowercase=ascii_lowercase
numbers="0123456789"


printable=printable[:-6]
printer=numbers+uppercase+lowercase+punctuation



def generate_password():
    num_lower = randint(5, 8)
    num_upper = randint(3, 5)
    num_numbers = randint(2, 4)
    num_punctuation = randint(2, 4)

    pwd=password_entry.get()
    if len(pwd)!=0:

        password_entry.delete(0,len(pwd))
    ult_list=[choice(lowercase) for _ in range(num_lower)]+[choice(uppercase) for _ in range(num_upper)] + [choice(numbers) for _ in range(num_numbers)] + [choice(punctuation) for _ in range(num_punctuation)]
    print(ult_list)
    # we will only use this if we need maximum security until then a normal password should look like the above
    # shuffle(ult_list)
    print(ult_list)
    password="".join(ult_list)


    print(password)

    password_entry.insert(0,password)
    password_entry.clipboard_clear()
    password_entry.clipboard_append(password)


def search():
    website=website_form.get()
    try:
        with open("password.json") as reader:
            data = load(reader)
    except:
        with open("password.json",mode="w")as writer:
            print("Created file 'password.json'")


    datal = list(data)
    print(datal)
    i = len(datal)


    if len(website)==0:
      while i>0:

        info=choice(datal)
        result=askyesno("Field left blank",f"Is this what you are looking for:\n{info}")
        print(result)
        if result and i >0:
            yes=askyesno(info,f"Is this the one? :{data[info]}")
            if yes:
                website_form.insert(0, info)
                website_form.select_range(0, END)
                pyperclip.copy(data[info]["Password"])
                i=0
            else:
                i-=1
        else:
                i-=1




    else:
        try:
            showinfo(website,data[website])
        except KeyError:
            showinfo("No Such Data","The given website doesn't seem to exist in our database.")




# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password_keypress(event):
    if len(password_entry.get())==0:
        generate_password()
        return
    web=str(website_form.get())
    email_address=email_entry.get()
    print(email_address)
    pwd= password_entry.get()
    print(pwd)

    if len(web)!=0 and len(email_address)!=0 and len(pwd)!=0:
        result=askokcancel("Save message",f"Are sure you want to save the following information:\n                            Website: {web} \n                   Email: {email_address} \n                         Password: {pwd}" )
        if result:
            try:
                with open("password.json") as reader:
                    data = load(reader)
                    data.update({web: {"Email": email_address, "Password": pwd}})
                with open("password.json",mode="w") as writer:
                    dump(data, writer,indent=4)


            except (FileNotFoundError,JSONDecodeError):
                with open("password.json",mode="w") as writer:
                    dump({web: {"Email": email_address, "Password": pwd}},writer,indent=4)
            website_form.delete(0, len(web))

            email_entry.delete(0, len(email_address))

            password_entry.delete(0, len(pwd))

            website_form.focus()
            email_entry.insert(0, email)

    else:
        showerror("Missing information","Information still missing, some fields were left blank. Fill the remaining blanks")


def add_password_button():

    web = str(website_form.get())
    email_address = email_entry.get()
    print(email_address)
    pwd = password_entry.get()
    print(pwd)

    if len(web) != 0 and len(email_address) != 0 and len(pwd) != 0:
        result = askokcancel("Save message",
                          f"Are sure you want to save the following information:\n                            Website: {web} \n                   Email: {email_address} \n                         Password: {pwd}")
        if result:
            try:
                with open("password.json") as reader:
                    data = load(reader)
                    data.update({web: {"Email": email_address, "Password": pwd}})
                with open("password.json", mode="w") as writer:
                    dump(data, writer,indent=4)


            except (FileNotFoundError,JSONDecodeError):
                with open("password.json",mode="w") as writer:
                    dump({web: {"Email": email_address, "Password": pwd}}, writer,indent=4)

            website_form.delete(0, len(web))

            email_entry.delete(0, len(email_address))

            password_entry.delete(0, len(pwd))

            website_form.focus()
            email_entry.insert(0, email)

    else:
        showerror("Missing information",
                  "Information still missing, some fields were left blank. Fill the remaining blanks")


def email_focus(event):
    if len(email_entry.get())!=0:
        email_entry.select_range(0,END)
    email_entry.focus()

def password_focus(event):
    if len(password_entry.get())!=0:
        password_entry.delete(0,END)
    password_entry.focus()








# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=10,pady=10)
canvas=Canvas(window,width=200, height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(125,100,image=logo)
canvas.grid(column=1,row=0,padx=10,pady=10)
Label(text="Website:").grid(row=1,column=0)
Label(text="Email/Username:").grid(row=2,column=0)
Label(text="Password:").grid(row=3,column=0)
website_form=Entry(width=47,highlightthickness=0)
website_form.focus()
website_form.grid(column=1,row=1,padx=0,ipadx=0,sticky=W,columnspan=2)
website_form.bind("<KeyPress-Return>",email_focus)
search=Button(text="Search",width=6,command=search).grid(column=2,padx=0,row=1,sticky=E)

email_entry=Entry(width=56)
email_entry.bind("<KeyPress-Return>",password_focus)
email_entry.grid(column=1,row=2,columnspan=2,sticky=W)
email_entry.insert(0,email)
password_entry=Entry(width=37,borderwidth=1)
password_entry.grid(column=1,row=3,padx=0,sticky=W)
print(len(password_entry.get()))
password_entry.bind("<Return>",add_password_keypress)

generator=Button(text= "Generate Password",width=14,command =generate_password,borderwidth=1)
generator.grid(column=2,row=3,sticky=EW,padx=0)
add=Button(text="Add",width=46,borderwidth=1 , command=lambda: add_password_button())
add.grid(column=1,row=4,columnspan=2,sticky=EW)


window.mainloop()