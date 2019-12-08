minimum = 245318 #my minimum password
maximum = 765747 #my maximum password
passwords1 = 0 
passwords2 = 0
for x in range(minimum, maximum+1): #loop through every possible password
    number = list(str(x)) #make a list containing all of the digits
    double = False
    for y in range(5): # loop through digits
        if number[y] > number[y+1]: #if next digit is lower than current, end loop immediately
            break
        if number[y] == number[y+1] and double == True: #if next digit is equal to current, indicate double
            double = True
        if number[y] == number[y+1]: #if next digit is equal to current, indicate double
            double = True
    else: #if the loop didn't break we can check if there was any double, if true add 1 to password count
        if double == True:
            passwords1+=1
print(passwords1)
