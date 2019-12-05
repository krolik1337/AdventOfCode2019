input = open("InputDay3.txt", "r") #open file
wires = input.read().split('\n')
wire1 = wires[0].split(',')
wire2 = wires[1].split(',')
w1coord = w2coord = {'x_axis':0, 'y_axis':0}
wire1path = wire2path = commonpoints = list()
for x in wire1:
    direction = x[:1]
    distance = x[1:]
    if direction == 'U':
        w1coord['y_axis']+=int(distance)
    elif direction == 'D':
        w1coord['y_axis']-=int(distance)
    elif direction == 'L':
        w1coord['x_axis']-=int(distance)
    elif direction == 'R':
        w1coord['x_axis']+=int(distance)
    wire1path.append([w1coord['x_axis'], w1coord['y_axis']])
for x in wire2:
    direction = x[:1]
    distance = x[1:]
    if direction == 'U':
        w2coord['y_axis']+=int(distance)
    elif direction == 'D':
        w2coord['y_axis']-=int(distance)
    elif direction == 'L':
        w2coord['x_axis']-=int(distance)
    elif direction == 'R':
        w2coord['x_axis']+=int(distance)
    wire2path.append([w2coord['x_axis'], w2coord['y_axis']])
for x in range(len(wire1path)):
    for y in range(len(wire2path)):
        if wire1path[x][0] == wire2path[y][0] and wire1path[x][1] == wire2path[y][1]:
            commonpoints.append(wire1path[x])
