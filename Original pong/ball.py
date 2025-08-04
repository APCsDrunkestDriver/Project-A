import arcade

#define a class for the ball
class ball:
    #defines a function to define the variables of the ball
    def __init__ (self,x,y,width,height,colour,vilocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.vilocity = vilocity
        self.first_hit = True

    #define a function to draw the ball
    def draw(self):
        arcade.draw_rectangle_filled (self.x, self.y, self.width, self.height, self.colour)

    #define a function to update the ball each frame
    def update(self):
        #moves the ball by its coresponding vilocity
        self.x+=self.vilocity[0]
        self.y+=self.vilocity[1]
