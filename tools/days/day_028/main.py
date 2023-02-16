# Day 28
# Updated 2023, Jarid Prince

from days.day_028.files.helpers import *


def day_028():
    title("POMODORO")
    global pomodoro_reps
    pomodoro_reps = 0
    global pomodoro_timer
    pomodoro_timer = None

    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)
    window.lift()
    window.attributes("-topmost", True)
    window.after_idle(window.attributes, "-topmost", False)

    # ---------------------------- TIMER RESET ------------------------------- #
    def reset_timer():
        canvas.itemconfig(timer_text, text="00:00")
        completed_label.config(text="")
        global pomodoro_reps
        global pomodoro_timer
        window.after_cancel(pomodoro_timer)
        pomodoro_reps = 0
        timer_label.config(text="Timer", fg=GREEN)

    # ---------------------------- TIMER MECHANISM ------------------------------- #
    def start_timer():
        short_break_secs = SHORT_BREAK_MIN * 60
        long_break_secs = LONG_BREAK_MIN * 60
        work_secs = WORK_MIN * 60
        global pomodoro_timer
        global pomodoro_reps
        pomodoro_reps += 1

        if pomodoro_reps % 8 == 0:
            timer_label.config(text="Break", fg=RED)
            countdown(long_break_secs)
        elif pomodoro_reps % 2 == 0:
            timer_label.config(text="Break", fg=PINK)
            countdown(short_break_secs)
        else:
            timer_label.config(text="Work", fg=GREEN)
            countdown(work_secs)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    def countdown(count):
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            global pomodoro_timer
            pomodoro_timer = window.after(1000, countdown, count - 1)
        else:
            start_timer()
            mark = ""
            work_sessions = math.floor(pomodoro_reps / 2)
            for _ in range(work_sessions):
                mark += "✓"
                completed_label.config(text=f"{mark}")

    # ---------------------------- UI SETUP ------------------------------- #

    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = PhotoImage(file="./tools/days/day_028/files/tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(
        100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
    )
    canvas.grid(column=2, row=2)

    timer_label = Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 35, "bold"))
    timer_label.grid(column=2, row=1)
    completed_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    completed_label.grid(column=2, row=4)

    button1 = Button(text="Start", command=start_timer)
    button2 = Button(text="Reset", command=reset_timer)
    button1.grid(column=1, row=3)
    button2.grid(column=3, row=3)
    window.mainloop()
