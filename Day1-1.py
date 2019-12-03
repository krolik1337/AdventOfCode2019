import math
input = open("InputDay1.txt", "r") 
req_fuel = 0
for line in input:
    req_fuel = req_fuel + (math.floor(int(line) / 3) - 2) #for each input line add subsum according to formula
print(req_fuel)