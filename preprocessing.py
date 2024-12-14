import cv2
import numpy as np
from PIL import Image

# def preprocess_image2(image_path):
#     image = cv2.imread(image_path)
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
#     _, binary_image = cv2.threshold(blurred_image, 128, 255, cv2.THRESH_BINARY_INV)
#     resized_image = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)
#     normalized_image = resized_image / 16.0

#     # cv2.imshow("Original Image", image)
#     # cv2.imshow("Grayscale Image", gray_image)
#     # cv2.imshow("Binary Image", binary_image)
#     # # cv2.imshow("Resized Image", resized_image)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()

#     flattened_image = normalized_image.flatten().reshape(1, -1)
#     return flattened_image

# def preprocess_image3(image_path):
#     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#     resized_image = cv2.bitwise_not(cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA))
#     normalized_image = resized_image / 16.0
#     flattened_image = normalized_image.flatten().reshape(1, -1)
    
#     cv2.imshow("flattened_image", flattened_image)
#     cv2.imshow("normalized_image", normalized_image)
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    
#     # print(flattened_image.shape) 
    
#     return flattened_image

def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Image not found at path: {image_path}")
    resized_image = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)
    resized_image = cv2.bitwise_not(resized_image)
    normalized_image = resized_image / 16.0
    flattened_image = normalized_image.flatten().reshape(1, -1)
    
    # cv2.imshow("flattened_image", flattened_image)
    # cv2.imshow("normalized_image", normalized_image)
    # cv2.imshow("image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    return flattened_image

# image_path = "assets\handwritten_numbers.png"
# preprocessed_image = preprocess_image(image_path)
