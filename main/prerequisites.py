# prerequisites.py
# GNU General Public License V3 and later.
# Import functions for TensorFlow/Keras models and related components

import tensorflow as tf
from tensorflow import keras
import numpy as np
import h5py

class Prerequisites:
    def __init__(self):
        self.tf = tf
        self.keras = keras
        self.np = np
        self.h5py = h5py

        # Library version requirements
        self.versions = {
            'tensorflow': '>=2.0.0',
            'keras': '>=2.0.0',
            'numpy': '>=1.16.0',
            'h5py': '>=2.10.0',
            'pandas': '>=0.24.0',
            'scikit-learn': '>=0.20.0',
            'matplotlib': '>=3.0.0'
        }

    # === Model I/O ===
    def load_model(self, model_path):
        return self.keras.models.load_model(model_path)

    def load_weights(self, model, weights_path):
        model.load_weights(weights_path)
        return model

    # === Dataset I/O ===
    def load_dataset(self, dataset_path):
        return self.tf.data.Dataset.load(dataset_path)

    # === Model summary as string ===
    def get_model_summary(self, model):
        summary_lines = []
        model.summary(print_fn=lambda x: summary_lines.append(x))
        return "\n".join(summary_lines)

    # === Optional: Save model utility ===
    def save_model(self, model, path):
        model.save(path)

    # === Optional: Build basic model ===
    def build_simple_pong_model(self):
        model = self.keras.Sequential([
            self.keras.layers.Input(shape=(4,)),  # [ball_x, ball_y, ball_dx, paddle_y]
            self.keras.layers.Dense(16, activation='relu'),
            self.keras.layers.Dense(3, activation='softmax')  # up, stay, down
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model