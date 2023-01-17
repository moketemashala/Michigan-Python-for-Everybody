hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    fh = float(hrs)
    fr = float(rate)
except:
    print('Error, please enter numeric input')
    quit()

print(fh, fr)

if fh < 40:
    pay = fh * fr
elif fh > 40:
    pay = fr * 40 + (fr *(fh - 40.0)* 1.5)
print(pay)
