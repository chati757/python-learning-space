import tkinter as tk

# Create the main window
root = tk.Tk()
#win.withdraw()

# Create the dialog window
dialog = tk.Toplevel(root)
dialog.title("test title")
dialog.focus_set()
# Add a label and a button to the dialog window
label = tk.Label(dialog, text="This is a focused dialog window1")
button = tk.Button(dialog, text="Close", command=root.quit)

label.pack()
button.pack()

dialog2 = tk.Toplevel(root)
# Add a label and a button to the dialog window
label2 = tk.Label(dialog2, text="This is a focused dialog window2")
button2 = tk.Button(dialog2, text="Close", command=root.quit)

label2.pack()
button2.pack()

root.mainloop()

print('do another')