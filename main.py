from tkinter import *
from tkinter import messagebox
from datetime import date

base = Tk()


# function to calculate the week
def btn_click():
    # The date should have correct format
    try:
        a, b, c = loginInput.get().split(' ')
        date2 = date(int(a), int(b), int(c))
    except:
        messagebox.showerror(title='Error', message='Wrong date format')
    # the last day of preceding week minus a week 'cause the first week is not 0
    date1 = date(2018, 12, 23)
    # The date should be corrent format
    if type(date2) not in [date]:
        messagebox.showerror(title='Error', message='Wrong date format')
    if (date2 - date1).days < 0:
        messagebox.showerror(title='Error', message='The date is earlier than given date')
    # days=weeks output
    result = (date2 - date1).days // 7

    info['text'] = f'Week number: {str(result)}'


# the main window
base['bg'] = 'white'
base.title('Week counter')

base.geometry('320x250')

base.resizable(width=False, height=False)

canvas = Canvas(base, height=300, width=250)
canvas.pack()
# The frame of the main window
frame = Frame(base, bg='#FEFFF1')
frame.place(rely=0.15, relwidth=1, relheight=1)
# the I/O block
title = Label(frame, text='Enter your date', bg='gray', font=10)
title.pack(pady=3)

title = Label(frame, text='e.g. 2020 5 12', bg='#E9E9E9', font=("Courier", 9))
title.pack(pady=3)

loginInput = Entry(frame, bg='white')
loginInput.pack()

btn = Button(frame, text='Submit', bg='#D1A095', command=btn_click)
btn.pack(pady=5)

info = Label(frame, text='Result', bg='#ffb700', font=40)
info.pack(pady=5)

base.mainloop()
