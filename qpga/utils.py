import keras
import numpy as np
import tensorflow as tf


def k_complex_from_real(x):
    return tf.stack([x, tf.zeros_like(x)], axis = 1)


def k_real(x):
    return x[:, 0, :]


def k_imag(x):
    return x[:, 1, :]


def k_conj(x):
    '''Conjugates a concatenated complex tensor'''
    return tf.stack([k_real(x), -1 * k_imag(x)], axis = 1)


def np_to_k_complex(x):
    return np.stack([np.real(x), np.imag(x)], axis = 1)


def k_to_tf_complex(x):
    return tf.complex(k_real(x), k_imag(x))


def tf_to_k_complex(x):
    return tf.stack([tf.real(x), tf.imag(x)], axis = 1)


def np_to_complex(x):
    return np.array(k_real(x) + 1j * k_imag(x), dtype = np.complex128)


def reshape_state_vector(state):
    dim = int(np.sqrt(len(state)))
    return np.reshape(state, (dim, dim))


class FrameWriterCallback(keras.callbacks.Callback):

    def __init__(self, input_state = None, target_state = None):
        super().__init__()
        self.input_state = input_state
        self.target_state = target_state
        self.predictions = []

    def on_batch_begin(self, batch, logs = None):
        self.predictions.append(self.model.predict(self.input_state))
