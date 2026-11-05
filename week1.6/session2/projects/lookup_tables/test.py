from lut import SharpeningPGMLookUpTable, LinearPGMLookUpTable
from image import Image

image = Image.read("../../images/coins.pgm")
sharpen = SharpeningPGMLookUpTable()
linear = LinearPGMLookUpTable()
sharpened_image = sharpen.apply(image)
flipped_image = linear.apply(image)
sharpened_image.write_pgm("sharpened_coin.pgm")
flipped_image.write_pgm("flipped_coin.pgm")