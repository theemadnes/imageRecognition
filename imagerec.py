from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 

i = Image.open('images/numbers/0.1.png')

# iar = image array
iar = np.asarray(i) # 3 dimensional array
print iar

'''
Each row appears as:
[[  0   0   0 255]
 [255 255 255 255]
 [255 255 255 255]
 [255 255 255 255]
 [255 255 255 255]
 [255 255 255 255]
 [255 255 255 255]
 [255 255 255 255]]
 each line is a pixel
 item 0 = red
 item 1 = green
 item 2 = blue
 item 3 = alpha (transparency)
'''

plt.imshow(iar)
plt.show()