# train_model.py
from prerequisites import Prerequisites
import numpy as np

# Initialize helper
pr = Prerequisites()
keras = pr.keras
np = pr.np

# Build the model
model = pr.build_simple_pong_model()

# Generate synthetic training data
# Inputs: [ball_x, ball_y, ball_dx, paddle_y]
X_train = []
y_train = []

for _ in range(5000):
    ball_x = np.random.rand()
    ball_y = np.random.rand()
    ball_dx = (np.random.rand() - 0.5) * 2
    paddle_y = np.random.rand()

    state = [ball_x, ball_y, ball_dx, paddle_y]

    # Simple rule: if ball is above paddle, move up; if below, move down; else stay
    if ball_y < paddle_y - 0.05:
        action = [1, 0, 0]  # up
    elif ball_y > paddle_y + 0.05:
        action = [0, 0, 1]  # down
    else:
        action = [0, 1, 0]  # stay

    X_train.append(state)
    y_train.append(action)

X_train = np.array(X_train)
y_train = np.array(y_train)

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Save the model
model.save("model.h5")
print("[INFO] Model trained and saved to model.h5")