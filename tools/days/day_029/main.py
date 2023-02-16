# Day 29
# Updated 2023, Jarid Prince

from days.day_029.files.helpers import *


def day_029():
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def generate_password():
        # Manual definition (also can use string.printable)
        letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers
        shuffle(password_list)

        password = "".join(password_list)
        passin.insert(0, password)
        pyperclip.copy(password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def save_data():
        website = webin.get()
        email = emailin.get()
        password = passin.get()

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Opps", message="Please fill in all fields")
        else:
            is_ok = messagebox.askokcancel(
                title=website,
                message=f"These are the details entered:\nEmail: {email}"
                f"\nPassword: {password}\nIs it ok to save?",
            )
            if is_ok:
                with open("./tools/days/day_029/files/data.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password}\n")
                    webin.delete(0, END)
                    passin.delete(0, END)

    # ---------------------------- UI SETUP ------------------------------- #
    title("PASS MANAGER")
    window = Tk()
    window.title("Password Generator")
    logo = PhotoImage(file="./tools/days/day_029/files/logo.png")
    window.lift()
    window.attributes("-topmost", True)
    window.after_idle(window.attributes, "-topmost", False)
    window.iconphoto(True, logo)
    window.config(padx=50, pady=50)

    canvas = Canvas(width=200, height=200)
    canvas.create_image(100, 100, image=logo)
    canvas.grid(row=0, column=1)

    website_ = Label(text="Website:")
    website_.grid(row=1, column=0)

    email_ = Label(text="Email/Username:")
    email_.grid(row=2, column=0)

    pass_ = Label(text="Password:")
    pass_.grid(row=3, column=0)

    webin = Entry(width=35)
    webin.grid(row=1, column=1, columnspan=2)
    webin.focus()
    emailin = Entry(width=35)
    emailin.grid(row=2, column=1, columnspan=2)
    emailin.insert(0, "base@outlook.com")
    passin = Entry(width=21)
    passin.grid(row=3, column=1)

    generatepass = Button(text="Generate Password", command=generate_password)
    generatepass.grid(row=3, column=2)
    add = Button(text="Add", width=36, command=save_data)
    add.grid(row=4, column=1, columnspan=2)
    # , columnspan=2
    window.mainloop()
