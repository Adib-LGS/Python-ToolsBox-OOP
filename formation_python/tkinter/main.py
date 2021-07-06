######Intro to tkinter#####
import tkinter

mainapp = tkinter.Tk()
mainapp.title("First test")
mainapp.geometry("700x700+350+175") #Window size
mainapp.minsize(400, 400)
mainapp.maxsize(1280, 720)
mainapp.positionfrom("user")
#stop resizing window:
#mainapp.resizable(width=False, height=True)
"""
Caluculation psotion
position_X : (screen_width // 2) - (window_width // 2)
position_Y : (screen_height // 2) - (window_height // 2)
"""

def exit():
    print('exit')
####----------------------------------------

#Observer (like event-listener)
def update_label_observer(*args):
    var_label.set(var_entry.get())

def radio_change_observer():
    if var_agreement.get():
        print("Agree")
    else:
        print("Disagree")


#widget
var_entry = tkinter.StringVar()
var_entry.trace_variable("w",update_label_observer)
#Link entry to variable
entry = tkinter.Entry(mainapp, textvariable=var_entry)

var_agreement = tkinter.IntVar()
var_agreement.trace("w", update_label_observer)
#Link radio tu variable
radio1 = tkinter.Radiobutton(mainapp, text="Agree ?", value=1, variable=var_agreement)
radio2 = tkinter.Radiobutton(mainapp, text="Disagree", value=0, variable=var_agreement)

var_label = tkinter.StringVar()
label_w = tkinter.Label(mainapp, textvariable=var_label)


var_label.set("This will change")


entry.pack()
label_w.pack()
radio1.pack()
radio2.pack()




##Program stay in while loop til client choose to exit
mainapp.mainloop()