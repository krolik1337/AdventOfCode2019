input = list(map(int, open("InputDay8.txt", "r").read())) #make a list of digits from input
width = 25
height = 6
message=[] #make a list for our message
for x in range(width*height): #loop through whole layer
    index = x
    while input[index] == 2: #if pixel is still transparent...
        index+=height*width  #... go to the same pixel on deeper layer...
    message.append(input[index]) #...then add first non-trnasparent pixel to our message
for x in range(len(message)): #print output message kinda 'readable' way
    if (x+1) % 25 != 0:
        print(message[x], end='') #print without newline
    else:
        print(message[x])