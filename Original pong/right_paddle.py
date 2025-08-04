import arcade

#define a class for the right paddle
class right_paddle:
    
    #defines a function to define the variables of the left paddle
    def __init__ (self,x,y,width,height,colour, move_speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.move_speed = move_speed
        self.moving_up = False
        self.moving_down = False

        #defines a function to draw the right paddle.
    def draw(self):
        arcade.draw_rectangle_filled (self.x, self.y, self.width, self.height, self.colour)

    def update(self):
        #stops the paddles x value from being more than the screens top
        if self.y + self.height/2 > 480:
            self.moving_up = False
        
        #stops the paddle x value from being less that the screens bottom
        if self.y - self.height/2 < 0:
            self.moving_down = False

        #moves the paddle  up
        if self.moving_up:
            self.y += self.move_speed

        #moves the paddle down
        elif self.moving_down:
            self.y -= self.move_speed
