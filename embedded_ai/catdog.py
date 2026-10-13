import numpy as np
import tensorflow as tf
from tensorflow.keras import models, layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

root_dir = '/home/sihyeon/Downloads/PetImages/'
train_dir = root_dir + 'train/'
test_dir = root_dir + 'test/'

model = models.Sequential()
model.add(layers.Input(shape=(128,128,3)))
model.add(layers.Conv2D(32,(3,3), activation='relu', input_shape=(128,128,3)))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(64,(3,3), activation='relu'))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(128,(3,3), activation='relu'))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Dropout(0.3))
model.add(layers.Flatten())
model.add(layers.Dense(units=256, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(units=1, activation='sigmoid'))
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 이미지 전처리
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)
test_datagen = ImageDataGenerator(rescale = 1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary')

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary',
    shuffle=False)

# 훈련
model_path = 'cat_dog_model.keras'
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_accuracy',
        patience=5,
        mode='max',
        restore_best_weights=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.5,
        patience=2,
        min_lr=1e-6
    ),
    tf.keras.callbacks.ModelCheckpoint(
        model_path,
        monitor='val_accuracy',
        mode='max',
        save_best_only=True
    )
]

history = model.fit(
    train_generator,
    epochs=30,
    validation_data=test_generator,
    callbacks=callbacks
)

# 가장 검증 정확도가 높았던 모델 저장
model.save(model_path)
print(f'saved model: {model_path}')

# 저장한 모델 다시 불러오기
loaded_model = tf.keras.models.load_model(model_path)
print(f'loaded model: {model_path}')


def show_test_predictions(model, generator, count_per_class=6):
    """고양이와 개 테스트 이미지를 각각 표시한다."""
    generator.reset()
    image_paths = generator.filepaths
    images = []
    labels = []

    index_to_class = {
        index: class_name
        for class_name, index in generator.class_indices.items()
    }
    class_to_index = generator.class_indices

    for image_path in image_paths:
        image = tf.keras.utils.load_img(image_path, target_size=(128, 128))
        images.append(tf.keras.utils.img_to_array(image) / 255.0)
        class_name = image_path.rsplit('/', 2)[-2]
        labels.append(class_to_index[class_name])

    images = np.array(images)
    labels = np.array(labels)
    predictions = model.predict(images, verbose=0).ravel()

    selected_indices = []
    for class_index in sorted(index_to_class):
        class_indices = np.where(labels == class_index)[0]
        selected_indices.extend(class_indices[:count_per_class])

    columns = count_per_class
    rows = len(index_to_class)

    plt.figure(figsize=(4 * columns, 4 * rows))

    for plot_index, index in enumerate(selected_indices):
        predicted_index = int(predictions[index] >= 0.5)
        actual_index = labels[index]
        predicted_class = index_to_class[predicted_index]
        actual_class = index_to_class[actual_index]
        title_color = 'green' if predicted_index == actual_index else 'red'

        plt.subplot(rows, columns, plot_index + 1)
        plt.imshow(images[index])
        plt.axis('off')
        plt.title(
            f'predicted: {predicted_class}\n'
            f'actual: {actual_class}\n'
            f'probability: {predictions[index]:.3f}',
            color=title_color
        )

    plt.tight_layout()
    plt.show()


# 다시 불러온 모델로 테스트 이미지 예측 확인
show_test_predictions(loaded_model, test_generator, count_per_class=6)

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()