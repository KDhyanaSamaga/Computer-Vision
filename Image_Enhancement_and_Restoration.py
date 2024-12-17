import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path, grayscale=True):
    """Load an image from the given path."""
    if grayscale:
        return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    else:
        return cv2.imread(image_path)

def point_processing(image):
    """Apply point processing techniques."""
    negative_image = 255 - image

    equalized_image = cv2.equalizeHist(image)

    return negative_image, equalized_image

def apply_filters(image):
    """Apply smoothing and sharpening filters."""
   
    mean_filter = cv2.blur(image, (5, 5))

    laplacian_sharpened = cv2.Laplacian(image, cv2.CV_64F)

    return mean_filter, laplacian_sharpened

def noise_reduction(image):
    """Apply noise reduction techniques."""
    denoised_image = cv2.medianBlur(image, 5)
    return denoised_image

def display_images(images, titles):
    """Display multiple images with their titles."""
    plt.figure(figsize=(10, 6))
    for i in range(len(images)):
        plt.subplot(1, len(images), i+1)
        if len(images[i].shape) == 3:  
            plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        else:  
            plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.tight_layout()
    plt.show()

def main_assignment_1(image_path):
    image = load_image(image_path)
    negative_image, equalized_image = point_processing(image)
    mean_filter, laplacian_sharpened = apply_filters(image)
    denoised_image = noise_reduction(image)

    images = [image, negative_image, equalized_image, mean_filter, laplacian_sharpened, denoised_image]
    titles = ["Original", "Negative", "Histogram Equalization", "Mean Filter", "Laplacian", "Denoised"]
    display_images(images, titles)

image_path = input("Enter the path of the grayscale image: ")
main_assignment_1(image_path)
