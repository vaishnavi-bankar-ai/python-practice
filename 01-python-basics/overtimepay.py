hrs= input("Enter Hours:")
h=float(hrs)
rate=input("Enter the rate per hour:")
r=float(rate)
if h<=40:
    grosspay=h*r
    print(grosspay)
elif h>40:
    newr=1.5*r
    grosspay=((h-40)*newr)+ (40*r)
    print(grosspay)


  
    
