import tkinter as t
from fileinput import close
from tkinter import messagebox
class SetGUI:
    def __init__(self):
        self.main=t.Tk()
        self.menubar=t.Menu(self.main)
        self.fmenu=t.Menu(self.menubar,tearoff=0)
        self.fmenu.add_command(label="Close",command=self.close)
        self.fmenu.add_separator()
        self.fmenu.add_command(label="Exit",command=exit)

        self.actionmenu=t.Menu(self.menubar,tearoff=0)
        self.actionmenu.add_command(label="Show Message",command=self.display_msg)



        self.menubar.add_cascade(menu=self.fmenu,label="File")
        self.menubar.add_cascade(menu=self.actionmenu,label="Open")
        self.main.config(menu=self.menubar)

        self.main.geometry("400x400")
        self.lbl=t.Label(self.main,text="Message",font=("Times New Roman",16))
        self.lbl.pack(padx=10,pady=10)
        self.txt=t.Text(self.main,height=5,font=("Times New Roman",14))
        self.txt.bind("<KeyPress>",self.shortcut)
        self.txt.pack(padx=10,pady=10)
        self.chk_value=t.IntVar()
        self.chk=t.Checkbutton(self.main,text="Display Message",font=("Times New Roman",14),variable=self.chk_value)
        self.chk.pack(padx=10,pady=10)
        self.btn=t.Button(self.main,width="10",text="Click",font=("Times New Roman",14),command=self.display_msg)
        self.btn.pack(padx=5,pady=5)
        self.clrbtn=t.Button(self.main,width="10",text="Clear",font=("Times New Roman",14),command=self.clear)
        self.clrbtn.pack(padx=5,pady=5)

        self.main.protocol("WM_DELETE_WINDOW",self.close)
        self.main.mainloop()

    def display_msg(self):
        if self.chk_value.get()==0:
            print(self.txt.get('1.0',t.END))
        else:
            messagebox.showinfo(title="Message",message=self.txt.get('1.0',t.END))

    def shortcut(self,event):
       if event.state==12 and event.keysym=="Return":
           self.display_msg()

    def close(self):
        if messagebox.askyesno(title="Exit",message="Do you want to exit?"):
         self.main.destroy()

    def clear(self):
        self.txt.delete("1.0",t.END)


SetGUI()


