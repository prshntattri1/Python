'''
Created on Apr 22, 2018

@author: Prashant
'''
while True:
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Modulo(Remainder)")
    print("6.Quit")
    ch = int(input("Choice:"))
    if ch == 6:
        break;
    a = float(input("A:"))
    b = float(input("B:"))
    if ch == 1:
        print("A+B="+str(a+b))
    elif ch == 2:
        print("A-B="+str(a-b)+", B-A="+str(b-a))    
    elif ch == 3:
        print("A*B="+str(a*b))
    elif ch == 4:
        print("A/B="+str(a/b)+", B/A"+str(b/a))
    else:
        print("A%B="+str(a%b)+", B%A"+str(b%a))    