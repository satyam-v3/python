from PIL import Image, ImageEnhance, ImageFilter
import os

# Paths to the input and output directories
path = '' # Inputs folders
pathOut = '' # output folders

# Ensure the output directory exists
os.makedirs(pathOut, exist_ok=True)

# Process each image in the input directory
for filename in os.listdir(path):
    # Construct the full file path
    img_path = os.path.join(path, filename)

    # Open the image
    img = Image.open(img_path)

    # Apply a series of transformations
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    # Enhance the contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    # Construct the output file name
    clean_name = os.path.splitext(filename)[0]
    output_path = os.path.join(pathOut, f"{clean_name}_edited.jpg")

    # Save the edited image
    edit.save(output_path)
