# ai_player.py
from prerequisites import Prerequisites

class AIPlayer:
    
    pr = Prerequisites()
    model = pr.build_simple_pong_model()
    summary = pr.get_model_summary(model) # Get model summary as string

    print(summary)
    def __init__(self, model_path=None):
        pr = Prerequisites()
        self.tf = pr.tf
        self.keras = pr.keras
        self.np = pr.np

        if model_path:
            self.model = self.keras.models.load_model(model_path)
        else:
            self.model = self.build_model()

    def build_model(self):
        model = self.keras.models.Sequential([
            self.keras.layers.Input(shape=(4,)),  # [ball_x, ball_y, ball_dx, paddle_y]
            self.keras.layers.Dense(16, activation='relu'),
            self.keras.layers.Dense(3, activation='softmax')  # [up, stay, down]
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def decide_action(self, game_state):
        """
        Predicts the action based on the current game state.
        :param game_state: [ball_x, ball_y, ball_dx, paddle_y]
        :return: 'up', 'stay', or 'down'
        """
        state = self.np.array([game_state])
        prediction = self.model.predict(state, verbose=0)
        action = self.np.argmax(prediction[0])
        return ['up', 'stay', 'down'][action]