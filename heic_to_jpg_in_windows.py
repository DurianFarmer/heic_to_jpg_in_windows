from PIL import Image
import pillow_heif
import os

pillow_heif.register_heif_opener() # to open heif files in Windows

# Get list of HEIF and HEIC files in directory
directory = 'old'
new_directory = 'new'
files = [f for f in os.listdir(directory) if f.endswith('.heic') or f.endswith('.heif')]

# Convert each file to JPEG
for filename in files:
    image = Image.open(os.path.join(directory, filename))    
    image.convert('RGB').save(os.path.join(new_directory, os.path.splitext(filename)[0] + '.jpg'))