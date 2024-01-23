from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
        )
''')

conn.commit()

def save_data():
    name = name_entry.get()
    email = email_entry.get()
    cursor.execute("INSERT INTO user_data (name, email) VALUES(?,?)", (name, email))
    conn.commit()
    name_entry.delete(0, END)
    email_entry.delete(0, END)

def login_data():
    name = login_name_entry.get()
    email = login_email_entry.get()

    cursor.execute("SELECT * FROM user_data WHERE email=? AND name=?", (email,name))
    user = cursor.fetchone()

    if user:
        login_window.withdraw()
        root.deiconify()
    else:
        messagebox.showerror("Error", "User email not found")

def logout():
    root.withdraw()

root = Tk()
root.title("Data Entry")
root.config(padx=50, pady=50)

name_label = Label(text="Name:")
name_label.pack()
name_entry = Entry()
name_entry.pack()

email_label = Label(text="Email: ")
email_label.pack()
email_entry = Entry()
email_entry.pack()

save_button = Button(text="Save", command=save_data)
save_button.pack()

logout_button = Button(text="Logout", command=logout)
logout_button.pack()

root.withdraw()

login_window = Toplevel()
login_window.title("Login Page")
login_window.config(pady=50, padx=50)

login_email_label = Label(login_window, text="Email: ")
login_email_label.pack()
login_email_entry = Entry(login_window)
login_email_entry.pack()

login_name_label = Label(login_window, text="Name: ")
login_name_label.pack()
login_name_entry = Entry(login_window)
login_name_entry.pack()

login_button = Button(login_window, text="Login", command=login_data)
login_button.pack()

root.mainloop()
conn.close()