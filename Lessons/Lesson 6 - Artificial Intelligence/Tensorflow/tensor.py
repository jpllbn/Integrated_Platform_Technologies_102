# import tensorflow as tf

# Check TensorFlow version
# print("TensorFlow version:", tf.__version__)

# Importing Libraries
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers import Activation, Dense
import numpy as np

# Define input data
x = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
              [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0], [1], [0], [0], [1]], dtype=float)

# Define the model
model = tf.keras.Sequential()
model.add(Dense(4, input_dim=3, activation='relu', use_bias=True))
model.add(Dense(4, activation='relu', use_bias=True))
model.add(Dense(1, activation='sigmoid', use_bias=True))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print(model.get_weights())

# Train the model and capture the history
history = model.fit(x, y, epochs=2000, validation_data=(x,y))
model.summary()

# Saving and printing Loss and Accuracy History
loss_history = history.history["loss"]
numpy_loss_history = np.array(loss_history)
np.savetxt("loss_history.txt", numpy_loss_history, delimiter="\n")

accuracy_history = history.history["accuracy"]
numpy_accuracy_history = np.array(accuracy_history)
np.savetxt("accuracy_history.txt", numpy_accuracy_history, delimiter="\n")

print("Mean Accuracy:", np.mean(accuracy_history))

result = model.predict(x).round()
print(result)

