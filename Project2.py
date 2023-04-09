# File: Project2.py
# Student: Noah Graham
# UT EID: nlg838
# Course Name: CS303E
# 
# Date: 4/3/23
# Description of Program: Creates a car class that can be controlled like a toy car

import random
# Maybe other imports if you need them.

# Constants:
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

def dirConvert(n):
    # Turns the direction into a string
    if n == EAST:
        return "East"
    elif n == NORTH:
        return "North"
    elif n == WEST:
        return "West"
    elif n == SOUTH:
        return "South"
    
class ToyCar:

    def __init__( self, x = 0, y = 0, d = EAST ):
        # Command should fail and print "ERROR: Illegal direction entered." 
        # if the provided direction is invalid.
        if d != NORTH and d != WEST and d != EAST and d != SOUTH:
            print("ERROR: Illegal direction entered.")
        else:
            self.x = x
            self.y = y
            self.direction = d

    def __str__( self ):
        """ Generate a string containing information on 
        the class object. """
        return "Your car is at location ("+ str(self.x) + ", "+ str(self.y) + "), heading "+ dirConvert(self.direction)
    
    def setDir(self, n):
        # validate the parameter and then set the direction accordingly
        if n == NORTH or n == WEST or n == EAST or n == SOUTH:
             self.direction = n
        print("DEBUG: setting direction", dirConvert(self.direction))
    
    def getDir(self):
        # return the direction (one of 0, 90, 180, 270)
        return self.direction

    def getX(self):
        # return the X coordinate of the car's location
        return self.x

    def getY(self): 
        #return the Y coordinate of the car's location
        return self.y

    def turnLeft( self ):
        #change direction 90 degrees to the left
        self.direction += 90
        if self.direction > 270:
            self.direction = 0
        print("DEBUG: turning", dirConvert(self.direction))
    
    def turnRight(self): 
        #change direction 90 degrees to the right
        self.direction -= 90
        if self.direction < 0:
            self.direction = 270
        print("DEBUG: turning", dirConvert(self.direction))

    def forward(self, n): 
        #validate that n is non-negative and then move the car in the current direction
        if n > 0:
            if self.direction == NORTH:
                self.y += n
            elif self.direction == WEST:
                self.x -= n
            elif self.direction == EAST:
                self.x += n
            elif self.direction == SOUTH:
                self.y -= n
            print("DEBUG: moving forward", str(n))
        else:
            print("ERROR: Illegal distance entered.")


# The other functions you'll need to supply.  You can have more, but
# must have at least these four.

def randomDrive( car, n ):
    # Moves the car in a random direction between 0-100 times for n turns
    if n > 0:
        for i in range(n):
            randNum = random.randint(1,3)
            if randNum == 1:
                car.turnLeft()
            elif randNum == 3:
                car.turnRight()
            car.forward(random.randint(0,100))
    else:
        print("ERROR: Illegal value entered.")
                


def goto( car, x, y ):
    # Makes the car move to a specificied coordinate through the x and y planes
    if car.getX() < x:
        car.setDir(EAST)
        car.forward(x-car.getX())
    else:
        car.setDir(WEST)
        car.forward(car.getX()-x)
    if car.getY() < y:
        car.setDir(NORTH)
        car.forward(y-car.getY())
    else:
        car.setDir(SOUTH)
        car.forward(car.getY()-y)


def gasStation():
    # Gives the coordinates of a mobile gas station between -100,100 x and y
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    print("Located gas station at (", x, ", ", y, ")", sep="")
    return x,y

def gasUp(car):
    x, y = gasStation()
    goto(car, x, y)
