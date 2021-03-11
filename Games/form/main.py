import tkinter as tk


def open_setting():
    setting_window = tk.Toplevel(window)
    setting_window.geometry("240x160+0+0")
    setting_window.mainloop()


window = tk.Tk()
window.title("Form")
window.geometry("480x320+0+0")

setting = tk.Button(window, text="Setting", fg="red",
                    font=("Times New Roman", 12), command=open_setting)
setting.pack()


window.mainloop()
