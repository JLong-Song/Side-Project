import tkinter as tk


def open_setting():
    Setting_window = tk.Toplevel(Window)
    Setting_window.geometry("240x160+0+0")
    Setting_window.mainloop()


Window = tk.Tk()
Window.title("Form")
Window.geometry("480x320+0+0")

Canvas = tk.Canvas(Window, width=640, height=480)

Setting = tk.Button(Window, text="Setting", fg="red",
                    font=("Times New Roman", 12), command=open_setting)
Setting.pack()


Window.mainloop()
