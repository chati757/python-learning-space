import win32gui
import win32con

def focus_window(title):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
    else:
        print("Window with title '{}' not found!".format(title))

# Example usage:
focus_window("book_val_graph : test")




