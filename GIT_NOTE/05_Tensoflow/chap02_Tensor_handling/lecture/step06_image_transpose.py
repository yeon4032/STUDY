'''
 image transpose
'''

import matplotlib.image as img
import matplotlib.pyplot as plt
import tensorflow as tf

filename = "C:\\ITWILL\\5_Tensoflow\\data/images/packt.jpeg"
input_image = img.imread(filename)

print('input dim = {}'.format(input_image.ndim)) # input dim = 3
print('input shape = {}'.format(input_image.shape)) 
# input shape = (80, 144, 3)

plt.imshow(input_image)
plt.show()

x = tf.Variable(input_image, name='x')

# (80, 144, 3) -> (144, 80, 3)
x_trans = tf.transpose(x, perm=[1,0,2]) # 축 위치 변경 


# image 축 변경 
print(x_trans.shape)  # (144, 80, 3) 
print(x_trans) # shape=(144, 80, 3), dtype=uint8)
    
plt.imshow(x_trans)
plt.show()


