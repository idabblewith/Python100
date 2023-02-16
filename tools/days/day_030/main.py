# Day 30
# Updated 2023, Jarid Prince

from days.day_030.files.helpers import *


def day_030():
    def generate_password():
        AVAIL_CHAR = [char for char in string.printable]
        NUMBER = AVAIL_CHAR[:10]
        LOWER = AVAIL_CHAR[10:36]
        ALPHA = AVAIL_CHAR[36:62]
        SYMBOL = AVAIL_CHAR[62:-6]
        # Removed problematic characters
        SYMBOL.remove("\\")
        SYMBOL.remove("`")
        SYMBOL.remove('"')
        SYMBOL.remove(";")

        selected_characters = int(pw_var.get())
        if selected_characters == 10:
            alphabet_amount = int(2)
            numbers_amount = int(3)
            symbols_amount = int(3)
            caps_amount = int(2)
        elif selected_characters == 12:
            split_amount = selected_characters / 4
            alphabet_amount = int(split_amount)
            numbers_amount = int(split_amount)
            symbols_amount = int(split_amount)
            caps_amount = int(split_amount)
        elif selected_characters == 16:
            alphabet_amount = int(3)
            numbers_amount = int(4)
            symbols_amount = int(6)
            caps_amount = int(3)

        new_pass_array = []

        for _each_number in range(1, numbers_amount + 1):
            new_pass_array.append(random.choice(NUMBER))
        for _each_letter in range(1, alphabet_amount + 1):
            new_pass_array.append(random.choice(LOWER))
        for _each_symbol in range(1, symbols_amount + 1):
            new_pass_array.append(random.choice(SYMBOL))
        for _each_caps in range(1, caps_amount + 1):
            new_pass_array.append(random.choice(ALPHA))

        random.shuffle(new_pass_array)
        new_pass = ""

        for character in new_pass_array:
            new_pass += character

        passin.delete(0, END)
        passin.insert(0, new_pass)
        pyperclip.copy(new_pass)

    # ---------------------------- SAVE PASSWORD ------------------------------- #

    def save_data():
        website = webin.get().capitalize()
        email = emailin.get()
        password = passin.get()
        new_entry = {website: {email: {"password": password}}}
        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Opps", message="Please fill in all fields")
        else:
            is_ok = messagebox.askokcancel(
                title=website,
                message=f"These are the details entered:\nEmail: {email}"
                f"\nPassword: {password}\nIs it ok to save?",
            )
            if is_ok:

                try:
                    with open("./tools/days/day_030/files/data.json", "r") as data_file:
                        # json.dump(new_entry, data_file, indent=4) #w
                        data = json.load(data_file)  # r
                except FileNotFoundError:
                    with open("./tools/days/day_030/files/data.json", "w") as data_file:
                        json.dump(new_entry, data_file, indent=4)  # w
                except JSONDecodeError as a:
                    with open("./tools/days/day_030/files/data.json", "w") as data_file:
                        json.dump(new_entry, data_file, indent=4)  # w
                else:
                    try:
                        data[website][email] = {"password": password}
                    except KeyError as e:
                        data.update(new_entry)
                    finally:
                        with open(
                            "./tools/days/day_030/files/data.json", "w"
                        ) as data_file:
                            json.dump(data, data_file, indent=4)  # w
                finally:
                    webin.delete(0, END)
                    passin.delete(0, END)

    # ---------------------------- Search ------------------------------- #

    def search():
        try:
            website = webin.get().capitalize()
            em = emailin.get()
            with open("./tools/days/day_030/files/data.json", "r") as data_file:
                try:
                    data = json.load(data_file)
                except:
                    messagebox.showwarning(
                        title="Empty File",
                        message="The file is empty. Create some passwords first.",
                    )
                else:
                    try:
                        for user in data[website]:
                            # print(str(user))
                            # print(str(em))
                            # print(em == user)
                            if str(user) == str(em):
                                messagebox.showinfo(
                                    title=website,
                                    message=f'{website} Credentials\n\nEmail:\t\t{user}\nPassword:\t{data[website][user]["password"]}',
                                )
                    except KeyError as e:
                        print(e)
                        messagebox.showwarning(
                            title="No Website Found",
                            message="That website does not exist. Try again.",
                        )
        except FileNotFoundError:
            with open("./tools/days/day_030/files/data.json", "w") as data_file:
                data_file.write("")
            search()
        except Exception as e:
            print(e)

    # ---------------------------- UI SETUP ------------------------------- #
    title("PASSWORD MANAGER PRO")
    window = Tk()
    window.title("Password Manager")
    logo = PhotoImage(file="./tools/days/day_030/files/logo.png")
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
    webin.grid(row=1, column=1)
    webin.focus()
    emailin = Entry(width=35)
    emailin.grid(row=2, column=1)
    emailin.insert(0, "base@outlook.com")
    passin = Entry(width=35)
    passin.grid(row=3, column=1)

    search_b = Button(text="Search Website", command=search)
    search_b.grid(row=1, column=2)
    generatepass = Button(text="Create Password", command=generate_password)
    generatepass.grid(row=3, column=2)
    add = Button(text="Add", width=43, command=save_data)
    add.grid(row=4, column=1, columnspan=2)

    pw_choices = [10, 12, 16]
    pw_var = StringVar(window)
    pw_var.set(10)
    pw_choice_selector = OptionMenu(window, pw_var, *pw_choices)
    pw_choice_selector.grid(row=2, column=2, sticky="ew")

    window.mainloop()
