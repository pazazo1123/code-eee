def AbyB(a , b):
    try:
        c = ((a+b) // (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)      
AbyB(5.0, 6.0)
AbyB(7.0, 5.0)
print("ฟาอิซ มุคุระ")