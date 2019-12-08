def orbits(planet):
    if planets[orbiters.index(planet)] == endpoint: #if planet orbits endpoint directly, return 1...
        return 1
    else: #else trace back to endpoint
        return 1 + orbits(planets[orbiters.index(planet)])
endpoint = 'COM'       
input = open("InputDay6.txt", "r") #open file
pairs = input.read().split('\n') #split file into list of pairs
planets = [x[:3] for x in pairs] # separate both pairs
orbiters = [x[4:] for x in pairs]
output = 0
for x in orbiters: # add up all subsums od direct and indirect orbits
    output+=orbits(x)
print(output)