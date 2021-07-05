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

label_welcome = tkinter.Label(mainapp, text="Hello World")
message_welcome = tkinter.Message(mainapp, text="Message in A bottle")
input_message = tkinter.Entry(mainapp)
button_exit = tkinter.Button(mainapp, text="EXIT", command=exit)
check_box = tkinter.Checkbutton(mainapp, text='Agree')
radio_button = tkinter.Radiobutton(mainapp, text='Done', value=1)
radio_button2 = tkinter.Radiobutton(mainapp, text='Start', value=2)

label_welcome.pack()
message_welcome.pack()
input_message.pack()
button_exit.pack()
check_box.pack()
radio_button.pack()
radio_button2.pack()


##Program stay in while loop til client choose to exit
mainapp.mainloop()