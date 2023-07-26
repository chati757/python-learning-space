import tkinter as tk

# Create the main window
root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 200
window_height = 150
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Add a label, an entry field, and a button to the main window
label = tk.Label(root, text="Enter an integer:")
entry = tk.Entry(root)
button = tk.Button(root, text="Check", command=lambda: check_integer(entry))

label.pack(padx=5, pady=5)
entry.pack(padx=2, pady=2)
button.pack(padx=2 ,pady=5)

def check_integer(entry):
    try:
        value = int(entry.get())
        print("You entered a valid integer:", value)
    except ValueError:
        print("You did not enter a valid integer")

root.mainloop()