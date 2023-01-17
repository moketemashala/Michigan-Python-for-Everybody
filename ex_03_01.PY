hrs = input("Enter Hours:")
rate = input("Enter Rate:")
if float(hrs) < 40:
    pay = float(hrs)* float(rate)
elif float(hrs) > 40:
    pay = float(rate) * 40 + (float(rate) *(float(hrs) - 40.0)* 1.5)
print(pay)
