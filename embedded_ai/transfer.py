import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense,GlobalAveragePooling2D
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.applications.mobilenet import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model 

base_model = MobileNet(weights='imagenet',include_top=False) #imports the mobilenet model and discards the last 1000 neuron layer.
x=base_model.output
x=GlobalAveragePooling2D()(x)
x=Dense(1024,activation='relu')(x)
x=Dense(1024,activation='relu')(x)
x=Dense(512,activation='relu')(x)
preds=Dense(2,activation='softmax')(x)

model=Model(inputs=base_model.input,outputs=preds)

for layer in model.layers[:20]:
    layer.trainable=False
for layer in model.layers[20:]:
    layer.trainable=True
    
train_datagen=ImageDataGenerator(preprocessing_function=preprocess_input)
train_generator=train_datagen.flow_from_directory('/home/sihyeon/Downloads/PetImages/train',
    target_size=(128,128),
    color_mode='rgb',
    batch_size=32,
    class_mode='categorical', 
    shuffle=True)
    
model.compile(optimizer='Adam',loss='categorical_crossentropy',metrics=['accuracy'])
step_size_train = max(1, train_generator.n // train_generator.batch_size)
history = model.fit(train_generator, steps_per_epoch=step_size_train, epochs=5)


def show_training_results(history):
    """학습 이력과 최종 결과를 matplotlib 창으로 표시한다."""
    metrics = history.history
    final_accuracy = metrics['accuracy'][-1]
    final_loss = metrics['loss'][-1]

    figure, axes = plt.subplots(1, 2, figsize=(12, 5))
    figure.canvas.manager.set_window_title('MobileNet 학습 결과')
    figure.suptitle(
        f'학습 완료 | Epoch: {len(metrics["loss"])}    '
        f'정확도: {final_accuracy:.4f}    손실: {final_loss:.4f}',
        fontsize=14,
    )
    epochs = range(1, len(metrics['loss']) + 1)

    axes[0].plot(epochs, metrics['accuracy'], marker='o')
    axes[0].set_title('Training Accuracy')
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Accuracy')
    axes[0].grid(True)

    axes[1].plot(epochs, metrics['loss'], marker='o', color='tab:red')
    axes[1].set_title('Training Loss')
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('Loss')
    axes[1].grid(True)

    figure.tight_layout(rect=(0, 0, 1, 0.9))
    plt.show()


show_training_results(history)