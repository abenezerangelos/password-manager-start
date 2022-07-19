from tkinter import *





# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=10,pady=10)
canvas=Canvas(window,width=200, height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(130,100,image=logo)
canvas.grid(column=1,row=0,padx=10,pady=10)
website=Label(text="Website:")
website.grid(row=1,column=0)
email=Label(text="Email/Username:")
email.grid(row=2,column=0)
password=Label(text="Password:")
password.grid(row=3,column=0)
website_form=Entry(width=57)
website_form.grid(column=1,row=1,columnspan=2)
email_entry=Entry(width=57)
email_entry.grid(column=1,row=2,columnspan=2)
password_entry=Entry(width=37,borderwidth=1)
password_entry.grid(column=1,row=3,padx=2)
generator=Button(text= "Generate Password",width=15)
generator.grid(column=2,row=3,padx=3)
add=Button(text="Add",width=48)
add.grid(column=1,row=4,columnspan=2)
window.mainloop()
