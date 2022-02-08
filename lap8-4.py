def Checkgrade():
    score = int(tb1.get())
    midterm = int(tb2.get())
    final = int(tb3.get())
    love = int(tb4.get())
    total = score+midterm+final+love
    answer.set(total)
    
from tkinter import *
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมเช็คเกรด โดย ฟาอิซ มุคุระ")
answer=StringVar()

lb1 = Label(main, text="คะแนนเก็บ", font=("FreesiaUPC",20))
lb1.place(x=70, y=40)
lb2 = Label(main, text="กลางภาค", font=("FreesiaUPC",20))
lb2.place(x=70, y=100)
lb3 = Label(main, text="ปลายภาค", font=("FreesiaUPC",20))
lb3.place(x=70, y=160)
lb4 = Label(main, text="จิตพิสัย", font=("FreesiaUPC",20))
lb4.place(x=70, y=220)
lb5 = Label(main, text="คำตอบ", font=("FreesiaUPC",20))
lb5.place(x=70, y=320)
lb6 = Label(main, font=("FreesiaUPC",20), textvariable=answer)
lb6.place(x=300, y=320)

tb1=Entry(main)
tb1.place(x=200, y=45, width=200, height=25)
tb2=Entry(main)
tb2.place(x=200, y=105, width=200, height=25)
tb3=Entry(main)
tb3.place(x=200, y=165, width=200, height=25)
tb4=Entry(main)
tb4.place(x=200, y=225, width=200, height=25)

btn=Button(main, text="คำนวณ", font=("FreesiaUPC",20), command=Checkgrade)
btn.place(x=450, y=40)

main.mainloop()