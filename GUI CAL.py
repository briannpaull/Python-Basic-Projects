#importing tkinter
from tkinter import *
cal=Tk()

#defining shape
cal.geometry("600x600")
cal.title("CALCULATOR")

#defining heading
cal_head=Label(cal,text="CALCULATOR",bg="gray",font=("lucida",45,'italic'))
cal_head.pack(side=TOP)

#defining screen for input

screen_value=StringVar()
screen_value.set("")
screen=Entry(cal,textvar=screen_value,font="lucida 30 bold")
screen.pack(fill=X)

#creating events
def click(event):
    global screen_value
    
    text=event.widget.cget("text")
    if text=="=":
        if screen_value.get().isdigit():
            value=int(screen_value.get())
        else:
            value=eval(screen.get())
        screen_value.set(value)
    elif text=="C":
        screen_value.set("")
        screen.update()
        
    else:
        screen_value.set(screen_value.get() + text)
        screen.update()
    
  
#creating buttons
 
f= Frame(cal,bg="grey")
b= Button(f,text="1",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)

b= Button(f,text="2",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)


b= Button(f,text="3",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)


b= Button(f,text="4",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)


b= Button(f,text="5",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)

f.pack()
f= Frame(cal,bg="grey")
b= Button(f,text="6",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)

b= Button(f,text="7",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)


b= Button(f,text="8",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)


b= Button(f,text="9",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)


b= Button(f,text="0",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)

f.pack()
f= Frame(cal,bg="grey")
b= Button(f,text="+",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)

b= Button(f,text="-",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)


b= Button(f,text="*",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)


b= Button(f,text="/",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)

b= Button(f,text="%",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)


f.pack()

f= Frame(cal,bg="grey")

b= Button(f,text="=",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)

b= Button(f,text="C",padx=24,pady=24,font="lucida 30 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind('<Button>',click)

f.pack()

cal.mainloop()






