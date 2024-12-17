import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path, grayscale=True):
    """Load an image from the given path."""
    if grayscale:
        return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    else:
        return cv2.imread(image_path)

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

def segmentation(image):
    """Apply segmentation techniques."""
  
    _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)


    edges = cv2.Canny(image, 100, 200)

    return binary_image, edges

def morphological_processing(binary_image):
    """Apply morphological operations."""
    kernel = np.ones((5, 5), np.uint8)

    dilated_image = cv2.dilate(binary_image, kernel, iterations=1)
    eroded_image = cv2.erode(binary_image, kernel, iterations=1)

    return dilated_image, eroded_image

def color_processing(image_path):
    """Apply color processing techniques."""
    color_image = load_image(image_path, grayscale=False)

    hsv_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv_image, lower_red, upper_red)
    filtered_image = cv2.bitwise_and(color_image, color_image, mask=mask)

    return color_image, hsv_image, filtered_image

def main_assignment_2(image_path):
 
    grayscale_image = load_image(image_path)

    binary_image, edges = segmentation(grayscale_image)

    dilated_image, eroded_image = morphological_processing(binary_image)

    color_image, hsv_image, filtered_image = color_processing(image_path)

    images = [grayscale_image, binary_image, edges, dilated_image, eroded_image]
    titles = ["Original (Grayscale)", "Binary", "Edges", "Dilation", "Erosion"]
    display_images(images, titles)

    color_images = [color_image, hsv_image, filtered_image]
    color_titles = ["Original (Color)", "HSV Image", "Red Filtered"]
    display_images(color_images, color_titles)

if __name__ == "__main__":
    image_path = input("Enter the path of the image: ").strip()
    main_assignment_2(image_path)
