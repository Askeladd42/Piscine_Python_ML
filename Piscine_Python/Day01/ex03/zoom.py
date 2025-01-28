import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def main():
    """Main function to crop/zoom on an image."""
    try:
        # Load the image
        image_path = "animal.jpeg"
        image = ft_load(image_path)
        image_array = np.array(image)

        # Print image information
        print(f"The shape of image is: {image_array.shape}")
        print(image_array[:1])  # Print the first row of pixels

        # Crop the image
        cropped_image_array = image_array[:400, :400, :1]
        print(f"New shape after slicing: {cropped_image_array.shape}")
        print(cropped_image_array[:1])  # Print the first row of cropped pixels

        # Display the cropped image with scales on x and y axes
        plt.imshow(cropped_image_array.squeeze(), cmap='gray')
        plt.title('Cropped Image')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
