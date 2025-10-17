h = input("Enter hours: ")
r = input("Enter rate: ")

try:
    hrs = float(h)
    rate = float(r)
except:
    print("Error: Not a Number.")
    quit()

print("Hours:", hrs, "/ Rate:", rate)

if hrs > 40:
    calc = hrs * rate
    bonus = (hrs - 40) * (rate * 0.5)
    pay = calc + bonus
else:
    pay = hrs * rate

print ("Pay:", pay)