import tkinter as tk

class Lotfi(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit(): 
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this 
            self.set(self.old_value)

#demo:
window = tk.Tk()
window.wm_geometry("800x600")
window.resizable(False, False)
window.title('Login')
frame_NUMBER_OF_POINTS = tk.Frame(window)
From_entry=Lotfi(window)
From_entry.grid(column=0,row=0)
From_entry.pack()
MyLabel = tk.Label(window,text="test",font=('font name',25))
MyLabel.pack()
From_entry.place(relx=0.45, rely= 0.45, width=200, height=50)
window.mainloop()