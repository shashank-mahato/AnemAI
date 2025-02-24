import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization

# Paths
dataset_dir = r"C:\Users\Shashank Mahato\Desktop\HaemScan\eye_data"

# Data Augmentation
train_datagen = ImageDataGenerator(rescale=1./255, brightness_range=[0.8, 1.2])
val_datagen = ImageDataGenerator(rescale=1./255)

# Load datasets
train_data = train_datagen.flow_from_directory(
    os.path.join(dataset_dir, 'train'), target_size=(224, 224), batch_size=32, class_mode='binary'
)
val_data = val_datagen.flow_from_directory(
    os.path.join(dataset_dir, 'val'), target_size=(224, 224), batch_size=32, class_mode='binary'
)

# Define Custom CNN Model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(224, 224, 3)),
    BatchNormalization(),
    MaxPooling2D(pool_size=(2,2)),

    Conv2D(64, (3,3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D(pool_size=(2,2)),

    Conv2D(128, (3,3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D(pool_size=(2,2)),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(1, activation='sigmoid')  # Binary classification: Anemic (1) or Nonanemic (0)
])

# Compile Model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train Model
history = model.fit(train_data, validation_data=val_data, epochs=10)

# Save Model
model.save("eye_model.h5")

# Convert to TF Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TF Lite model
tflite_model_path = "eye_model.tflite"
with open(tflite_model_path, 'wb') as f:
    f.write(tflite_model)

print(f"TF Lite Model saved at: {tflite_model_path}")
