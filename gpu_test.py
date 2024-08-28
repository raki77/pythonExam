import tensorflow as tf

# GPU 장치 목록 확인
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("GPUs found:")
    for gpu in gpus: 
        print(gpu)
else:
    print("No GPUs found. Check your installation.")