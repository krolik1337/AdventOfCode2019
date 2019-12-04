#%%
input = open("InputDay2.txt", "r") #open file
puzzle = list(map(int, input.read().split(','))) #make a 'puzzle' list splitted by colon
puzzle[1] = 12 #switcharoo
puzzle[2] = 2
#%%
#adding two elements of a list
def opadd(list, index1, index2): 
    return list[index1] + list[index2]

#multiplying two elements of a list
def opmul(list, index1, index2):
    return list[index1] * list[index2]

index = 0
while puzzle[index] != 99:
    if puzzle[index] == 1:
        puzzle[puzzle[index+3]] = opadd(puzzle, puzzle[index+1], puzzle[index+2])
    else:
            puzzle[puzzle[index+3]] = opmul(puzzle, puzzle[index+1], puzzle[index+2])
    index+=4
print(puzzle[0])