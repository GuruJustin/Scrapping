x1 = int(input("Enter your value: "))
y1 = int(input("Enter your value: ")) 
x2 = int(input("Enter your value: ")) 
y2 = int(input("Enter your value: ")) 


x = (y1-y2) * 86
if ((x1-x2) % 2  != 0) :
    x -= 43

y = (x1-x2) * 74

print (x, y)