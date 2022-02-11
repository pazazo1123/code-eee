try:
    k = 200//10
    print(k)    
except ZeroDivisionError:   
    print("Can't divide by zero")       
finally:
       print('This is always executed')
print("ฟาอิซ มุคุระ")