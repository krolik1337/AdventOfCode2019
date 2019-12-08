input = open("InputDay3.txt", "r") #open file
wires = input.read().split('\n')
wire1 = wires[0].split(',')
wire2 = wires[1].split(',')
w1coord = {'x_axis':0, 'y_axis':0}
w2coord = {'x_axis':0, 'y_axis':0}
wire1path = []
wire2path = []
commonpoints = []
for x in wire1:
    direction = x[:1]
    distance = x[1:]
    y=0
    for y in range(int(distance)):
        if direction == 'U':
            w1coord['y_axis']+=1
        elif direction == 'D':
            w1coord['y_axis']-=1
        elif direction == 'L':
            w1coord['x_axis']-=1
        elif direction == 'R':
            w1coord['x_axis']+=1
        wire1path.append([w1coord['x_axis'], w1coord['y_axis']])
for x in wire2:
    direction = x[:1]
    distance = x[1:]
    y=0
    for y in range(int(distance)):
        if direction == 'U':
            w2coord['y_axis']+=1
        elif direction == 'D':
            w2coord['y_axis']-=1
        elif direction == 'L':
            w2coord['x_axis']-=1
        elif direction == 'R':
            w2coord['x_axis']+=1
        if [w2coord['x_axis'], w2coord['y_axis']] in wire1path:
            commonpoints.append([w2coord['x_axis'], w2coord['y_axis']])
manhattan = [abs(distance[0])+abs(distance[1]) for distance in commonpoints]
print(min(manhattan))