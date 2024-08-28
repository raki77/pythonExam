import tensorflow as tf
import time


# 간단한 모델 정의 함수
def build_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(512, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model


# MNIST 데이터셋 로드
def load_data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train.reshape(-1, 784).astype('float32') / 255.0
    x_test = x_test.reshape(-1, 784).astype('float32') / 255.0
    return x_train, y_train, x_test, y_test


# 속도 테스트 함수
def test_device(device_name):
    print(f"Testing on {device_name}")

    # 장치 할당
    with tf.device(device_name):
        # 데이터 로드
        x_train, y_train, x_test, y_test = load_data()

        # 모델 빌드
        model = build_model()

        # 훈련 시간 측정
        start_time = time.time()
        model.fit(x_train, y_train, epochs=5, batch_size=128, verbose=2)
        end_time = time.time()

        # 훈련 시간 출력
        print(f"{device_name} training time: {end_time - start_time:.2f} seconds")


# CPU와 GPU에서 속도 테스트
if __name__ == "__main__":
    # CPU 속도 테스트
    test_device("/CPU:0")

    # GPU 속도 테스트 (만약 GPU가 없다면 자동으로 CPU로 돌아갑니다)
    if tf.config.list_physical_devices('GPU'):
        test_device("/GPU:0")
    else:
        print("No GPU found, skipping GPU test.")

