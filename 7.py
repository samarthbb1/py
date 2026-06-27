import numpy as np
branch1 = np.array([10, 20, 30, 40, 50, 60]) # Sales for 6 months
branch2 = np.array([15, 25, 35, 45, 55, 65])

# Join (Concatenate)
combined = np.concatenate((branch1, branch2))

# Split into 4 quarterly segments (Total 12 months)
quarters = np.split(combined, 4)

print(f"Combined Sales: {combined}")
print(f"Quarterly Split: {quarters}")
print(f"Total: {np.sum(combined)}, Avg: {np.mean(combined):.2f}")
print(f"Max: {np.max(combined)}, Min: {np.min(combined)}")



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
