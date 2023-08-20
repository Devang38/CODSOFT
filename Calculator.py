from tkinter import*
root=Tk()
root.title('CALCULATOR')
root.config(bg='purple')
root.geometry('411x653')

def btn_click(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)

def clear():
    global expression
    expression=''
    input_text.set('')

def equal():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=''

expression=""
input_text=StringVar()
entry =Entry(root,width=100,font=('Times New Roman',50,'bold'),bd=10,textvariable=input_text)
entry.pack()

b1=Button(root,width=5,text='1',font=('Times New Roman',30,'bold'),command=lambda:btn_click("1"))
b1.place(x=5,y=120)

b2=Button(root,width=5,text='2',font=('Times New Roman',30,'bold'),command=lambda:btn_click("2"))
b2.place(x=140,y=120)

b3=Button(root,width=5,text='3',font=('Times New Roman',30,'bold'),command=lambda:btn_click("3"))
b3.place(x=275,y=120)

b4=Button(root,width=5,text='4',font=('Times New Roman',30,'bold'),command=lambda:btn_click("4"))
b4.place(x=5,y=210)

b5=Button(root,width=5,text='5',font=('Times New Roman',30,'bold'),command=lambda:btn_click("5"))
b5.place(x=140,y=210)

b6=Button(root,width=5,text='6',font=('Times New Roman',30,'bold'),command=lambda:btn_click("6"))
b6.place(x=275,y=210)

b7=Button(root,width=5,text='7',font=('Times New Roman',30,'bold'),command=lambda:btn_click("7"))
b7.place(x=5,y=300)

b8=Button(root,width=5,text='8',font=('Times New Roman',30,'bold'),command=lambda:btn_click("8"))
b8.place(x=140,y=300)

b9=Button(root,width=5,text='9',font=('Times New Roman',30,'bold'),command=lambda:btn_click("9"))
b9.place(x=275,y=300)

b10=Button(root,width=5,text='+',font=('Times New Roman',30,'bold'),command=lambda:btn_click("+"))
b10.place(x=5,y=390)

b11=Button(root,width=5,text='-',font=('Times New Roman',30,'bold'),command=lambda:btn_click("-"))
b11.place(x=140,y=390)

b0=Button(root,width=5,text='0',font=('Times New Roman',30,'bold'),command=lambda:btn_click("0"))
b0.place(x=275,y=390)

b12=Button(root,width=5,text='*',font=('Times New Roman',30,'bold'),command=lambda:btn_click("*"))
b12.place(x=5,y=480)

b13=Button(root,width=5,text='/',font=('Times New Roman',30,'bold'),command=lambda:btn_click("/"))
b13.place(x=140,y=480)

b14=Button(root,width=8,text='clear',font=('Times New Roman',30,'bold'),command=lambda:clear())
b14.place(x=215,y=570)

b15=Button(root,width=8,text='=',font=('Times New Roman',30,'bold'),command=lambda:equal())
b15.place(x=6,y=570)

b16=Button(root,width=5,text='.',font=('Times New Roman',30,'bold'),command=lambda:btn_click("."))
b16.place(x=275,y=480)

root.mainloop()