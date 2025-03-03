import tkinter as t

calculte=""

def addCalculation(sym):
    global calculte
    calculte+=str(sym)
    txt1.delete(1.0,"end")
    txt1.insert(1.0,calculte)

def evaluteCalculation():
    global calculte
    try:
        output=str(eval(calculte))
        calculte=""
        txt1.delete(1.0, "end")
        txt1.insert(1.0, output)
    except:
        clearField()
        txt1.insert(1.0,"Error")

def clearField():
    global calculte
    calculte=""
    txt1.delete(1.0,"end")

main= t.Tk()
main.geometry("300x300")
txt1=t.Text(main,height=2,width=18,font=("Times New Roman",20))
txt1.grid(columnspan=7)
btn1=t.Button(main,text="7",command=lambda: addCalculation(7),width=5,font=("Times New Roman",12))
btn1.grid(row=2,column=1)
btn2=t.Button(main,text="8",command=lambda : addCalculation(8),width=5,font=("Times New Roman",12))
btn2.grid(row=2,column=2)
btn3=t.Button(main,text="9",command=lambda :addCalculation(9),width=5,font=("Times New Roman",12))
btn3.grid(row=2,column=3)
btn4=t.Button(main,text="/",command=lambda : addCalculation("/"),width=5,font=("Times New Roman",12))
btn4.grid(row=2,column=4)
btn5=t.Button(main,text="4",command=lambda : addCalculation(4),width=5,font=("Times New Roman",12))
btn5.grid(row=3,column=1)
btn6=t.Button(main,text="5",command=lambda : addCalculation(5),width=5,font=("Times New Roman",12))
btn6.grid(row=3,column=2)
btn7=t.Button(main,text="6",command=lambda : addCalculation(6),width=5,font=("Times New Roman",12))
btn7.grid(row=3,column=3)
btn8=t.Button(main,text="*",command=lambda : addCalculation("*"),width=5,font=("Times New Roman",12))
btn8.grid(row=3,column=4)
btn9=t.Button(main,text="1",command=lambda : addCalculation(1),width=5,font=("Times New Roman",12))
btn9.grid(row=4,column=1)
btn10=t.Button(main,text="2",command=lambda : addCalculation(2),width=5,font=("Times New Roman",12))
btn10.grid(row=4,column=2)
btn11=t.Button(main,text="3",command=lambda : addCalculation(3),width=5,font=("Times New Roman",12))
btn11.grid(row=4,column=3)
btn12=t.Button(main,text="-",command=lambda : addCalculation("-"),width=5,font=("Times New Roman",12))
btn12.grid(row=4,column=4)
btn13=t.Button(main,text=".",command=lambda : addCalculation("."),width=5,font=("Times New Roman",12))
btn13.grid(row=5,column=1)
btn14=t.Button(main,text="0",command=lambda : addCalculation(0),width=5,font=("Times New Roman",12))
btn14.grid(row=5,column=2)
btn15=t.Button(main,text="=",command=evaluteCalculation,width=5,font=("Times New Roman",12))
btn15.grid(row=5,column=3)
btn16=t.Button(main,text="+",command=lambda : addCalculation("+"),width=5,font=("Times New Roman",12))
btn16.grid(row=5,column=4)
btn17=t.Button(main,text="C",command=lambda : clearField,width=5,font=("Times New Roman",12))
btn17.grid(row=6,column=1)
btn18=t.Button(main,text="%",command=lambda : addCalculation('%'),width=5,font=("Times New Roman",12))
btn18.grid(row=6,column=2)
btn19=t.Button(main,text="(",command=lambda : addCalculation("("),width=5,font=("Times New Roman",12))
btn19.grid(row=6,column=3)
btn20=t.Button(main,text=")",command=lambda : addCalculation(")"),width=5,font=("Times New Roman",12))
btn20.grid(row=6,column=4)
main.mainloop()