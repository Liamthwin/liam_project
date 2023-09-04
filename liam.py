import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Kaung Htet Kyaw school", foreground="red", background="black")
greeting.pack()

myfirst = label = tk.Label(text="Sign up", width=10, height=5, )
myfirst.pack()

first_name = tk.Entry()
first_name.pack()
print(first_name.get())

last_name = tk.Entry()
last_name.pack()

gmail = tk.Entry()
gmail.pack()

password = tk.Entry()
password.pack()

Gender = tk.Entry()
Gender.pack()
def get_first_name():
    print("First name:", first_name.get())
    print("Last name:", last_name.get())
    print("Gmail:", gmail.get())
    print("Password:", password.get())
    print("Gender:", Gender.get())

button = tk.Button(
    text="Sign up",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=get_first_name,
)
button.pack()

window.mainloop()


    




