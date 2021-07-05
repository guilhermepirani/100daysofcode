import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60

# ---------------------------- GLOBALS ------------------------------- #
reps = 0
work_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global work_timer, reps
    window.after_cancel(work_timer)
    top_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer, text='00:00')
    bottom_label.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def play_notification():
    playsound('C:/100daysofcode/day028/pomodoro/notification.wav')

def raise_window():
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        top_label.config(text="Break", fg=RED)
        raise_window()
        play_notification()
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        top_label.config(text="Break", fg=PINK)
        raise_window()
        play_notification()
    else:
        count_down(WORK_MIN)
        top_label.config(text="Work", fg=GREEN)
        raise_window()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps

    minutes = int(count / 60)
    if minutes < 10:
        minutes = f'0{minutes}'
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(timer, text=f'{minutes}:{seconds}')
    if count > 0:
        global work_timer
        work_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = int(reps / 2)
        bottom_label.config(text='✔'*marks)
        if reps == 9:
            reset()

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(False, False)

# Window icon
ico = Image.open('C:/100daysofcode/day028/pomodoro/tomato.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)

# Tomato image with text
tomato_img = tk.PhotoImage(file='C:/100daysofcode/day028/pomodoro/tomato.png')
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

# Other widgets
top_label = tk.Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
top_label.grid(row=0, column=1)

bottom_label = tk.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, 'bold'))
bottom_label.config(pady=25)
bottom_label.grid(row=2, column=1)

start_button = tk.Button(text='Start', bg='white', borderwidth=1, command=start_timer)
start_button.config(width=8)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text='Reset', bg='white', borderwidth=1, command=reset)
reset_button.config(width=8)
reset_button.grid(row=2, column=2)

window.mainloop()
