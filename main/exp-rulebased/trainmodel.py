from prerequisites import Prerequisites
pr = Prerequisites()
tf = pr.tf
np = pr.np
keras = pr.keras

model = keras.models.Sequential([
    keras.layers.Input(shape=(4,)),  # Example: [ball_x, ball_y, ball_dx, paddle_y]
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(3, activation='softmax')  # [up, stay, down]
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# example input vector: [ball_x, ball_y, ball_dx, paddle_y]
state = np.array([[ball_x, ball_y, ball_dx, paddle_y]])
prediction = model.predict(state)
action = np.argmax(prediction)

# 0 = move up, 1 = stay, 2 = move down
if action == 0:
    paddle_y -= paddle_speed
elif action == 2:
    paddle_y += paddle_speed