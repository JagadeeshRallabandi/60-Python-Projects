from tkinter import *
import calendar

# Function to show calendar of the given year
def showCalender():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendar for the Year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
    calYear.grid(row=5, column=1, padx=20)
    gui.mainloop()

# Driver code
if __name__ == '__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calendar")
    new.geometry("250x140")
    
    cal = Label(new, text="Calendar", bg='grey', font=("times", 28, "bold"))
    year = Label(new, text="Enter Year", bg='dark grey')
    year_field = Entry(new)
    button = Button(new, text='Show Calendar', fg='Black', bg='Blue', command=showCalender)
    exit_button = Button(new, text='Exit', fg='Black', bg='Red', command=new.quit)

    # Putting widgets in position
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    exit_button.grid(row=5, column=1)

    new.mainloop()
