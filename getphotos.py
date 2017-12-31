
# coding: utf-8

# In[1]:

import glob
import shutil
import os
from os import listdir
from PIL import Image as Pimage 


dst_dir = "C:/Users/nitesh/Documents/MLproject/convnet_input/photo500/"

    
def loadImages(path):
    count=0
    imagesList=listdir(path)
    for image in imagesList:
        count=count+1
        full_dir=path+image
        if(count<=500):
            shutil.copy(full_dir,dst_dir)
        else:
            break
    print(len(imagesList))        
            
loadImages("C:/Users/nitesh/Documents/MLproject/photos_full/")   


# In[ ]:



