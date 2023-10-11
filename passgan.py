import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Read data from the passwords.txt file
data = []

with open('chunk_rockyou_1.txt', 'r', encoding='iso-8859-1') as file:
    for line in file:
        line = line.strip()
        data.append(line)

# Tokenize the password data
max_words = 10000  # Adjust as needed
tokenizer = Tokenizer(num_words=max_words, oov_token='<OOV>')
tokenizer.fit_on_texts(data)
sequences = tokenizer.texts_to_sequences(data)

# Pad the sequences to make them the same length
max_sequence_length = 20  # Choose an appropriate sequence length
padded_data = pad_sequences(sequences, maxlen=max_sequence_length)

# Create and train a password generation model
model = keras.Sequential([
    keras.layers.Embedding(input_dim=max_words, output_dim=16, input_length=max_sequence_length),
    keras.layers.LSTM(64, return_sequences=True),
    keras.layers.LSTM(64, return_sequences=True),
    keras.layers.TimeDistributed(keras.layers.Dense(max_words, activation='softmax'))
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

model.fit(padded_data, padded_data, epochs=10)

