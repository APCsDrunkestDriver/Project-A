#Imports neccessary framework
import pygame
import random

# AIPlayer class for controlling the right paddle
class AIPlayer:
    def decide(self, ball_x, ball_y, paddle_y):
        # Simple AI logic: follow the ball's vertical position
        paddle_center = paddle_y + 50  # assuming paddle height is 100
        if ball_y < paddle_center - 10:
            return "up"
        elif ball_y > paddle_center + 10:
            return "down"
        else:
            return "stay"
#Initializes Pygame
pygame.init()
#Set up the window: width + height
window_width = 800
window_height = 400
window = pygame.display.set_mode([window_width, window_height])
pygame.display.set_caption('Single Player PyPong')  # Changed caption to reflect single player
clock = pygame.time.Clock()
#Loads sound effects for bounce + score
# Load sound effects
bounce_sounds = [
    pygame.mixer.Sound("main/resources/SFX/bounce.wav"),
    pygame.mixer.Sound("main/resources/SFX/bounce2.wav"),
    pygame.mixer.Sound("main/resources/SFX/bounce3.wav"),
]
# Removed bounce_sound here; we'll play a random one on collision instead
# Add score sound
try:
    score_sound = pygame.mixer.Sound("main/resources/SFX/scoresfx/score.wav")
except:
    score_sound = None
    print("Score sound file not found.")
#Ball class definition
class Ball:
    #Initializes ball attributes: position, velocity, radius, color
    def __init__(self):
        self.x = window_width // 2
        self.y = window_height // 2
        self.xVel = 5.0
        self.yVel = 5.0
        self.radius = 10
        self.colour = (255, 255, 255)
    #Serves the ball by resetting its position and assigning random velocities
    def serve(self):
        self.x = window_width // 2
        self.y = window_height // 2
        self.xVel = random.uniform(1.0, 5.0)
        self.yVel = random.uniform(1.0, 5.0)

    def move(self): #Updates the ball's position based on its velocity repeatedly
        self.x += self.xVel
        self.y += self.yVel
#Draws the ball on the window
    def draw(self):
        pygame.draw.circle(window, self.colour, (int(self.x), int(self.y)), self.radius)
#Checks for collisions with paddles and window edges
    def check_collision(self, paddles):
        if self.y - self.radius <= 0 or self.y + self.radius >= window_height:
            self.yVel *= -1
            self.yVel += random.uniform(-5.0, 5.0)
            random.choice(bounce_sounds).play()
        for paddle in paddles:
            if paddle.x <= self.x <= paddle.x + paddle.width and paddle.y <= self.y <= paddle.y + paddle.height:
                self.xVel *= -1
                self.xVel += random.uniform(-5.0, 5.0)
                random.choice(bounce_sounds).play()
#score: Checks if the ball has scored on either side
    def check_score(self):
        if self.x - self.radius <= 0:
            if score_sound:
                score_sound.play()
            return "right"
        elif self.x + self.radius >= window_width:
            if score_sound:
                score_sound.play()
            return "left"
        return None
#Paddle class definition  
class Paddle:
   #Initializes paddle traits: position, color, size, speed
    def __init__(self, x, colour):
        self.x = x
        self.y = window_height // 2 - 50
        self.width = 10
        self.height = 100
        self.colour = colour
        self.speed = 9
#Moves the paddle up at a consistent speed
    def move_up(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 0
#Moves the paddle down at a consistent speed
    def move_down(self):
        self.y += self.speed
        if self.y > window_height - self.height:
            self.y = window_height - self.height
#Draws the paddle on the window
    def draw(self):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))
#Draws the left and right paddles with different colour
left_paddle = Paddle(20, (0, 255, 255))#cyan paddle
# Draws the left and right paddles with different colour
right_paddle = Paddle(window_width - 30, (255, 0, 0))#red paddle
# Initialize AI player for right paddle
ai = AIPlayer()
#Creates and serves the ball
ball = Ball()
ball.serve()
#Initialisation of score
left_score = 0
right_score = 0
#Loads font for scoreboard
try:
    font = pygame.font.Font("main/resources/Montserrat/static/Montserrat-Light.ttf", 27)
except:
    font = pygame.font.SysFont(None, 27)
    print("Custom font not found. Using default system font.")
#Updates the scoreboard with the current score
def update_scoreboard():
    left_text = font.render((f"Player 1: {left_score}"), True, (0, 255, 255))
    right_text = font.render((f"Player 2: {right_score}"), True, (255, 0, 0))
    window.blit(left_text, (20, 20))
    window.blit(right_text, (window_width - right_text.get_width() - 20, 20))
#Main game loop
def game_loop():
    #Declares Global Variables for Scores
    global left_score, right_score
    left_score = 0
    right_score = 0
    active = True
#runs game loop
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                # Prevent quitting from within the loop from calling pygame.quit() early
                return
        #gets state of all keys 
        keys = pygame.key.get_pressed()
    #Moves the left paddle with 'W' and 'S' keys
        if keys[pygame.K_w]:
            left_paddle.move_up()
        if keys[pygame.K_s]:
            left_paddle.move_down()
    # AI controls right paddle
        decision = ai.decide(ball.x, ball.y, right_paddle.y)
        if decision == "up":
            right_paddle.move_up()
        elif decision == "down":
            right_paddle.move_down()
#Fills the window with a dark color (very dark grey)
        window.fill((10, 10, 10))
#Moves and draw the ball, checks for collisions and scoring
        ball.move()
        ball.draw()
        ball.check_collision([left_paddle, right_paddle])
#Checks if the ball has scored on either side
        scored_side = ball.check_score()
        if scored_side == "left":
            left_score += 1
            ball.serve()
        elif scored_side == "right":
            right_score += 1
            ball.serve()
#draws the paddles
        left_paddle.draw()
        right_paddle.draw()
        #update and display the scoreboard
        update_scoreboard()
#updates the display and controls the refresh rate
        pygame.display.update()
        clock.tick(60)

# Define an entry point for importing
def run_game():
    game_loop()
    pygame.quit()

# If the file is run directly, start the game
if __name__ == "__main__":
    run_game()
