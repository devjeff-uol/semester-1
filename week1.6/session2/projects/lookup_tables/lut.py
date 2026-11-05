import math
from image import Image

class PGMLookUpTable:
    """
    PGM image pixel value look up table
    """

    def __init__(self):
        lut = list(range(256))
        for i in lut:
            lut[i] = self._pixel_calculation(i) # pixel manipulation
        self.lut = lut

    def _pixel_calculation(self, value: int) -> int:
        raise NotImplementedError("Subclass of PGMLookUpTable must implement the _pixel_calculation method")

    def _apply(self, image: Image) -> Image:
        width = image.width
        height = image.height
        size = width * height
        for i in range(size):
            image[i] = self.lut[image[i]] # update the pixel values to maniplated ones

    def apply(self, image: Image) -> Image:
        if not isinstance(image, (Image)):
            raise TypeError("image must be an object of the Image class")

        new_image = image.copy()
        self._apply(new_image)
        return new_image

    def apply_in_place(self, image: Image) -> Image:
        if not isinstance(image, (Image)):
            raise TypeError("image must be an object of the Image class")
        
        self._apply(image)

class LinearPGMLookUpTable(PGMLookUpTable):
    def _pixel_calculation(self, value: int) -> int:
        return 255 - value

class SharpeningPGMLookUpTable(PGMLookUpTable):
    def _pixel_calculation(self, value: int) -> int:
        return round(255 * math.sqrt(value / 255))