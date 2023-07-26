import tkinter as tk
from tkinter import simpledialog

# Create the main window
root = tk.Tk()

# Create the dialog window
class MyDialog(simpledialog.Dialog):
    def __init__(self, parent, title, message):
        self.message = message
        simpledialog.Dialog.__init__(self, parent, title)

    def body(self, master):
        tk.Label(master, text=self.message).pack()

        self.entry = tk.Entry(master)
        self.entry.pack()
        return self.entry # initial focus

    def apply(self):
        self.result = self.entry.get()

# Show the dialog window and get the result
dialog = MyDialog(root, "Input", "Enter an integer:")
result = dialog.result

# Check the result
if result:
    print("You entered:", result)
else:
    print("You canceled the operation")

root.mainloop()