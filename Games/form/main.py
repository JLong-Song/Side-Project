import tkinter as tk


def open_setting():
    pass


window = tk.Tk()
window.title("Form")
window.geometry("480x320")

setting = tk.Button(window, text="Setting", fg="red",
                    font=("Times New Roman", 12), command=open_setting)
setting.pack()


window.mainloop()
