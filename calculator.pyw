from tkinter import *

def click(event):
    global tyval
    text = event.widget.cget("text")
    if text =='=':
        if tyval.get().isdigit():
            value = int(tyval.get())
        else:
            value = eval(screen.get())
        
        tyval.set(value)
        screen.update()

    elif text =='C':
        tyval.set("")
        screen.update()
    else:
        tyval.set(tyval.get() + text)
        screen.update()

cal = Tk()
cal.geometry("315x500")
cal.title("Calculator")
cal.configure(bg='#282C35')
tyval = StringVar()
# Type  
  
tyval.set("")


h=Scrollbar(cal, orient='horizontal')
h.pack(side=BOTTOM, fill='x')
screen = Entry(cal, textvar=tyval, font="ariel 25 bold",bg='#282C35',fg='white',xscrollcommand=h.set,highlightthickness=0,borderwidth=0)
screen.pack(fill=X,ipady="20",pady='20')
h.config(command=screen.xview)

# new frame

fr = Frame(cal, bg='#282C35')

b = Button(fr,text='C',font="lucida 18 bold",fg='white',bg='#16161d')
b.pack(side=LEFT,ipadx=60,ipady=2.5,padx=1,pady=3)
b.bind('<Button-1>',click)

b = Button(fr,text='00',font="lucida 20 bold",bg='black',fg='white')
b.pack(side=LEFT,ipadx=10,ipady=0.4,padx=1,pady=3)
b.bind('<Button-1>',click)


b = Button(fr,text='/',font="lucida 20 bold",fg='white',bg='#16161d')
b.pack(side=LEFT,ipadx=20,ipady=0.4,padx=1,anchor=W,pady=3)
b.bind('<Button-1>',click)
fr.pack()

# new frame

fr = Frame(cal, bg='#282C35')
b = Button(fr,text='9',font="lucida 20 bold",bg='black',fg='white')
b.pack(side=LEFT,ipadx=18,ipady=0,padx=1)
b.bind('<Button-1>',click)

b = Button(fr,text='8',font="lucida 20 bold",bg='black',fg='white')
b.pack(side=LEFT,ipadx=18,ipady=0,padx=1)
b.bind('<Button-1>',click)

b = Button(fr,text='7',font="lucida 20 bold",fg='white',bg='black')
b.pack(side=LEFT,ipadx=18,ipady=0,padx=1)
b.bind('<Button-1>',click)

b = Button(fr,text='*',font="lucida 20 bold",fg='white',bg='#16161d')
b.pack(side=LEFT,ipadx=18,ipady=0,padx=1,anchor=W)
b.bind('<Button-1>',click)
fr.pack()

# new frame

fr = Frame(cal, bg='#282C35')
b = Button(fr,text='6',font="lucida 18 bold",bg='black',fg='white')
b.pack(side=LEFT,ipadx=20,ipady=3,padx=1,pady=3)
b.bind('<Button-1>',click)

b = Button(fr,text='5',font="lucida 18 bold",bg='black',fg='white')
b.pack(side=LEFT,ipadx=22,ipady=3,padx=1,pady=3)
b.bind('<Button-1>',click)

b = Button(fr,text='4',font="lucida 20 bold",fg='white',bg='black')
b.pack(side=LEFT,ipadx=18,ipady=0,padx=1,pady=3)
b.bind('<Button-1>',click)

b = Button(fr,text='-',font="lucida 20 bold",fg='white',bg='#16161d')
b.pack(side=LEFT,ipadx=18,ipady=0,padx=1,anchor=W,pady=3)
b.bind('<Button-1>',click)
fr.pack()

# new frame

fr = Frame(cal, bg='#282C35')
b = Button(fr,text='3',font="lucida 20 bold",bg='black',fg='white')
b.pack(side=LEFT,ipadx=18,ipady=0,padx=1)
b.bind('<Button-1>',click)

b = Button(fr,text='2',font="lucida 20 bold",bg='black',fg='white')
b.pack(side=LEFT,ipadx=18,ipady=0,padx=1)
b.bind('<Button-1>',click)

b = Button(fr,text='1',font="lucida 20 bold",fg='white',bg='black')
b.pack(side=LEFT,ipadx=18,ipady=0,padx=1)
b.bind('<Button-1>',click)

b = Button(fr,text='+',font="lucida 20 bold",fg='white',bg='#16161d')
b.pack(side=LEFT,ipadx=18,ipady=0,padx=1,anchor=W)
b.bind('<Button-1>',click)
fr.pack()

# new frame

fr = Frame(cal, bg='#282C35')
b = Button(fr,text='%',font="lucida 18 bold",bg='#16161d',fg='white')
b.pack(side=LEFT,ipadx=18,ipady=3,padx=1,anchor=W,pady=3)
b.bind('<Button-1>',click)

b = Button(fr,text='0',font="lucida 20 bold",bg='black',fg='white')
b.pack(side=LEFT,ipadx=18,ipady=0,padx=1,pady=3)
b.bind('<Button-1>',click)

b = Button(fr,text='.',font="lucida 20 bold",fg='white',bg='#16161d')
b.pack(side=LEFT,ipadx=22,ipady=0,padx=1,pady=3)
b.bind('<Button-1>',click)

b = Button(fr,text='=',font="lucida 20 bold",fg='white',bg='#2a52be')
b.pack(side=LEFT,ipadx=18,ipady=0,padx=1,pady=3)
b.bind('<Button-1>',click)
fr.pack()

ft = Frame(cal, bg='#282C35')
Label(ft,text="Made by Atharva",font='lucida 10 bold').pack(pady=15)
ft.pack()

cal.mainloop()