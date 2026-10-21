def computepay(h,r):
    if h <= 40:
        grosspay = h*r
    elif h>40:
        grosspay = ((h-40)*1.5*r) +(40*r)
    return grosspay
hrs = input("Enter number of hours:")
rate=input("Enter rate per hour:")
h=float(hrs)
r=float(rate)
p=computepay(h,r)
print("Pay" ,p)
