
#########################################################################
# Convolutional Neural Network - Image Search Engine
#########################################################################


###########################################################################################
# import packages
###########################################################################################

from tensorflow.keras.models import Model, load_model
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from os import listdir
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import pickle

###########################################################################################
# bring in pre-trained model (excluding top)
###########################################################################################

# image parameters

img_width = 224
img_height = 224
num_channels = 3

# network architecture

vgg = VGG16(input_shape = (img_width, img_height, num_channels), include_top = False, pooling = 'avg')

model = Model(inputs = vgg.input, outputs = vgg.layers[-1].output)

# save model file

model.save('models/vgg16_search_engine.h5')


###########################################################################################
# preprocessing & featurising functions
###########################################################################################

# image pre-processing function

def preprocess_image(filepath):
    
    image = load_img(filepath, target_size = (img_width, img_height))
    image = img_to_array(image)
    image = np.expand_dims(image, axis = 0)
    image = preprocess_input(image)
    
    return image

# featurise image

def featurise_image(image):
    
    feature_vector = model.predict(image)
    
    return feature_vector

###########################################################################################
# featurise base images
###########################################################################################

# source directory for base images

source_dir = 'data/'

# empty objects to append to

filename_store = []
feature_vector_store = np.empty((0,512))

# pass in & featurise base image set

for image in listdir(source_dir):
    
    print(image)
    
    # append image filename for future lookup
    filename_store.append(source_dir + image)
    
    # preprocess the image
    preprocessed_image = preprocess_image(source_dir + image)
    
    # extract the feature vector
    feature_vector = featurise_image(preprocessed_image)
    
    # append feature vector for similarity calculations
    feature_vector_store = np.append(feature_vector_store, feature_vector, axis = 0)

# save key objects for future use

pickle.dump(filename_store, open('models/filename_store.p', 'wb'))
pickle.dump(feature_vector_store, open('models/feature_vector_store.p', 'wb'))

        
###########################################################################################
# pass in new image, and return similar images
###########################################################################################

# load in required objects

model = load_model('models/vgg16_search_engine.h5', compile = False)

filename_store = pickle.load(open('models/filename_store.p', 'rb'))
feature_vector_store = pickle.load(open('models/feature_vector_store.p', 'rb'))

# search parameters

search_results_n = 8
search_image = 'search_image_02.jpg'
        
# preprocess & featurise search image

preprocessed_image = preprocess_image(search_image)
search_feature_vector = featurise_image(preprocessed_image)
        
# instantiate nearest neighbours logic

image_neighbours = NearestNeighbors(n_neighbors = search_results_n, metric = 'cosine')

# apply to our feature vector store

image_neighbours.fit(feature_vector_store)

# return search results for search image (distances & indices)

image_distances, image_indices = image_neighbours.kneighbors(search_feature_vector)

# convert closest image indices & distances to lists

image_indices = list(image_indices[0])
image_distances = list(image_distances[0])

# get list of filenames for search results

search_result_files = [filename_store[i] for i in image_indices]

# plot results

plt.figure(figsize=(12,9))
for counter, result_file in enumerate(search_result_files):    
    image = load_img(result_file)
    ax = plt.subplot(3, 3, counter+1)
    plt.imshow(image)
    plt.text(0, -5, round(image_distances[counter],3))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()





