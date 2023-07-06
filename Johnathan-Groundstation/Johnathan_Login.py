from tkinter import *       # The '*' means import everything from tkinter library


# The main window of the app is called the 'root'
root = Tk()     # Creating that main window
root.title("Johnathan Groundstation Login")

e = Entry(root, width=25, fg="black", bg="white", borderwidth=3)
e.grid(row=2, column=0)

e.insert(0, "Enter your password")

password_status_label = Label(root, text="")

def start_click():
    password_status_label.config(text="")
    
    if e.get() == "babi ngepeT":
        password_status_label.config(text="Welcome, Arthur", bd=20)
        # A button that takes user to the actual groundstation window
        initiation_button = Button(root, bg='red', padx=40, pady=40, bd=50).grid(row=5, column=0)

    else :
        password_status_label.config(text="Password incorrect")

    password_status_label.grid(row=4, column=0)
    e.delete(0, 'end')

myLabel1 = Label(root, text="   Project Johnathan   ", font=("Calibri", 50, "bold")).grid(row=0, column=0)     # Label for the root with text

#myLabel2 = Label(root, text="Insert password:").grid(row=1, column=0)      # The grid is object controlling the positioning of the labels

#myLabel1.pack()        # Packing the label, just as big as the widgets inside. In this case, its the 'hello world' text

#myLabel1.grid(row=0, column=0)      # This is if you want specific row and column

#myLabel2.grid(row=1, column=0)      # However the positioning is relative, if row=10, it will be the same

# BUTTON
start_button = Button(root, text="ENTER", command=start_click, bg="red").grid(row=3, column=0)

# Create a main loop to know each time where the cursor is above the window, because 
#   it will interact with the UI
root.mainloop()