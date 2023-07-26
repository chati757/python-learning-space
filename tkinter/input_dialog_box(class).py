import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 200
        window_height = 100
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        # Add a label, an entry field, and a button to the main window
        self.label = tk.Label(self, text="Enter an integer:")
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Check", command=lambda: self.check_integer(self.entry))

        self.label.pack(padx=5, pady=5)
        self.entry.pack(padx=2, pady=2)
        self.button.pack(padx=2 ,pady=5)

    def check_integer(self,entry):
        try:
            value = int(self.entry.get())
            print("You entered a valid integer:", value)
        except ValueError:
            print("You did not enter a valid integer")

m = MainWindow()
m.mainloop()