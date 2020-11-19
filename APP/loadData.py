import numpy as np


INPUT_SIGNAL_TYPES = [
    "body_acc_x_",
    "body_acc_y_",
    "body_acc_z_",
    "body_gyro_x_",
    "body_gyro_y_",
    "body_gyro_z_",
    "total_acc_x_",
    "total_acc_y_",
    "total_acc_z_"
]

# Output classes to learn how to classify
LABELS = [
    "WALKING",
    "WALKING_UPSTAIRS",
    "WALKING_DOWNSTAIRS",
    "SITTING",
    "STANDING",
    "LAYING"
]


DATA_PATH = "testdata/"
DATASET_PATH = DATA_PATH + "UCI HAR Dataset/"
print("\n" + "Dataset is now located at: " + DATASET_PATH)

TRAIN = "train/"
TEST = "test/"


# Load "X" (the neural network's training and testing inputs)

def load_X(X_signals_paths):
    X_signals = []

    for signal_type_path in X_signals_paths:
        file = open(signal_type_path, 'r')
        # Read dataset from disk, dealing with text files' syntax
        X_signals.append(
            [np.array(serie, dtype=np.float32) for serie in [
                row.replace('  ', ' ').strip().split(' ') for row in file
            ]]
        )
        # print(X_signals[-1][0].shape)
        file.close()

    return np.transpose(np.array(X_signals), (1, 2, 0))


# 测试集和和训练集和里面3个加速度的3个方向文件列表

X_train_signals_paths = [
    DATASET_PATH + TRAIN + "Inertial Signals/" + signal + "train.txt" for signal in INPUT_SIGNAL_TYPES
]
X_test_signals_paths = [
    DATASET_PATH + TEST + "Inertial Signals/" + signal + "test.txt" for signal in INPUT_SIGNAL_TYPES
]

# Load "y" (the neural network's training and testing outputs)
def load_y(y_path):
    file = open(y_path, 'r')
    # Read dataset from disk, dealing with text file's syntax
    y_ = np.array(
        [elem for elem in [
            row.replace('  ', ' ').strip().split(' ') for row in file
        ]],
        dtype=np.int32
    )
    file.close()
    # Substract 1 to each output class for friendly 0-based indexing
    return y_ - 1


y_train_path = DATASET_PATH + TRAIN + "y_train.txt"
y_test_path = DATASET_PATH + TEST + "y_test.txt"


def load_data():
    x_train = load_X(X_train_signals_paths)
    x_test = load_X(X_test_signals_paths)
    y_train = load_y(y_train_path)
    y_test = load_y(y_test_path)

    return x_train,y_train,x_test,y_test





if __name__ == '__main__':
    y = load_data()[1]


# Input Data
#
# training_data_count = len(X_train)  # 7352 training series (with 50% overlap between each serie)
# test_data_count = len(X_test)  # 2947 testing series
# n_steps = len(X_train[0])  # 128 timesteps per series
# n_input = len(X_train[0][0])  # 9 input parameters per timestep
#
# print("Some useful info to get an insight on dataset's shape and normalisation:")
# print("(X shape, y shape, every X's mean, every X's standard deviation)")
# print(X_test.shape, y_test.shape, np.mean(X_test), np.std(X_test))
# print("The dataset is therefore properly normalised, as expected, but not yet one-hot encoded.")
# print('training_data_count:',X_train.shape)


