from PIL import Image
import numpy as np
import os

def load_image(path):
    return Image.open(path)

# Basic Image Manipulations
# 1. Load an image using PIL, convert it to a NumPy array
image = load_image('download.jpg')
image_array = np.array(image)
print("Image Shape:", image_array.shape)

# Extract and display individual RGB channels
red_channel = image_array[:, :, 0]
green_channel = image_array[:, :, 1]
blue_channel = image_array[:, :, 2]

# Save channels as separate images
Image.fromarray(red_channel).save('red_channel.png')
Image.fromarray(green_channel).save('green_channel.png')
Image.fromarray(blue_channel).save('blue_channel.png')

# Create grayscale image
grayscale_image = np.mean(image_array, axis=2).astype(np.uint8)
Image.fromarray(grayscale_image).save('grayscale_image.png')

# Weighted Blending
image1 = np.array(load_image('image1.jpg'))
image2 = np.array(load_image('image2.jpg'))

for alpha in np.linspace(0, 1, 10):
    blended_image = (alpha * image1 + (1 - alpha) * image2).astype(np.uint8)
    Image.fromarray(blended_image).save(f'blended_{alpha:.2f}.png')

# Watermark Implementation
base_image = load_image('base_image.jpg')
watermark = load_image('watermark.png').resize(base_image.size)
base_array = np.array(base_image)
watermark_array = np.array(watermark)

alpha = 0.3
watermarked_image = (alpha * watermark_array + (1 - alpha) * base_array).astype(np.uint8)
Image.fromarray(watermarked_image).save('watermarked_image.png')

# Creative Art
landscape = load_image('landscape.jpg')
texture = load_image('texture.jpg').resize(landscape.size)
creative_image = (0.7 * np.array(landscape) + 0.3 * np.array(texture)).astype(np.uint8)
Image.fromarray(creative_image).save('creative_art.png')

# Data Augmentation
for i in range(10):
    alpha = np.random.rand()
    blended_image = (alpha * image1 + (1 - alpha) * image2).astype(np.uint8)
    Image.fromarray(blended_image).save(f'data_augmented_{i}.png')

# Brightness and Contrast Adjustments

def adjust_brightness(image_array, value):
    brightened_image = np.clip(image_array + value, 0, 255).astype(np.uint8)
    return brightened_image

brighter_image = adjust_brightness(image_array, 50)
darker_image = adjust_brightness(image_array, -50)
Image.fromarray(brighter_image).save('brighter_image.png')
Image.fromarray(darker_image).save('darker_image.png')

# Overlaying a Smaller Image
smaller_image = load_image('smaller_image.jpg').resize((100, 100))
smaller_array = np.array(smaller_image)
base_array[50:150, 50:150, :] = smaller_array
Image.fromarray(base_array).save('overlay_image.png')

# Tiling
height, width = image_array.shape[:2]
tiles = [
    image_array[0:height // 2, 0:width // 2],
    image_array[0:height // 2, width // 2:],
    image_array[height // 2:, 0:width // 2],
    image_array[height // 2:, width // 2:],
]

for i, tile in enumerate(tiles):
    Image.fromarray(tile).save(f'tile_{i}.png')

rearranged_image = np.block([
    [tiles[2], tiles[0]],
    [tiles[3], tiles[1]]
])
Image.fromarray(rearranged_image).save('rearranged_image.png')

# Noise Addition
noise = np.random.randint(0, 50, image_array.shape, dtype=np.uint8)
noisy_image = np.clip(image_array + noise, 0, 255).astype(np.uint8)
Image.fromarray(noisy_image).save('noisy_image.png')

# Geometric Transformations
# Flipping
horizontally_flipped = image_array[:, ::-1, :]
vertically_flipped = image_array[::-1, :, :]
Image.fromarray(horizontally_flipped).save('horizontally_flipped.png')
Image.fromarray(vertically_flipped).save('vertically_flipped.png')

# Rotations
rotated_90 = np.transpose(image_array, (1, 0, 2))[:, ::-1, :]
rotated_180 = image_array[::-1, ::-1, :]
Image.fromarray(rotated_90).save('rotated_90.png')
Image.fromarray(rotated_180).save('rotated_180.png')
