hours = input("Enter hours: ")
rate = input("Enter rate: ")

try:
    hrs = float(hours)
    rt = float(rate)
except:
    print("Error: Not a number")
    quit()

print("Hours:", hrs,"/ Rate:", rt)

def computepay(hours, rate):
    if hours > 40:
        calc = hours * rate
        bonus = (hours - 40) * (rate * 0.5)
        pay = calc + bonus

        return pay
    
    else:
        pay = hours * rate
    
        return pay
    
print("Pay", computepay(hrs, rt))