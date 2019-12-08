minimum = 245318 #my minimum password
maximum = 765747 #my maximum password
passwords1 = 0 
passwords2 = 0
for x in range(minimum, maximum+1): #loop through every possible password
    number = list(str(x)) #make a list containing all of the digits
    double = False
    counter = 1 #count of consecutive digit appeareance
    temp = [] 
    for y in range(5): # loop through digits
        if number[y] > number[y+1]: #if next digit is lower than current, end loop immediately
            break
        if number[y] == number[y+1]: #if next digit is equal to current, indicate double
            double = True
            counter += 1 # if next digit is equal to current, consecutive digit counter is raised by 1...
        else:
            temp.append(counter) #...if not, we add it to the list and reset the counter to 1
            counter = 1
        
    else: #if the loop didn't break we can check if there was any double
        temp.append(counter)
        if double == True: #part 1: passwords containing minimum 2 equal digits next to each other
            passwords1+=1
        if double == True and 2 in temp: #part2: passwords containing at least one set of exactly 2 equal digits next to each other
            passwords2+=1
print(passwords1)
print(passwords2)
