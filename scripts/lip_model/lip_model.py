import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam

# Paths
dataset_dir = r"C:\Users\Shashank Mahato\Desktop\DataHaemScan\lip_data"

# Data Augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    brightness_range=[0.8, 1.2],
    horizontal_flip=True,
    rotation_range=10,
    zoom_range=0.2,
    shear_range=0.1
)

val_datagen = ImageDataGenerator(rescale=1./255)

# Load datasets
train_data = train_datagen.flow_from_directory(
    os.path.join(dataset_dir, 'train'), target_size=(224, 224), batch_size=32, class_mode='binary'
)
val_data = val_datagen.flow_from_directory(
    os.path.join(dataset_dir, 'val'), target_size=(224, 224), batch_size=32, class_mode='binary'
)

# Load Pretrained
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze first 140 layers (to avoid overfitting)
for layer in base_model.layers[:140]:
    layer.trainable = False

# Custom Layers on Top
x = base_model.output
x = GlobalAveragePooling2D()(x)  # Reduces feature map size
x = Dense(256, activation='relu')(x)
x = BatchNormalization()(x)
x = Dropout(0.5)(x)  # Stronger dropout to reduce overfitting
x = Dense(128, activation='relu')(x)
x = BatchNormalization()(x)
x = Dropout(0.3)(x)
predictions = Dense(1, activation='sigmoid')(x)  # Binary classification

# Final Model
model = Model(inputs=base_model.input, outputs=predictions)

# Compile with Lower Learning Rate
model.compile(optimizer=Adam(learning_rate=1e-4), loss='binary_crossentropy', metrics=['accuracy'])

# Train Model
history = model.fit(train_data, validation_data=val_data, epochs=10)

# Save Model
model.save("lip_model.h5")

# Convert Model to TF Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save TF Lite Model
with open("lip_model.tflite", "wb") as f:
    f.write(tflite_model)

print("TF Lite model saved successfully!")
