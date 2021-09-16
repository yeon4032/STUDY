'''
 image slice
'''

import matplotlib.image as img 
import matplotlib.pyplot as plt 
import tensorflow as tf

filename = "C:\\ITWILL\\5_Tensoflow\\data/images/packt.jpeg"
input_image = img.imread(filename)
type(input_image) # numpy.ndarray

print('input dim =', input_image.ndim) #dimension->input dim = 3
print('input shape =', input_image.shape) #shape->input shape = (80, 144, 3) -> (h,w,c)

# image 원본 출력 
plt.imshow(input_image)
plt.show() 

# image slice
img_slice = tf.slice(input_image, [15,0,0],[40,-1,-1])

print(img_slice.shape) 

# image slice 출력 
plt.imshow(img_slice)
plt.show()

