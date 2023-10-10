#importing library
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time
import math
import winsound


w=Tk()
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#272727"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark = "✓"
reps=0
timer = None

#Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
#w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar

#new window to open
def new_win():
    def ring_timer():
        frequency = 2500  # Set the frequency of the sound (2500 Hz)
        duration = 500  # Set the duration of the sound (1 second)
        num_bells = 5 # Set the number of times the bell should ring
    
        for _ in range(num_bells):
            winsound.Beep(frequency, duration)  # Play the sound
            time.sleep(0.2)  # Wait for 1 second before playing the next bell sound


    
    def restCommand ():
        global reps
        reps=0
        window.after_cancel(timer)
        canvas.itemconfig(timer_text , text = "00:00")
        timer_label.config(text="Timer",fg=GREEN)
        check_label.config(text="") 
    # ---------------------------- TIMER MECHANISM ------------------------------- # 

    def startCommand():
        global reps
        reps+=1
        short_break_sec = SHORT_BREAK_MIN*60
        long_break_sec = LONG_BREAK_MIN*60

        #if its 1st/3rd/5th/7th rep
        if (reps%8 == 0):
                count_down(long_break_sec)
                timer_label.config(text="Break",fg=RED)    
                ring_timer()
        elif (reps%2==0):
                count_down(short_break_sec)
                timer_label.config(text="Break",fg=PINK)
                ring_timer()
        else:
                count_down(WORK_MIN*60)
                timer_label.config(text="Work",fg=GREEN)
                


    


    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
    def count_down(count):
        global timer
        count_min = math.floor(count/60)
        count_sec = count%60
        if count_sec==0:
            count_sec="00"

        canvas.itemconfig(timer_text , text = f"{count_min}:{count_sec}")
        if(count>0):
            timer = window.after(1000,count_down,count - 1)
        else:
            startCommand()
            marks=""
            work_session = math.floor(reps/2)
            for _ in range(work_session):
                marks+=check_mark
            check_label.config(text=marks)

    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("FocusFusion")
    window.config(padx=100, pady=50 ,bg=YELLOW)



    canvas = Canvas(width=200, height=224 ,bg=YELLOW , highlightthickness=0)
    tomato_img = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image= tomato_img)
    timer_text =canvas.create_text(100,130, text="00:00",fill='white',font=(FONT_NAME,35,'bold'))
    canvas.grid(column=1, row=1)



    timer_label = Label(text="Timer", font=(FONT_NAME,50,'bold'),fg=GREEN ,bg=YELLOW)
    timer_label.grid(column=1,row=0 )

    check_label = Label(text=" " ,font=(FONT_NAME,20,'bold'),fg=GREEN ,bg=YELLOW )
    check_label.grid(column=1, row=3)

    start_button= Button(text = "Start" , command=startCommand,highlightthickness=0)
    start_button.grid(column=0 ,row=2)

    rest_button = Button(text="Reset" , command=restCommand , highlightthickness=0)
    rest_button.grid(column=3, row=2)




    window.mainloop()


Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(w, text=' Focus Fusion', fg='white', bg='#272727') #decorate it 
label1.configure(font=("Game Of Squids", 24, "bold"))   #You need to install this font in your PC or try another one
label1.place(x=100,y=90)

label2=Label(w, text='Loading...', fg='white', bg='#272727') #decorate it 
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

#making animation

image_a=ImageTk.PhotoImage(Image.open('c2.png'))
image_b=ImageTk.PhotoImage(Image.open('c1.png'))




for i in range(5): #5loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)



w.destroy()
new_win()
w.mainloop()
