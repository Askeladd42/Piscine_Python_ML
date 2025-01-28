import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load an image from a file and return it as a numpy array."""
    try:
        img = Image.open(path)
        if img.format not in ['JPEG', 'JPG']:
            raise ValueError(
                "Unsupported image format. "
                "Only JPG and JPEG are supported.")

        img = img.convert('RGB')
        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")
        print(img_array)

        return img_array
    except Exception as e:
        print(f"Error: {e}")
        return None
