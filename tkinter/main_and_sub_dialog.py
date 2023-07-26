import tkinter as tk

'''
ตัวอย่างชุด code นี้ใช้สำหรับการประยุกต์กับ subprocess โดยเราให้ root = tk.Tk() 
อยู่ที่ main process ส่วน sub_dialog เป็นส่วนการทำงานที่ถูกเรียกใช้จาก subprocess
การสร้างและใช้งาน subdialog จะถูกใช้โดย subprocess เราจะสังเกตุเห็นว่าแม้ทำการใช้และทำการปิด sub_dialog ลง
ในส่วนของ root ก็จะยังคงอยู่และรอรับคำสั่งจาก subdialog สั่งใช้ใหม่จาก subprocess ในครั้งถัดๆไป

โดยตัวอย่างทำการเรียกใช้ ทั้งหมดสองครั้ง (ส่วนของ if __name__ == '__main__':)
จะเห็นว่าแม้มีการเรียกใช้ครั้งแรกและเราได้ทำการปิดโปรแกรมลง ส่วนของ root ยังถือเป็น buffer
เพื่อรอการเรียกใช้ในครั้งถัดไปได้ โดยไม่ต้องทำการสร้าง root ใหม่ และ root นี้ก็ยังถือว่าเป็นส่วนของ main process และเป็น global variable

เหตุผลที่เราสร้าง root ไว้ใน main process และเป็น global variable เพราะว่า
หากเราทำการสร้าง root โดยใช้ sub-process ตัว tkinter lib จะปัญหาเวลาเราจะ
start subprocess ดังนั้นเราจึงออกแบบให้ root อยู่ที่ main-process และให้ subprocess 
ส่งคำสั่งสร้าง dialog ไปยัง root ที่อยู่ที่ main process ให้ปฏิบัติ(สร้าง)อีกที
'''

# Create the main window
#root.withdraw()

class sub_dialog:
    def __init__(self,title,label,check_integer=False):
        self.check_integer = check_integer
        self.tkroot = tk.Tk()
        self.tkroot.withdraw()
        self.title = title
        self.label = label
        self.value = None
    
    def create_sub_dialog(self):
        self.dialog = tk.Toplevel(self.tkroot)
        screen_width = self.tkroot.winfo_screenwidth()
        screen_height = self.tkroot.winfo_screenheight()
        window_width = 180
        window_height = 100 
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        self.dialog.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        self.dialog.title(self.title)
        #self.dialog.focus_set()

        self.frame = tk.Frame(self.dialog)
        self.label = tk.Label(self.frame,text=self.label)
        self.entry = tk.Entry(self.frame)
        self.button1 = tk.Button(self.frame, text="  Check  ", command=lambda:self.check_input_integer(self.entry) if(self.check_integer==True) else self.check_input_string(self.entry))
        self.button2 = tk.Button(self.frame,text="  Close  ",command=self.close)

        self.label.grid(row=0, column=0 , columnspan=2 , sticky='w')
        self.entry.grid(row=1, column=0 , columnspan=2 , pady=8)
        # Place the buttons in a grid
        self.button1.grid(row=2, column=0 , pady=10)
        self.button2.grid(row=2, column=1 , pady=10)
        self.button1.focus_force()

        # Pack the frame
        self.frame.pack(pady=2)
        self.dialog.protocol("WM_DELETE_WINDOW", self.close)

        self.tkroot.mainloop()
        return self.value

    def close(self):
        self.dialog.destroy()
        self.tkroot.quit()
        self.tkroot.destroy()

    def check_input_string(self,entry):
        self.value = self.entry.get()
        self.close()

    def check_input_integer(self,entry):
        try:
            self.value = int(self.entry.get())
            self.close()
        except ValueError:
            #ask again
            pass

if __name__ == '__main__':
    sd = sub_dialog("some title","some label",check_integer=True)
    data = sd.create_sub_dialog()
    print(data)

    sd = sub_dialog("some title","some label")
    data = sd.create_sub_dialog()
    '''
    print('do another')
    import time
    time.sleep(5)
    sub_dialog()
    '''