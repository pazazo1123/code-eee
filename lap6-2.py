f = open("myfile2.txt","w")
txt1="siam dhurakit\n"
txt1 +="ฟาอิซ มุคุระ \n"
txt1 +="tel 0948927001"

s = f.write(txt1)

f.close()

print("เขียนลงไฟล์แล้ว")