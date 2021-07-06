import tkinter

#Init base window
app = tkinter.Tk()
app.geometry("700x500")
app.title("Menu List")


#Widget
#-Main Menu
main_menu = tkinter.Menu(app)


#-Observer
def show_about():
    about_window = tkinter,tkinter.Toplevel(app)
    about_window.title("About")
    about_label = tkinter.Label(about_window, text="We're One")
    about_label.pack()


#-Add menu command
first_menu = tkinter.Menu(main_menu, tearoff=0)
first_menu.add_command(label="choice1")
first_menu.add_command(label="choice2")
first_menu.add_command(label="exit", command=app.quit)


second_menu = tkinter.Menu(main_menu, tearoff=0)
second_menu.add_command(label="command1")
second_menu.add_command(label="About US", command=show_about)

#-Rolling menu
main_menu.add_cascade(label="First menu", menu=first_menu)
main_menu.add_cascade(label="Second menu", menu=second_menu)


#Config
app.config(menu=main_menu)


#MainLoop
app.mainloop()