# GNU general public licence V3 and later.
# Import functions for TensorFlow/Keras models and related components.

import tensorflow as tf
import tensorflow.keras as keras
def import_model(model_path):
    return keras.models.load_model(model_path)
def import_weights(model, weights_path):
    model.load_weights(weights_path)
    return model
def import_optimizer(optimizer_path):
    with open(optimizer_path, 'rb') as f:
        optimizer = tf.keras.optimizers.deserialize(f.read())
    return optimizer
def import_loss(loss_path):
    with open(loss_path, 'rb') as f:
        loss = tf.keras.losses.deserialize(f.read())
    return loss
def import_metrics(metrics_path):
    with open(metrics_path, 'rb') as f:
        metrics = tf.keras.metrics.deserialize(f.read())
    return metrics
def import_callbacks(callbacks_path):
    with open(callbacks_path, 'rb') as f:
        callbacks = tf.keras.callbacks.deserialize(f.read())
    return callbacks
def import_dataset(dataset_path):
    dataset = tf.data.Dataset.load(dataset_path)
    return dataset
def import_config(config_path):
    with open(config_path, 'r') as f:
        config = f.read()
    return config
def import_preprocessing(preprocessing_path):
    with open(preprocessing_path, 'r') as f:
        preprocessing = f.read()
    return preprocessing
def import_custom_objects(custom_objects_path):
    with open(custom_objects_path, 'rb') as f:
        custom_objects = tf.keras.utils.deserialize_keras_object(f.read())
    return custom_objects
def import_training_history(history_path):
    with open(history_path, 'rb') as f:
        history = tf.keras.utils.deserialize_keras_object(f.read())
    return history
def import_evaluation_results(evaluation_path):
    with open(evaluation_path, 'rb') as f:
        evaluation_results = tf.keras.utils.deserialize_keras_object(f.read())
    return evaluation_results
def import_predictions(predictions_path):
    with open(predictions_path, 'rb') as f:
        predictions = tf.keras.utils.deserialize_keras_object(f.read())
    return predictions
def import_model_summary(model_path):
    model = import_model(model_path)
    model_summary = []
    model.summary(print_fn=lambda x: model_summary.append(x))
    return "\n".join(model_summary)         
def import_training_config(training_config_path):
    with open(training_config_path, 'r') as f:
        training_config = f.read()
    return training_config
def import_evaluation_config(evaluation_config_path):
    with open(evaluation_config_path, 'r') as f:
        evaluation_config = f.read()
    return evaluation_config
def import_prediction_config(prediction_config_path):
    with open(prediction_config_path, 'r') as f:
        prediction_config = f.read()
    return prediction_config
def import_model_architecture(model_architecture_path):
    with open(model_architecture_path, 'r') as f:
        model_architecture = f.read()
    return model_architecture
def import_training_data(training_data_path):
    training_data = tf.data.Dataset.load(training_data_path)
    return training_data
def import_validation_data(validation_data_path):
    validation_data = tf.data.Dataset.load(validation_data_path)
    return validation_data
def import_test_data(test_data_path):
    test_data = tf.data.Dataset.load(test_data_path)
    return test_data
def import_pretrained_model(pretrained_model_path):
    pretrained_model = keras.models.load_model(pretrained_model_path)
    return pretrained_model
def import_pretrained_weights(pretrained_model, pretrained_weights_path):
    pretrained_model.load_weights(pretrained_weights_path)
    return pretrained_model
def import_pretrained_optimizer(pretrained_optimizer_path):
    with open(pretrained_optimizer_path, 'rb') as f:
        pretrained_optimizer = tf.keras.optimizers.deserialize(f.read())
    return pretrained_optimizer
def import_pretrained_loss(pretrained_loss_path):
    with open(pretrained_loss_path, 'rb') as f:
        pretrained_loss = tf.keras.losses.deserialize(f.read())
    return pretrained_loss
def import_pretrained_metrics(pretrained_metrics_path):
    with open(pretrained_metrics_path, 'rb') as f:
        pretrained_metrics = tf.keras.metrics.deserialize(f.read())
    return pretrained_metrics
def import_pretrained_callbacks(pretrained_callbacks_path):
    with open(pretrained_callbacks_path, 'rb') as f:
        pretrained_callbacks = tf.keras.callbacks.deserialize(f.read())
    return pretrained_callbacks
def import_pretrained_dataset(pretrained_dataset_path):
    pretrained_dataset = tf.data.Dataset.load(pretrained_dataset_path)
    return pretrained_dataset
def import_pretrained_config(pretrained_config_path):
    with open(pretrained_config_path, 'r') as f:
        pretrained_config = f.read()
    return pretrained_config
def import_pretrained_preprocessing(pretrained_preprocessing_path):
    with open(pretrained_preprocessing_path, 'r') as f:
        pretrained_preprocessing = f.read()
    return pretrained_preprocessing
def import_pretrained_custom_objects(pretrained_custom_objects_path):
    with open(pretrained_custom_objects_path, 'rb') as f:
        pretrained_custom_objects = tf.keras.utils.deserialize_keras_object(f.read())
    return pretrained_custom_objects
def import_pretrained_training_history(pretrained_history_path):
    with open(pretrained_history_path, 'rb') as f:
        pretrained_history = tf.keras.utils.deserialize_keras_object(f.read())
    return pretrained_history
def import_pretrained_evaluation_results(pretrained_evaluation_path):
    with open(pretrained_evaluation_path, 'rb') as f:
        pretrained_evaluation_results = tf.keras.utils.deserialize_keras_object(f.read())
    return pretrained_evaluation_results
def import_pretrained_predictions(pretrained_predictions_path):
    with open(pretrained_predictions_path, 'rb') as f:
        pretrained_predictions = tf.keras.utils.deserialize_keras_object(f.read())
    return pretrained_predictions
def import_pretrained_model_summary(pretrained_model_path):
    pretrained_model = import_pretrained_model(pretrained_model_path)
    pretrained_model_summary = []
    pretrained_model.summary(print_fn=lambda x: pretrained_model_summary.append(x))
    return "\n".join(pretrained_model_summary)
def import_pretrained_training_config(pretrained_training_config_path):
    with open(pretrained_training_config_path, 'r') as f:
        pretrained_training_config = f.read()
    return pretrained_training_config
def import_pretrained_evaluation_config(pretrained_evaluation_config_path):
    with open(pretrained_evaluation_config_path, 'r') as f:
        pretrained_evaluation_config = f.read()
    return pretrained_evaluation_config
def import_pretrained_prediction_config(pretrained_prediction_config_path):
    with open(pretrained_prediction_config_path, 'r') as f:
        pretrained_prediction_config = f.read()
    return pretrained_prediction_config
def import_pretrained_model_architecture(pretrained_model_architecture_path):
    with open(pretrained_model_architecture_path, 'r') as f:
        pretrained_model_architecture = f.read()
    return pretrained_model_architecture
def import_pretrained_training_data(pretrained_training_data_path):
    pretrained_training_data = tf.data.Dataset.load(pretrained_training_data_path)
    return pretrained_training_data
def import_pretrained_validation_data(pretrained_validation_data_path):
    pretrained_validation_data = tf.data.Dataset.load(pretrained_validation_data_path)
    return pretrained_validation_data
def import_pretrained_test_data(pretrained_test_data_path):
    pretrained_test_data = tf.data.Dataset.load(pretrained_test_data_path)
    return pretrained_test_data
def import_pretrained_model_weights(pretrained_model, pretrained_weights_path):
    pretrained_model.load_weights(pretrained_weights_path)
    return pretrained_model
def import_pretrained_model_optimizer(pretrained_model, pretrained_optimizer_path):
    with open(pretrained_optimizer_path, 'rb') as f:
        pretrained_optimizer = tf.keras.optimizers.deserialize(f.read())
    pretrained_model.compile(optimizer=pretrained_optimizer)
    return pretrained_model
def import_pretrained_model_loss(pretrained_model, pretrained_loss_path):
    with open(pretrained_loss_path, 'rb') as f:
        pretrained_loss = tf.keras.losses.deserialize(f.read())
    pretrained_model.compile(loss=pretrained_loss)
    return pretrained_model
def import_pretrained_model_metrics(pretrained_model, pretrained_metrics_path):
    with open(pretrained_metrics_path, 'rb') as f:
        pretrained_metrics = tf.keras.metrics.deserialize(f.read())
    pretrained_model.compile(metrics=pretrained_metrics)
    return pretrained_model
def import_pretrained_model_callbacks(pretrained_model, pretrained_callbacks_path):
    with open(pretrained_callbacks_path, 'rb') as f:
        pretrained_callbacks = tf.keras.callbacks.deserialize(f.read())
    pretrained_model.callbacks = pretrained_callbacks
    return pretrained_model
def import_pretrained_model_dataset(pretrained_model, pretrained_dataset_path):
    pretrained_dataset = tf.data.Dataset.load(pretrained_dataset_path)
    pretrained_model.fit(pretrained_dataset)
    return pretrained_model
def import_pretrained_model_config(pretrained_model, pretrained_config_path):
    with open(pretrained_config_path, 'r') as f:
        pretrained_config = f.read()
    pretrained_model.config = pretrained_config
    return pretrained_model
def import_pretrained_model_preprocessing(pretrained_model, pretrained_preprocessing_path):
    with open(pretrained_preprocessing_path, 'r') as f:
        pretrained_preprocessing = f.read()
    pretrained_model.preprocessing = pretrained_preprocessing
    return pretrained_model
def import_pretrained_model_custom_objects(pretrained_model, pretrained_custom_objects_path):
    with open(pretrained_custom_objects_path, 'rb') as f:
        pretrained_custom_objects = tf.keras.utils.deserialize_keras_object(f.read())
    pretrained_model.custom_objects = pretrained_custom_objects
    return pretrained_model