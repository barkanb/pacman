"""
Write a module docstring here
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

    #moving along the grid. 
    def traverse():
        global position
        for i in moveList: 
            if (i == "N") :
                newPos = position[0], position[1]+1
                if (coinAction(newPos)) :
                    position = newPos
                #print (position)
            elif (i == "S"):
                newPos = position[0], position[1]-1
                if (coinAction(newPos)) :
                    position = newPos
                #print (position)
            elif (i == "E"):
                newPos = position[0]+1, position[1]
                if (coinAction(newPos)) :
                    position = newPos
                #print (position)
            elif (i == "W"):
                newPos = position[0]-1, position[1]
                if (coinAction(newPos)) :
                    position = newPos
                #print (position)


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
        if cnt == 1:    #get grid size
            arguments = line.strip().split()
            if (len(arguments) != 2 or (not (arguments[0]).isnumeric()) or (not (arguments[1]).isnumeric()) ):
                return sendError()
            gridX = int(arguments[0])
            gridY = int(arguments[1])  

            if (gridX< 0 or gridY <0):
                return sendError()

            grid= [[1 for y in range(gridY)] for x in range(gridX)] 
        
        elif cnt == 2:    #get initial position
            arguments = line.strip().split()
            if (len(arguments) != 2 or (not (arguments[0]).isnumeric()) or (not (arguments[1]).isnumeric()) ):
                return sendError()
            position = int(arguments[0]), int(arguments[1])
            if position[0] < 0 or position[1]< 0 or position[0]>= gridX or position[1] >= gridY:
                return sendError()
            grid[position[0]] [position[1]] = 0
            
        elif cnt == 3:     #get moves
            arguments = line.strip()
            if (not bool(re.fullmatch('^[W,N,E,S]+$', arguments)) or len(arguments)==0):
                return sendError()
            moves = arguments
        
        else:       #all other lines describe walls. 
            arguments = line.strip().split()
            if (len(arguments) != 2 or (not (arguments[0]).isnumeric()) or (not (arguments[1]).isnumeric()) ):
                return sendError()
            wallX = int(arguments[0])
            wallY = int(arguments[1])
            if wallX < 0 or wallY< 0 or wallX>= gridX or wallY >= gridY:
                return sendError()
            grid[wallX] [wallY] = 2

        line = fp.readline()
        cnt += 1

    fp.close()

    if cnt<3: 
        return sendError()
   
    #movement list from movement arguments. 
    global moveList 
    moveList= list(moves)    


    traverse()
     # return final_pos_x, final_pos_y, coins_collected 
    return(position[0], position[1], coin)



#uncomment for testing. 
#pacman("input.txt");
