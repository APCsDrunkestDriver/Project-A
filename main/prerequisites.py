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
        import tensorflow as tf
        from tensorflow import keras
        import numpy as np
        import h5py # if saving/loading models

        # Define the required versions of libraries
        self.tf = ">=2.0.0"
        self.tensorflow = ">=2.0.0"
        self.keras = ">=2.0.0"
        self.numpy = ">=1.16.0"
        self.h5py = ">=2.10.0"
        self.pandas = ">=0.24.0"
        self.scikit_learn = ">=0.20.0"
        self.matplotlib = ">=3.0.0"

    def import_model(self, model_path):
        return keras.models.load_model(model_path)

    def import_weights(self, model, weights_path):
        model.load_weights(weights_path)
        return model

    def import_optimizer(self, optimizer_path):
        with open(optimizer_path, 'rb') as f:
            optimizer = tf.keras.optimizers.deserialize(f.read())
        return optimizer

    def import_loss(self, loss_path):
        with open(loss_path, 'rb') as f:
            loss = tf.keras.losses.deserialize(f.read())
        return loss

    def import_metrics(self, metrics_path):
        with open(metrics_path, 'rb') as f:
            metrics = tf.keras.metrics.deserialize(f.read())
        return metrics

    def import_callbacks(self, callbacks_path):
        with open(callbacks_path, 'rb') as f:
            callbacks = tf.keras.callbacks.deserialize(f.read())
        return callbacks

    def import_dataset(self, dataset_path):
        return tf.data.Dataset.load(dataset_path)

    def import_config(self, config_path):
        with open(config_path, 'r') as f:
            return f.read()

    def import_preprocessing(self, preprocessing_path):
        with open(preprocessing_path, 'r') as f:
            return f.read()

    def import_custom_objects(self, path):
        with open(path, 'rb') as f:
            return tf.keras.utils.deserialize_keras_object(f.read())

    def import_training_history(self, path):
        with open(path, 'rb') as f:
            return tf.keras.utils.deserialize_keras_object(f.read())

    def import_evaluation_results(self, path):
        with open(path, 'rb') as f:
            return tf.keras.utils.deserialize_keras_object(f.read())

    def import_predictions(self, path):
        with open(path, 'rb') as f:
            return tf.keras.utils.deserialize_keras_object(f.read())

    def import_model_summary(self, model_path):
        model = self.import_model(model_path)
        model_summary = []
        model.summary(print_fn=lambda x: model_summary.append(x))
        return "\n".join(model_summary)

    def import_training_config(self, path):
        with open(path, 'r') as f:
            return f.read()

    def import_evaluation_config(self, path):
        with open(path, 'r') as f:
            return f.read()

    def import_prediction_config(self, path):
        with open(path, 'r') as f:
            return f.read()

    def import_model_architecture(self, path):
        with open(path, 'r') as f:
            return f.read()

    def import_training_data(self, path):
        return tf.data.Dataset.load(path)

    def import_validation_data(self, path):
        return tf.data.Dataset.load(path)

    def import_test_data(self, path):
        return tf.data.Dataset.load(path)

    # PRETRAINED VERSIONS

    def import_pretrained_model(self, path):
        return keras.models.load_model(path)

    def import_pretrained_weights(self, model, path):
        model.load_weights(path)
        return model

    def import_pretrained_optimizer(self, path):
        return self.import_optimizer(path)

    def import_pretrained_loss(self, path):
        return self.import_loss(path)

    def import_pretrained_metrics(self, path):
        return self.import_metrics(path)

    def import_pretrained_callbacks(self, path):
        return self.import_callbacks(path)

    def import_pretrained_dataset(self, path):
        return self.import_dataset(path)

    def import_pretrained_config(self, path):
        return self.import_config(path)

    def import_pretrained_preprocessing(self, path):
        return self.import_preprocessing(path)

    def import_pretrained_custom_objects(self, path):
        return self.import_custom_objects(path)

    def import_pretrained_training_history(self, path):
        return self.import_training_history(path)

    def import_pretrained_evaluation_results(self, path):
        return self.import_evaluation_results(path)

    def import_pretrained_predictions(self, path):
        return self.import_predictions(path)

    def import_pretrained_model_summary(self, path):
        return self.import_model_summary(path)

    def import_pretrained_training_config(self, path):
        return self.import_training_config(path)

    def import_pretrained_evaluation_config(self, path):
        return self.import_evaluation_config(path)

    def import_pretrained_prediction_config(self, path):
        return self.import_prediction_config(path)

    def import_pretrained_model_architecture(self, path):
        return self.import_model_architecture(path)

    def import_pretrained_training_data(self, path):
        return self.import_training_data(path)

    def import_pretrained_validation_data(self, path):
        return self.import_validation_data(path)

    def import_pretrained_test_data(self, path):
        return self.import_test_data(path)

    # ADVANCED: Modify pretrained model directly

    def apply_pretrained_model_weights(self, model, path):
        return self.import_pretrained_weights(model, path)

    def apply_pretrained_model_optimizer(self, model, path):
        optimizer = self.import_pretrained_optimizer(path)
        model.compile(optimizer=optimizer)
        return model

    def apply_pretrained_model_loss(self, model, path):
        loss = self.import_pretrained_loss(path)
        model.compile(loss=loss)
        return model

    def apply_pretrained_model_metrics(self, model, path):
        metrics = self.import_pretrained_metrics(path)
        model.compile(metrics=metrics)
        return model

    def apply_pretrained_model_callbacks(self, model, path):
        callbacks = self.import_pretrained_callbacks(path)
        model.callbacks = callbacks
        return model

    def train_pretrained_model_with_dataset(self, model, dataset_path):
        dataset = self.import_pretrained_dataset(dataset_path)
        model.fit(dataset)
        return model

    def apply_pretrained_model_config(self, model, path):
        model.config = self.import_pretrained_config(path)
        return model

    def apply_pretrained_model_preprocessing(self, model, path):
        model.preprocessing = self.import_pretrained_preprocessing(path)
        return model

    def apply_pretrained_model_custom_objects(self, model, path):
        model.custom_objects = self.import_pretrained_custom_objects(path)
        return model
