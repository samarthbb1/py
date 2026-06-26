import numpy as np
import matplotlib.pyplot as plt

image_matrix=np.array([
    [10,50,250,150],
    [50,100,200,150],
    [10,150,50,250],
    [100,250,150,150],
])
plt.imshow(image_matrix,cmap='gray')
plt.title('grayscale image')
plt.show()