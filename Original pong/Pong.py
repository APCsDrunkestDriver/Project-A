import arcade
import random
import time


#define a class for the left paddle

class left_paddle:
    #define a function to define the variables of the left paddle
    def __init__ (self,x,y,width,height,colour, move_speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.move_speed = move_speed
        self.moving_up = False
        self.moving_down = False

        #defines a funcion to draw the left paddle
    def draw(self):
        arcade.draw_rectangle_filled (self.x, self.y, self.width, self.height, self.colour)
    #stops the paddles from going outside the screen

    #define a function that updates the paddle each frame
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

#make a class for the window
class pong(arcade.Window):
    def random_vilocity():
        #makes a while loop to generate numbers until the y vilocity is one more than the x vilocity
        loop = True
        while loop == True:
                #generates a random number for the x vilocity between 1 and 5
                numx = random.uniform(0,5)
                #subtracts the y from the x so that the overall vilocity stays the same.
                numy = 5 - numx
                #checks if x is equal to or greater than one more than y
                if numx >= numy + 1:
                        #repeats the loop it isn't
                        loop = False
        #randomly decides to make the x or y negative so it can go backwards up or down
        mo_numx = numx * random.choice([1, -1])
        mo_numy = numy * random.choice([1, -1])
        #returns the finished vilocity
        return mo_numx, mo_numy

    #defines the init method which is called each time a new instance of the class is created
    def __init__(self):

        #define the window size and name
        super().__init__(640,480,"PONG")

        #defines the play variable for the menu
        self.play = False

        #define the bounce sound
        self.bounce_sound = arcade.load_sound("/Users/kobiaxtens/Library/CloudStorage/OneDrive-Personal/code/python/term 2/venv_pong.py/pygame pong/bounce_sound.wav")
        arcade.play_sound(self.bounce_sound)
        self.fail_sound = arcade.load_sound("/Users/kobiaxtens/Library/CloudStorage/OneDrive-Personal/code/python/term 2/venv_pong.py/pygame pong/fail_sound.wav")
        arcade.play_sound(self.fail_sound)

        #defines weather the game is paused or not
        self.paused = False

        #defines the score variables
        self.right_score = 0
        self.left_score = 0

        #define the left paddle
        self.left_paddle = left_paddle(50, 240, 7, 70, arcade.color.WHITE, move_speed=10)
        
        #define the right paddle
        self.right_paddle = right_paddle(590, 240, 7, 70, arcade.color.WHITE, move_speed=10)

        #calls the random vilocity function
        numx, numy = pong.random_vilocity()

        #define the ball
        self.ball = ball(300,200,10,10,arcade.color.WHITE, vilocity=(numx, numy))

    def reset_game(self):
        # Reset score variables
        self.right_score = 0
        self.left_score = 0

        # Reset ball position and velocity
        numx, numy = pong.random_vilocity()
        self.ball = ball(300, 200, 10, 10, arcade.color.WHITE, vilocity=(numx, numy))

    #defines a function that renders the game for each frame
    def on_draw(self):
        #displays the start menu
        if self.play == False:
            arcade.draw_text ("Welcome to Pong!", 100, 400, arcade.color.WHITE, 50)
            arcade.draw_text ("Press p to play multiplayer.", 100, 300, arcade.color.WHITE, 30)
            arcade.draw_text ("use arrows and w and s to move.", 50, 200, arcade.color.WHITE, 30)
            
            

        else:
            #draws the score
            text_colour = (255,255,255,220)
            arcade.draw_text (self.left_score, 140,320,text_colour, 100)
            arcade.draw_text (self.right_score, 450,320,text_colour, 100)

            #when the ball flys off the left screen
            if self.ball.x+self.ball.width*5 < 0:
                #resets the position of the ball
                numx, numy = pong.random_vilocity()
                self.ball.vilocity = (numx, numy)
                self.ball = ball(300,200,10,10,arcade.color.WHITE, vilocity=(numx, numy))
                #increases the right persons score by one
                self.right_score += 1
                #play fail sound
                arcade.play_sound(self.fail_sound)

            #when the ball flys off the right screen
            if self.ball.x-self.ball.width*5 > 640:
                #resets the position of the ball
                numx, numy = pong.random_vilocity()
                self.ball.vilocity = (numx, numy)
                self.ball = ball(300,200,10,10,arcade.color.WHITE, vilocity=(numx, numy))
                #increases the left persons score by one
                self.left_score += 1
                #play fail sound
                arcade.play_sound(self.fail_sound)

            #checks if 10 has been scored
            if self.right_score == 10:
                #displays the winner
                arcade.draw_text ("Right player wins!", 100, 200, arcade.color.WHITE, 30)
                arcade.draw_text ("Press f to play again", 100, 100, arcade.color.WHITE, 30)
                self.paused = True

            #checks if 10 has been scored
            if self.left_score == 10:
                #displays the winner
                arcade.draw_text ("Left player wins!", 100, 200, arcade.color.WHITE, 50)
                arcade.draw_text ("Press f to play again", 100, 100, arcade.color.WHITE, 30)
                self.paused = True



            
            #checks if the ball is touching the x axis and inverts its vilocity 
            if self.ball.y + self.ball.height/2 >= 480:
                self.ball.vilocity = (self.ball.vilocity[0], -self.ball.vilocity[1])
                #plays the bounce sound
                arcade.play_sound(self.bounce_sound)
            if self.ball.y - self.ball.height/2 <= 0:
                self.ball.vilocity = (self.ball.vilocity[0], -self.ball.vilocity[1])
                #plays the bounce sound
                arcade.play_sound(self.bounce_sound)


    #define a function to start the paddle moving
    def on_key_press(self, key, modifiers):
        #left paddle
        if self.play == False:
            if key == arcade.key.P:
                self.play = True
                self.reset_game()
                
        else:
            if key == arcade.key.W:
                self.left_paddle.moving_up = True
            elif key == arcade.key.S:
                self.left_paddle.moving_down = True
            #right paddle
            if key == arcade.key.UP:
                self.right_paddle.moving_up = True
            elif key == arcade.key.DOWN:
                self.right_paddle.moving_down = True
            if self.paused == True:
                self.paused = False
                if key == arcade.key.F:
                    self.reset_game()
                else:
                    self.paused = True

            
    #define a function to stop the paddle from moving
    def on_key_release(self, key, modifiers):
        #left paddle
        if key == arcade.key.W:
            self.left_paddle.moving_up = False
        elif key == arcade.key.S:
            self.left_paddle.moving_down = False
        #right paddles
        if key == arcade.key.UP:
            self.right_paddle.moving_up = False
        elif key == arcade.key.DOWN:
            self.right_paddle.moving_down = False
    

    def on_update(self, delta_time):
        if self.paused == False:
            #updates the paddles and ball each frame
            self.left_paddle.update()
            self.right_paddle.update()
            self.ball.update()

            #renders state of the game for each frame.
            arcade.start_render()

            #draws the dotted line.
            rectangle_color = (255,255,255,190)
            arcade.draw_rectangle_filled (320, 460, 7, 30, rectangle_color)
            arcade.draw_rectangle_filled (320, 400, 7, 30, rectangle_color)
            arcade.draw_rectangle_filled (320, 340, 7, 30, rectangle_color)
            arcade.draw_rectangle_filled (320, 280, 7, 30, rectangle_color)
            arcade.draw_rectangle_filled (320, 220, 7, 30, rectangle_color)
            arcade.draw_rectangle_filled (320, 160, 7, 30, rectangle_color)
            arcade.draw_rectangle_filled (320, 100, 7, 30, rectangle_color)
            arcade.draw_rectangle_filled (320, 40, 7, 30, rectangle_color)

            #draw the left paddle
            self.left_paddle.draw()

            #draw the left paddle
            self.right_paddle.draw()

            #draw the ball
            self.ball.draw()

            #checks if the ball collides with the x and y intercept of the right paddle
            if (self.ball.x + self.ball.width/2 >= self.right_paddle.x - self.right_paddle.width/2
            #checks if it isn't at the top of the paddle
            and not self.ball.y + self.ball.height/2 > self.right_paddle.y + self.right_paddle.height/2
            #checks if it isn't at the bottom of the paddle
            and not self.ball.y + self.ball.height/2 <= self.right_paddle.y-self.right_paddle.height/2
            #checks if it isn't in front of the paddle
            and not self.ball.x + self.ball.width/2 >= self.right_paddle.x + self.right_paddle.width/2):
                
                #plays the bounce sound
                arcade.play_sound(self.bounce_sound)

                #defines a function to make the vilocity equal 10
                def make_it_10():
                        x,y = self.ball.vilocity
                        #if x is negative
                        if x < 0 and y > 0:
                                #changes x to posative
                                x = x*-1
                                #finds the number to divide by
                                f=(x+y)/15
                                #dividees x and y by the factor
                                tenx = x/f
                                teny = y/f
                                #connverts x back into negative
                                tenx = tenx * -1
                                return tenx, teny
                        #if y is negative
                        elif y < 0 and x > 0:
                                #changes y to posative
                                y = y*-1
                                #finds the number to divide by
                                f=(x+y)/15
                                #dividees x and y by the factor
                                tenx = x/f
                                teny = y/f
                                #connverts y back into negative
                                tenx = tenx*-1
                                return tenx, teny
                        #if x and y is negative
                        elif x < 0 and y < 0:
                                y = y*-1
                                x = x*-1
                                #finds the number to divide by
                                f=(x+y)/10
                                #dividees x and y by the factor
                                tenx = x/f
                                teny = y/f
                                #connverts x and y back into negative
                                tenx = tenx * -1
                                teny = teny * -1
                                return tenx, teny

                        else:
                                f=(x+y)/15
                                #finds the number to divide by
                                #dividees x and y by the factor
                                tenx = x/f
                                teny = y/f
                                return tenx, teny

            #changes the balls vilocity depending on were you hit it
                #gets the distance from the middle of the paddle to were the ball is hitting it.
                ball_location_on_paddle = self.right_paddle.y-self.ball.y
                #devides the location by negative 5 in order to keep the y moving in the same direction and find a vilocity for it to be
                new_yvillocity = ball_location_on_paddle/-5
                #subtracts 10 from the y vilocity to find the x vilocity
                new_xvillocity = (10-new_yvillocity)*-1
                #defines the new vilocitys as the actual balls vilocity
                self.ball.vilocity = (new_xvillocity, new_yvillocity)
                
                #calls the make_it_10 function to make sure the ball doesn't fly away at a million miles an hour
                self.ball.vilocity = make_it_10()

                #stops the y vilocity form being larger than the x vilocity
                number = -1
                while number < 0:
                    #converts the x and y vilocity into absolute values
                    xnumber = abs(self.ball.vilocity[0])
                    ynumber = abs(self.ball.vilocity[1])
                    #subtracts the numbers to find if the x vilocity is too big.
                    number = xnumber - ynumber
                    #changes the x and y vilocity by 0.2
                    ball_vilocity_x = self.ball.vilocity[0] + 0.1
                    ball_vilocity_y = self.ball.vilocity [1] - 0.1
                    #defines the new vilocity
                    self.ball.vilocity = (ball_vilocity_x, ball_vilocity_y)
                #checks if the vilocity is good and does it ag
                vilocityx,vilocityy = self.ball.vilocity
                if vilocityx < 0:
                    vilocityx * -1

            #checks if the ball collides with the x and y intercept of the left paddle
            if (self.ball.x - self.ball.width/2 < self.left_paddle.x + self.left_paddle.width/2
            #checks if it isn't at the top of the paddle
            and not self.ball.y + self.ball.height/2 > self.left_paddle.y + self.left_paddle.height/2
            #checks if it isn't at the bottom of the paddle
            and not self.ball.y + self.ball.height/2 < self.left_paddle.y-self.left_paddle.height/2
            #checks if it isn't in front of the paddle
            and not self.ball.x + self.ball.width/2 < self.left_paddle.x + self.left_paddle.width/2):
            
            
                
                #plays the bounce sound
                arcade.play_sound(self.bounce_sound)

                #defines a function to make the vilocity equal 10
                def make_it_10():
                        x,y = self.ball.vilocity
                        #if x is negative
                        if x < 0 and y > 0:
                                #changes x to posative
                                x = x*-1
                                #finds the number to divide by
                                f=(x+y)/10
                                #dividees x and y by the factor
                                tenx = x/f
                                teny = y/f
                                #connverts x back into negative
                                tenx = tenx * -1
                                return tenx, teny
                        #if y is negative
                        elif y < 0 and x > 0:
                                #changes y to posative
                                y = y*-1
                                #finds the number to divide by
                                f=(x+y)/10
                                #dividees x and y by the factor
                                tenx = x/f
                                teny = y/f
                                #connverts y back into negative
                                tenx = tenx*-1
                                return tenx, teny
                        #if x and y is negative
                        elif x < 0 and y < 0:
                                y = y*-1
                                x = x*-1
                                f=(x+y)/10
                                #finds the number to divide by
                                #dividees x and y by the factor
                                tenx = x/f
                                teny = y/f
                                #connverts x and y back into negative
                                tenx = tenx * -1
                                teny = teny * -1
                                return tenx, teny

                        else:
                                #finds the number to divide by
                                f=(x+y)/10
                                #dividees x and y by the factor
                                tenx = x/f
                                teny = y/f
                                return tenx, teny
                            
                #changes the balls vilocity depending on were you hit it
                #gets the distance from the middle of the paddle to were the ball is hitting it.
                ball_location_on_paddle = self.right_paddle.y-self.ball.y
                #devides the location by negative 5 in order to keep the y moving in the same direction and find a vilocity for it to be
                new_yvillocity = ball_location_on_paddle/-5
                #subtracts 10 from the y vilocity to find the x vilocity
                new_xvillocity = (10-new_yvillocity)*-1
                #defines the new vilocitys as the actual balls vilocity
                self.ball.vilocity = (new_xvillocity, new_yvillocity)
                
                #calls the make_it_10 function to make sure the ball doesn't fly away at a million miles an hour 
                self.ball.vilocity = make_it_10()

                #stops the y vilocity form being larger than the x vilocity
                number = -1
                while number < 0:
                    #converts the x and y vilocity into absolute values
                    xnumber = abs(self.ball.vilocity[0])
                    ynumber = abs(self.ball.vilocity[1])
                    #subtracts the numbers to find if the x vilocity is too big.
                    number = xnumber - ynumber
                    #changes the x and y vilocity by 0.2
                    ball_vilocity_x = self.ball.vilocity[0] + 0.1
                    ball_vilocity_y = self.ball.vilocity [1] - 0.1
                    #defines the new vilocity
                    self.ball.vilocity = (ball_vilocity_x, ball_vilocity_y)

                #checks if the vilocity is in the correct direction
                vilocityx,vilocityy = self.ball.vilocity
                print(vilocityx)
                if vilocityx < 0:
                    vilocityx = vilocityx * -1
                    self.ball.vilocity = (vilocityx, vilocityy)



#starts the game loop
game = pong()
arcade.run()