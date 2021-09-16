'''
문) image.jpg 이미지 파일을 대상으로 파랑색 우산 부분만 slice 하시오.
'''

import matplotlib.image as mp_image
import matplotlib.pyplot as plt 
import tensorflow as tf
filename = "C:\\ITWILL\\5_Tensoflow\\data/images/umbrella.jpg"
input_image = mp_image.imread(filename)
print(input_image) # 0~225

print('input dim =', input_image.ndim) #dimension->input dim = 3
print('input shape =', input_image.shape) #input shape = (432, 650, 3) -> (h,w,c)

# image 원본 출력 
plt.imshow(input_image)
plt.show() 

# image slice
cutted_image = tf.slice(input_image, [100,30,0], [332,530,-1])

# image slice 출력 
plt.imshow(cutted_image)
plt.show()

