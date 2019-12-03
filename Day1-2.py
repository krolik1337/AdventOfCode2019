import math 

def fuel(mass):
    req_fuel = (math.floor(mass/3)-2) #calculate required fuel
    if req_fuel > 0: 
        return req_fuel + fuel(req_fuel) #if required fuel is >0 perform calculations recursively
    else:
        return 0

input = open("InputDay1.txt", "r")
req_fuel = 0
for line in input:
    req_fuel = req_fuel + fuel(int(line))
print(req_fuel)