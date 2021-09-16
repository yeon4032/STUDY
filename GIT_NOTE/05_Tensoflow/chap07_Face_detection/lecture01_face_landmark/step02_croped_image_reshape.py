# -*- coding: utf-8 -*-
"""
croped image reshape(150x150)

NameError: name 'fix' is not defined
"""

from glob import glob # (*.jpg)
from PIL import Image # image file read
from skimage import io # image save
import numpy as np

path = 'C:\\ITWILL\\5_Tensoflow\\workspace\\chap07_Face_detection\\lecture01_face_landmark'
fpath = path + "/croped_images"
print(fpath)

# croped image -> 150x150
def imgReshape() : 
    img_h = img_w = 150
    
    img_reshape = [] # image save 
    
    for file in glob(fpath + "/*.jpg") :
        img = Image.open(file) 
        
        # image 규격화 
        img = img.resize( (img_h, img_w) )
        # PIL -> numpy
        img_data = np.array(img)
        print(img_data.shape)
        
        img_reshape.append(img_data)
    
    return np.array(img_reshape) # list -> numpy
        
img_reshape = imgReshape()    

print(img_reshape.shape) # (5, 150, 150, 3) - (size, h, w, c)

# 전체 이미지 사이즈
size=img_reshape.shape[0]

# images show & save 
import matplotlib.pyplot as plt
from skimage import io # image save

for i in range(size): # 0 ~ size-1
    img=img_reshape[i]
    plt.imshow(img)
    plt.show()
    
    # image save
    io.imsave(fpath+"/croped"+ str(i+1) +"_resize"+".jpg",img)


    
    
    
    
    
    
    
    

