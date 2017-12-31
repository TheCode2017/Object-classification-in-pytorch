

import glob
import shutil
import os
from os import listdir
from PIL import Image as Pimage 
import pandas as pd

#src_dir = "C:/Users/nitesh/Documents/MLproject/convnet_input/photo/"
#dst_dir = "C:/Users/nitesh/Documents/MLproject/convnet_input/photo500"

    
def loadImages(path):
    count=0
    imagesList=listdir(path)
    label1=pd.DataFrame([])
    label=pd.read_csv('C:/Users/nitesh/Documents/MLproject/outlatest.csv')
    label1=label1.append(label.loc[label['photoid'].isin(imagesList)])
    label1.to_csv('C:/Users/nitesh/Documents/MLproject/out500.csv',index=False)
    #for image in imagesList:
        #count=count+1
        #f#ull_dir=path+image
        #if(count<=499):
            #shutil.copy(full_dir,dst_dir)
        #else:
            #break
    print(len(imagesList))        
            
loadImages("C:/Users/nitesh/Documents/MLproject/convnet_input/photo500/")   











