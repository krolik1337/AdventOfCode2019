input = list(map(int, open("InputDay8.txt", "r").read())) #make a list of digits from input
width = 25
height = 6
layers = len(input)//(width*height) #calculate number of layers
zeros = [0] * layers #make a list for counting digits on every layer (one on every index)
ones = [0] * layers
twos = [0] * layers
for x, y in zip(input, range(len(input))): #loop through whole input x is the value of pixel, y is pixel's index
    if x == 0:
        zeros[y//(height*width)]+=1 #change list values according to current x
    elif x == 1:    
        ones[y//(height*width)]+=1
    elif x == 2:
        twos[y//(height*width)]+=1
minIndex=zeros.index(min(zeros)) #get index of layer with fewest 0's
print(ones[minIndex]*twos[minIndex]) #print output