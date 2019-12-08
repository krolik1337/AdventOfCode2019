def orbits(planet, path):
    if planets[orbiters.index(planet)] == 'COM': #if planet orbits COM directly, insert it at the front...
        path.insert(0, planets[orbiters.index(planet)])
        return path
    else: #...else trace back to COM adding visited planets to the list
        path.insert(0, planets[orbiters.index(planet)])
        return orbits(planets[orbiters.index(planet)], path)
input = open("InputDay6.txt", "r") #open file
pairs = input.read().split('\n') #split file into list of pairs
planets = [x[:3] for x in pairs] # separate both pairs
orbiters = [x[4:] for x in pairs]
index = 0 #declare path for me, santa, and index of crossing point
myPath = []
santaPath = []
santaPath = orbits(orbiters[orbiters.index('SAN')], santaPath) #make paths for both santa and me
myPath = orbits(orbiters[orbiters.index('YOU')], myPath)
for x, y in zip(myPath, santaPath): #loop through both paths to determine index of crossing point
    if x != y:
        break
    index+=1
print(len(myPath[index:])+len(santaPath[index:])) #print sum of path lengths starting from crossing point