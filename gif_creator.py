import imageio.v3 as iio
import numpy as np
from PIL import Image

filenames = ['cat1.jpg', 'cat2.jpg']
images = []

target_width = 400
target_height = 300

for filename in filenames:
    img = Image.open(filename)
    resized_img = img.resize((target_width, target_height))
    resized_img_np = np.array(resized_img)
    images.append(resized_img_np)

iio.imwrite('cat.gif', images, duration=500, loop=0)
