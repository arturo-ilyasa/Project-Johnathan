from tkinter import *

root = Tk()
root.title("Johnathan Groundstation")

direction_status = Entry(root, width=27)
direction_status.grid(row=0, column=0, columnspan=3)

def button_click(direction):
    direction_status.delete(0, 'end')
    direction_status.insert(0, direction)


# Use lambda when you want to call a function with arguments
button_1 = Button(root, text="→", padx=20, pady=20, command=lambda: button_click("Right"))
button_2 = Button(root, text="←", padx=20, pady=20, command=lambda: button_click("Left"))
button_3 = Button(root, text="↑", padx=20, pady=20, command=lambda: button_click("Forward"))
button_4 = Button(root, text="↓", padx=20, pady=20, command=lambda: button_click("Backward"))
button_5 = Button(root, text="SELF DESTRUCT")

button_1.grid(row=2, column=2)
button_2.grid(row=2, column=0)
button_3.grid(row=1, column=1)
button_4.grid(row=2, column=1)
button_5.grid(row=3, column=0, columnspan=3)



root.mainloop()