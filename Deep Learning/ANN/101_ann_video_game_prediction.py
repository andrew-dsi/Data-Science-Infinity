
#########################################################################
# Artificial Neural Network - Video Game Success Prediction
#########################################################################


#########################################################################
# Import Libraries
#########################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import ModelCheckpoint

#########################################################################
# Import Data
#########################################################################

# import data
data_for_model = pd.read_csv("data/ann-game-data.csv")

# drop any redundant columns
data_for_model.drop("player_id", axis = 1, inplace = True)


#########################################################################
# Split Input Variables & Output Variable
#########################################################################

X = data_for_model.drop(["success"], axis = 1)
y = data_for_model["success"]

#########################################################################
# Split out Training & Test sets
#########################################################################

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42, stratify = y)

#########################################################################
# Deal with Categorical Variables
#########################################################################

categorical_vars = ["clan"]

one_hot_encoder = OneHotEncoder(sparse=False, drop = "first")

X_train_encoded = one_hot_encoder.fit_transform(X_train[categorical_vars])
X_test_encoded = one_hot_encoder.transform(X_test[categorical_vars])

encoder_feature_names = one_hot_encoder.get_feature_names_out(categorical_vars)

X_train_encoded = pd.DataFrame(X_train_encoded, columns = encoder_feature_names)
X_train = pd.concat([X_train.reset_index(drop=True), X_train_encoded.reset_index(drop=True)], axis = 1)
X_train.drop(categorical_vars, axis = 1, inplace = True)

X_test_encoded = pd.DataFrame(X_test_encoded, columns = encoder_feature_names)
X_test = pd.concat([X_test.reset_index(drop=True), X_test_encoded.reset_index(drop=True)], axis = 1)
X_test.drop(categorical_vars, axis = 1, inplace = True)

#########################################################################
# Feature Scaling
#########################################################################

scale_norm = MinMaxScaler()
X_train = pd.DataFrame(scale_norm.fit_transform(X_train), columns = X_train.columns)
X_test = pd.DataFrame(scale_norm.transform(X_test), columns = X_test.columns)

#########################################################################
# Network Architecture
#########################################################################

# network architecture

model = Sequential()

model.add(Dense(units = 32, input_dim = X_train.shape[1]))
model.add(Activation('relu'))

model.add(Dense(units = 32))
model.add(Activation('relu'))

model.add(Dense(units = 1))
model.add(Activation('sigmoid'))

# compile network

model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# view network architecture

model.summary()

#########################################################################
# Train Our Network!
#########################################################################

# training parameters

num_epochs = 50
batch_size = 32
model_filename = 'models/video_game_ann.h5'

# callbacks

save_best_model = ModelCheckpoint(filepath = model_filename,
                                  monitor = 'val_accuracy',
                                  mode = 'max',
                                  verbose = 1,
                                  save_best_only = True)

# train the network

history = model.fit(x = X_train.values,
                    y = y_train,
                    validation_data = (X_test, y_test),
                    batch_size = batch_size,
                    epochs = num_epochs,
                    callbacks = [save_best_model])

#########################################################################
# Visualise Training & Validation Performance
#########################################################################

import matplotlib.pyplot as plt

# plot metrics by epoch
fig, ax = plt.subplots(2, 1, figsize=(15,15))
ax[0].set_title('Loss')
ax[0].plot(history.epoch, history.history["loss"], label="Training Loss")
ax[0].plot(history.epoch, history.history["val_loss"], label="Validation Loss")
ax[1].set_title('Accuracy')
ax[1].plot(history.epoch, history.history["accuracy"], label="Training Accuracy")
ax[1].plot(history.epoch, history.history["val_accuracy"], label="Validation Accuracy")
ax[0].legend()
ax[1].legend()
plt.show()

# get best epoch performance for validation accuracy
max(history.history['val_accuracy'])


#########################################################################
# Make Predictions On New Data
#########################################################################

# import packages

from tensorflow.keras.models import load_model

# load model

model = load_model(model_filename)

# create new data

list(X_train)

player_a = [[9, 30, 6, 11, 62, 0, 1]]
player_a = scale_norm.transform(player_a)

# make our prediction

prediction = model.predict(player_a)
print(prediction)



player_b = [[11, 27, 0, 9, 59, 0, 0]]
player_b = scale_norm.transform(player_b)

prediction = model.predict(player_b)
print(prediction)

prediction_class = (prediction >= 0.5) * 1
print(prediction_class)

















