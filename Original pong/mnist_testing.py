import tensorflow as tf
print("TensorFlow version:", tf.__version__)

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test,y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential ([
    tf.keras.layers.Flatten(input_shape = (28,28)),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(12)
])


predictions = model(x_train[:1]).numpy()
predictions


tf.nn.softmax(predictions).numpy()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

loss_fn(y_train[:1], predictions).numpy()

model.compile(optimizer='adam',
    loss=loss_fn,
    metrics=['accuracy'])

tf.keras.mixed_precision.set_global_policy('float32')  # Force float32 precision


model.fit(x_train, y_train, epochs=5, batch_size=64)


model.evaluate(x_test, y_test, verbose=3)