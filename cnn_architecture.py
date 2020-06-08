#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
import os


# In[10]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras import optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# In[11]:


train_dir=r'C:\ProgramData\Anaconda3\jupyter_notebook\DATA1\TRAIN'
test_dir=r'C:\ProgramData\Anaconda3\jupyter_notebook\DATA1\TEST'
validation_dir=r'C:\ProgramData\Anaconda3\jupyter_notebook\DATA1\VALIDATION'


# In[12]:


train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size =(128,128),
        batch_size =20
        class_mode = 'categorical'
        classes = [ ]
        color_mode = 'grayscale')

validation_generator = test_datagen.flow_from_directory(
        validation_dir,
        target_size = (128,128)
        batch_size =20,
        class_mode ='categorical',
        classes = [ ],
        color_mode = 'grayscale')


# In[ ]:


model = keras.models.sequential
model.add(layers.conv2D(32(3,3), activation='relu',input_size=(128,128,1))
model.add(layers.maxpooling2D((2,2)))

model.add(layers.conv2D(64(3,3),activation='relu'))
model.add(layers.maxpooling2D((2,2)))

model.add(layers.conv2D(128(3,3),activation='relu'))
model.add(layers.maxpooling2D((2,2)))

model.add(layers.conv2D(128(3,3),activation='relu'))
model.add(layers.maxpooling2D((2,2)))

model.add(layers.flatten())

model.add(layers.dense(60,activation='relu'))
model.add(Droupout(0.20))
model.add(layers.dense(10,activation='softmax'))


# In[ ]:


model.summary()


# In[ ]:


model.compile(optimizer='sgd',loss = 'categorical_crossentropy',matrics =['acc'])


# In[ ]:


history = model.fit_generator(
    train_genarator,
    steps_per_epoch =50,
    epochs=10,
    validation_data = validation_generator.
    validation_steps = 25
)


# In[ ]:


pd.DataFrame(history.history).plot(figsize=(8,5))
plot.gird(True)
plot.gcs().set_ylim(0,1)
plot.show


# In[ ]:


model.save("model.h5")


# In[ ]:


from tensorflow.keras import backend as k
k.clear_session()
del model


# In[ ]:




