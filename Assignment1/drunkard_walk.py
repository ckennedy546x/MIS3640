# This function includes solutions to problems 3 AND 4.  
# Both are solved by running this function 

import turtle
import random #calls upon both the turtle and random packages

def drunkard_walk(step_size, step_number):
    '''A drunkard in a grid of streets randomly 
    picks one of four directions and stumbles to the next 
    intersection, then again randomly picks one of four 
    directions, and so on. This function calculates the distance
    after n intersections. It also uses Turtle to draw the 
    drunkard's walk'''
    distance = 0 # At outset, drunkard hasn't moved yet, so the distance is 0
    for i in range(step_number): #This run a loop that will run each movement (or intersection) in the determined amount of steps
        turtle.setheading(90 * random.randint(0, 3)) #This will generate a random number between 0 and 3 that will multiply by 90.  The result will be the angle the drunkard travels in which will either bu right, left, up, or down.
        turtle.forward(step_size) #This will tell the drunkard how far to move during this indvidual step before the next turn.
        distance = distance + step_size #This will calculate the new distance after every turn and walk up until the next turn. It will take the total distance and add the current distance that was just traveled from the last turn. The next element will be ran and will repeat this process until all the steps (aka turns) have been completed.
    return distance #This will return the final distance after the entire loop is completed.
        

    
print("The drunkard has traveled a distance of", drunkard_walk(15,20)) #This will run the function