try:
    w = int(input("น้ำหนัก "))
    h = int(input("ส่วนสูง "))
    bmi = w/(h/100)**2
    
except:
    print("error ครับผม")
    
else:
    print("คำตอบ ",bmi)