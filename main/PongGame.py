# game.py
import pygame
from ai_player import AIPlayer

class PongGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        # Paddle and ball positions
        self.ball = pygame.Rect(400, 300, 10, 10)
        self.paddle_ai = pygame.Rect(750, 250, 10, 100)

        # Ball speed
        self.ball_dx = 5
        self.ball_dy = 5

        # AI Player
        self.ai = AIPlayer(model_path="model.h5")

    def get_ai_state(self):
        return [
            self.ball.x / 800,
            self.ball.y / 600,
            self.ball_dx / 10,
            self.paddle_ai.y / 600
        ]

    def update_ai_paddle(self):
        action = self.ai.decide_action(self.get_ai_state())
        if action == 'up' and self.paddle_ai.top > 0:
            self.paddle_ai.y -= 5
        elif action == 'down' and self.paddle_ai.bottom < 600:
            self.paddle_ai.y += 5

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Move ball
            self.ball.x += self.ball_dx
            self.ball.y += self.ball_dy

            # Wall bounce
            if self.ball.top <= 0 or self.ball.bottom >= 600:
                self.ball_dy *= -1

            # Update AI paddle
            self.update_ai_paddle()

            # Draw
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (255, 255, 255), self.paddle_ai)
            pygame.draw.ellipse(self.screen, (255, 255, 255), self.ball)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    game = PongGame()
    game.run()