#Leap year finder

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        leap = True
        if year % 100 ==0:
            if year % 400 == 0:
                leap = True
            else :
                leap = False
    
    return leap

inp1 = input(" Enter years from 1800 to 10^5. \n Enter the year you want to check for a leap day in numerical form. ")
if len(inp1) >= 4 and len(inp1) <=6:
    check = True
    inp1 =int(inp1)
else:
    print("Please enter year within the given constaraints.")
try:
    if check == True:        
        if is_leap(inp1) == True:
            print(inp1,"is a leap year.")
        else:
            print(inp1,"is not a leap year.")
except:
    print("incorrect input")