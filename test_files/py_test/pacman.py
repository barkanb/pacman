
""" 
The code navigates a 2-dimensional board with obstacles (walls) covered in coins which are picked up when moved over, similar to a simplified Pacman game. 

The function takes an input file of a specific format that describes the board in a form of a grid. 
It also  describes the walls and provides a list of sequential moves on that board for the Packman object.
The function returns the final coordinates after following the movement instructions and the number of spaces visited (thus describing the number of coins that were picked up by Packman). 
Format issues and general exceptions will provide an error output of (-1,-1,0)

Parameters: 
    input_file (str): Local file name. It provides the grid, walls, starting position and a movement list. 

Returns:
	(int, int, int): Final position on X axis, final position on Y axis, number of coins collected

"""

import os
import sys
import re

__author__ = "Boris Barkan"

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
    #------------Helper functions-------------------

    #moving along the grid bases on the move list. 
    #Edges and walls will prevent a move. 
    #After move position is updated. 
    def traverse():
        global position
        for i in moveList: 
            if (i == "N") :
                newPos = position[0], position[1]+1
                if (coinAction(newPos)) :
                    position = newPos

            elif (i == "S"):
                newPos = position[0], position[1]-1
                if (coinAction(newPos)) :
                    position = newPos

            elif (i == "E"):
                newPos = position[0]+1, position[1]
                if (coinAction(newPos)) :
                    position = newPos

            elif (i == "W"):
                newPos = position[0]-1, position[1]
                if (coinAction(newPos)) :
                    position = newPos


    #check next move and coin count. 
    def coinAction(position):
        global grid
        if ((position[0] >= gridX) or (position[1] >= gridY)):
            return 0;
        elif ((position[0] <0 ) or (position[1] <0 )):
            return 0;
        elif (grid[position[0]][position[1]] ==2):
            return 0;
        elif (grid[position[0]][position[1]] ==1):
            global coin 
            coin=  coin+1
            grid[position[0]][position[1]] = 0
            return 1
        elif (grid[position[0]][position[1]] ==0):
            return 1

    #Error sent.
    def sendError():
        return (-1,-1,0)

    #----------------end helper functions-------------------------

    

    #read file from same folder
    fp = open(os.path.join(sys.path[0], input_file), 'r')

    #initialize grid attributes, coin count, position, moves and so on. 
    global grid
    gridX =0
    gridY =0

    global coin
    coin = 0   

    global position
    position = 0 , 0 

    moves =""
    wallList= []

    #read lines of the file for instructions. 
    line = fp.readline()
    cnt = 1
    while line:

        #get grid size from first line per instructions. 
        #Validation rules are checked and throws an error when an issue is discovered. 
        if cnt == 1: 
            arguments = line.strip().split()

            #check for arguments and values
            if (len(arguments) != 2 or (not (arguments[0]).isnumeric()) or (not (arguments[1]).isnumeric()) ):
                return sendError()
            gridX = int(arguments[0])
            gridY = int(arguments[1])  

            if (gridX< 0 or gridY <0):
                return sendError()

            #pupulate a new grid
            grid= [[1 for y in range(gridY)] for x in range(gridX)] 
        

        #get initial position on line 2 per instructions.
        elif cnt == 2:  
            arguments = line.strip().split()

            #check for arguments and values
            if (len(arguments) != 2 or (not (arguments[0]).isnumeric()) or (not (arguments[1]).isnumeric()) ):
                return sendError()
            position = int(arguments[0]), int(arguments[1])
            if position[0] < 0 or position[1]< 0 or position[0]>= gridX or position[1] >= gridY:
                return sendError()

            #populate start point (0 stands for no coins)    
            grid[position[0]] [position[1]] = 0
            
        #get moves from line 3 per instructions
        elif cnt == 3:     
            arguments = line.strip()

            #check allowed syntax
            if (not bool(re.fullmatch('^[W,N,E,S]+$', arguments)) or len(arguments)==0):
                return sendError()
            moves = arguments
        
        #all other lines describe walls. 
        else: 
            arguments = line.strip().split()
            if (len(arguments) != 2 or (not (arguments[0]).isnumeric()) or (not (arguments[1]).isnumeric()) ):
                return sendError()
            wallX = int(arguments[0])
            wallY = int(arguments[1])
            if wallX < 0 or wallY< 0 or wallX>= gridX or wallY >= gridY:
                return sendError()
            
            #Populated the walls on the grid with the nu,ber '2' to designate that its a wall.
            grid[wallX] [wallY] = 2

        #moving through the file lines.
        line = fp.readline()
        cnt += 1

    fp.close()

    #if the file has less then 3 lines it should throw an error.
    if cnt<3: 
        return sendError()
   
    #movement list from movement arguments. 
    global moveList 
    moveList= list(moves)    

    #start the movements
    traverse()
     # return final_pos_x, final_pos_y, coins_collected 
    return(position[0], position[1], coin)



#uncomment for testing. 
#pacman("input.txt");
