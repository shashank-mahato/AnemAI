import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Flatten, Dropout, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam

# Paths
dataset_dir = r"C:\Users\Shashank Mahato\Desktop\DataHaemScan\skin_data"

# Data Augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    brightness_range=[0.7, 1.3],  # Adjust brightness
    horizontal_flip=True,  # Flip images
    rotation_range=15,  # Rotate images
    zoom_range=0.1  # Slight zoom
)

val_datagen = ImageDataGenerator(rescale=1./255)

# Load Datasets
train_data = train_datagen.flow_from_directory(
    os.path.join(dataset_dir, 'train'), target_size=(224, 224), batch_size=32, class_mode='binary'
)
val_data = val_datagen.flow_from_directory(
    os.path.join(dataset_dir, 'val'), target_size=(224, 224), batch_size=32, class_mode='binary'
)

# Load Pretrained MobileNetV2 Model
base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224, 224, 3))

# Freeze Initial Layers
base_model.trainable = False  

# Build Model
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.3)(x)
x = Dense(128, activation='relu')(x)
x = Dropout(0.3)(x)
output_layer = Dense(1, activation='sigmoid')(x)

model = Model(inputs=base_model.input, outputs=output_layer)

# Compile Model
model.compile(optimizer=Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])

# Train Model
history = model.fit(train_data, validation_data=val_data, epochs=10)

# Save Model
model.save("skin_model.h5")

# Convert Model to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save TFLite Model
with open("skin_model.tflite", "wb") as f:
    f.write(tflite_model)

print("TFLite Model Saved Successfully!")
