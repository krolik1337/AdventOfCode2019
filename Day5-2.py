input = open("InputDay5.txt", "r") #open file
puzzle = list(map(int, input.read().split(','))) #make a 'puzzle' list splitted by colon

inputValue = 5
def mode(type, list, index): #return value depending on immediate or position mode
    if type == 1:
        return list[index]
    else:
        return list[list[index]]

index = 0
while puzzle[index] != 99:
    instruction = [int(x) for x in str(puzzle[index])] #make a list of instruction digits, fill to len(5) with zeros if needed
    while len(instruction) < 5:
        instruction.insert(0,0)
    if instruction[-1] == 1:
        #opcode 1: add values from next two indexes/addresses, save it under address from 3rd
        puzzle[puzzle[index+3]] = mode(instruction[-3], puzzle, index+1) + mode(instruction[-4], puzzle, index+2)
        index+=4
    elif instruction[-1] == 2:
        #opcode 2: multiply values from next two indexes/addresses, save it under address from 3rd
        puzzle[puzzle[index+3]] = mode(instruction[-3], puzzle, index+1) * mode(instruction[-4], puzzle, index+2)
        index+=4
    elif instruction[-1] == 3:
        #opcode 3: take input value and save it under address from next index
        puzzle[puzzle[index+1]]=inputValue
        index+=2
    elif instruction[-1] == 4:
        #opcode 4: output value from address from next index
        print(puzzle[puzzle[index+1]])
        index+=2
    elif instruction[-1] == 5:
        #opcode 5: if first value is non-zero, jump to index from second value
        if mode(instruction[-3], puzzle, index+1) != 0:
            index = mode(instruction[-4], puzzle, index+2)
        else: 
            index+=3
    elif instruction[-1] == 6:
        #opcode 6: if first value is zero, jump to index from second value
        if mode(instruction[-3], puzzle, index+1) == 0:
            index = mode(instruction[-4], puzzle, index+2)
        else: 
            index+=3
    elif instruction[-1] == 7:
        #opcode 7: if first value is less than second, write 1 to address from 3rd parameter, otherwise write 0
        if mode(instruction[-3], puzzle, index+1) < mode(instruction[-4], puzzle, index+2):
            puzzle[puzzle[index+3]] = 1
        else: 
            puzzle[puzzle[index+3]] = 0
        index+=4
    elif instruction[-1] == 8:
        #opcode 8: if first value is equal to second, write 1 to address from 3rd parameter, otherwise write 0
        if mode(instruction[-3], puzzle, index+1) == mode(instruction[-4], puzzle, index+2):
            puzzle[puzzle[index+3]] = 1
        else: 
            puzzle[puzzle[index+3]] = 0
        index+=4