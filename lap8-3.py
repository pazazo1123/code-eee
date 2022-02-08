def triangle():
    b = int(base.get())
    h = int(high.get())
    a = 1/2*b*h
    messagebox.showinfo("พื้นที่สามเหลี่ยม","คำตอบ %.2f" % a)
    area.set(a)

from tkinter import *
main = Tk()
main.geometry("800x500")
main.title("โปรแกรมหาพื้นที่สามเหลี่ยม โดย ฟาอิซ มุคุระ")
base = StringVar()
high = StringVar()
area = StringVar()

lb1 = Label(main, text="รับค่าฐาน: ", font=("FreesiaUPC",20))
lb1.place(x=50, y=10)
tb1 = Entry(main, textvariable= base)
tb1.place(x=180, y=20, width=200, height=20)
lb2 = Label(main, text="รับค่าสูง: ", font=("FreesiaUPC",20))
lb2.place(x=50, y=55)
tb2 = Entry(main, textvariable= high)
tb2.place(x=180, y=65, width=200, height=20)

btn = Button(main, text="คำนวณ", font=("FreesiaUPC",20), command= triangle)
btn.place(x=180,y=110)

lb3 = Label(main, text="คำตอบ: ", font=("FreesiaUPC",20))
lb3.place(x=50, y=185)
lb4 = Label(main,  font=("FreesiaUPC",20), textvariable= area)
lb4.place(x=180, y=185)

main.mainloop()