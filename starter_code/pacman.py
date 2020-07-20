"""
Write a module docstring here
"""

__author__ = "Boris Barkan"

gold = 0

def pacman(input_file):
    """ Use this function to format your input/output arguments. Be sure not to change the order of the output arguments. 
    Remember that code organization is very important to us, so we encourage the use of helper fuctions and classes as you see fit.
    
    Input:
        1. input_file (String) = contains the name of a text file you need to read that is in the same directory, includes the ".txt" extension
           (ie. "input.txt")
    Outputs:
        1. final_pos_x (int) = final x location of Pacman
        2. final_pos_y (int) = final y location of Pacman
        3. coins_collected (int) = the number of coins that have been collected by Pacman across all movements
    """

    #read file
    fp = open(input_file, 'r')

    gridX =0
    gridY =0

    #initial position
    global position
    position = 0 , 0
    
    moves =""
    wallList= []
    global grid

    line = fp.readline()
    cnt = 1
    while line:
        if cnt == 1:
            arguments = line.strip().split()
            gridX = int(arguments[0])
            gridY = int(arguments[1])  
            grid= [[1 for x in range(gridX)] for y in range(gridY)] 
        elif cnt == 2:
            arguments = line.strip().split()
            position = int(arguments[0]), int(arguments[1])
            grid[position[0]] [position[1]] = 0
        elif cnt == 3:
            arguments = line.strip()
            moves = arguments
        else:
            arguments = line.strip().split()
            grid[int(arguments[0])] [int(arguments[1])] = 2

        print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1

   



    #movement list
    global moveList 
    moveList= list(moves)    

    #walls
    wall1 = 1,1
    wall2 = 1,2

    #updating grid
    grid[position[0]] [position[1]] = 0


    #print (grid)
    #print (moveList)

    # return final_pos_x, final_pos_y, coins_collected 


    def traverse():
        global position
        for i in moveList: 
            if (i == "N") :
                newPos = position[0], position[1]+1
                if (goldAction(newPos)) :
                    position = newPos
                print (position)
            elif (i == "S"):
                newPos = position[0], position[1]-1
                if (goldAction(newPos)) :
                    position = newPos
                print (position)
            elif (i == "E"):
                newPos = position[0]+1, position[1]
                if (goldAction(newPos)) :
                    position = newPos
                print (position)
            elif (i == "W"):
                newPos = position[0]-1, position[1]
                if (goldAction(newPos)) :
                    position = newPos
                print (position)


    def goldAction(position):
        global grid
        if ((position[0] >= gridX) or (position[1] >= gridY)):
            return 0;
        elif ((position[0] <0 ) or (position[1] <0 )):
            return 0;
        elif (grid[position[0]][position[1]] ==2):
            return 0;
        elif (grid[position[0]][position[1]] ==1):
            global gold 
            gold=  gold+1
            grid[position[0]][position[1]] = 0
            return 1
        elif (grid[position[0]][position[1]] ==0):
            return 1

    traverse()
    print(gold)
    fp.close()


pacman("/Users/bo/repo/C3/packman-fork/starter_code/input.txt");
print(grid)
print(position)
