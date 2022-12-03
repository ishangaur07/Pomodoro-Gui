from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    Title_label.config(text="Start")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        Title_label.config(text="Long Break", fg=RED)

    elif reps % 2 == 0:
        countdown(short_break_sec)
        Title_label.config(text="Short Break", fg=PINK)

    else:
        countdown(work_sec)
        Title_label.config(text="Working", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Using dynamic typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✔"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro technique")
window.config(padx=200, pady=150, bg=YELLOW)

# Labels
Title_label = Label(text="Start", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
Title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Check mark
text = "✔"
check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "normal"))
check_label.grid(row=3, column=1)

# Button
start_button = Button(text="Start", command=start_timer, highlightthickness=0, width=10, height=1)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_time,  width=10, height=1)
reset_button.grid(row=2, column=2)

window.mainloop()
