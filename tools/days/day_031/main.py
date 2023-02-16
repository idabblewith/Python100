# Day 31
# Updated 2023, Jarid Prince

from days.day_031.files.helpers import *


def day_031():
    # FUNCTION DEFINITIONS

    # Removing known word from words to learn
    def check_remove():
        global fc_current_card
        to_learn.remove(fc_current_card)
        data = pandas.DataFrame(to_learn)
        data.to_csv("./tools/days/day_031/files/words_to_learn.csv", index=False)
        loop()

    # Centers the Application Window
    def center_window(width=900, height=800):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window.geometry("%dx%d+%d+%d" % (width, height, x, y))

    # Fills in the card with a random choice from to_learn csv
    def set_current_card():
        global fc_current_card
        fc_current_card = random.choice(to_learn)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=fc_current_card["French"], fill="black")
        canvas.itemconfig(card_bg, image=card_front_img)
        return fc_current_card

    # Prepares next card
    def next_card():
        global fc_flip_timer
        global fc_current_card
        window.after_cancel(fc_flip_timer)
        fc_current_card = set_current_card()
        return fc_current_card

    # Flips the card after given time (4000 ms here)
    def set_flip_timer():
        # global fc_current_card
        global fc_flip_timer
        fc_flip_timer = window.after(4000, flip_card)
        return fc_flip_timer

    # Sets variables on card for the corresponding values on the back
    def flip_card():
        global fc_current_card
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=fc_current_card["English"], fill="white")
        canvas.itemconfig(card_bg, image=card_back_img)

    # Main loop which calls above functions
    def loop():
        global fc_flip_timer
        window.after_cancel(fc_flip_timer)
        global fc_current_card
        fc_current_card = next_card()
        fc_flip_timer = set_flip_timer()
        return fc_current_card, fc_flip_timer

    # MAIN
    title("FLASH CARDS")

    # Read in appropriate CSV files
    try:
        data = pandas.read_csv("./tools/days/day_031/files/words_to_learn.csv")
    except FileNotFoundError:
        unaltered_data = pandas.read_csv("./tools/days/day_031/files/french_words.csv")
        to_learn = unaltered_data.to_dict(orient="records")
    else:
        to_learn = data.to_dict(orient="records")

    # Configure window & canvas
    window = Tk()
    window.title("Flashcard App")
    window.lift()
    window.attributes("-topmost", True)
    window.after_idle(window.attributes, "-topmost", False)
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    card_front_img = PhotoImage(file="./tools/days/day_031/files/card_front.png")
    card_back_img = PhotoImage(file="./tools/days/day_031/files/card_back.png")
    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_bg = canvas.create_image(400, 263, image=card_front_img)
    card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
    card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
    canvas.grid(row=0, column=0, columnspan=2)

    # Preparing buttons
    dont_know_img = PhotoImage(file="./tools/days/day_031/files/wrong.png")
    dont_know_btn = Button(
        image=dont_know_img, highlightthickness=0, borderwidth=0, command=loop
    )
    dont_know_btn.grid(row=1, column=0)

    know_img = PhotoImage(file="./tools/days/day_031/files/right.png")
    know_btn = Button(
        image=know_img, highlightthickness=0, borderwidth=0, command=check_remove
    )
    know_btn.grid(row=1, column=1)

    # Center after configuration
    center_window()

    # Begin loop
    global fc_current_card
    fc_current_card = set_current_card()
    global fc_flip_timer
    fc_flip_timer = set_flip_timer()
    fc_current_card, fc_flip_timer = loop()

    window.mainloop()
