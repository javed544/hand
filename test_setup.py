import cv2
import numpy as np
from PIL import Image

print("Libraries loaded successfully!")

black_image = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.imshow("Black Image", black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
