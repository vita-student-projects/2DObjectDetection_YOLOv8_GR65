import os
import random
import shutil

# Set the directory paths
image_dir = 'data_object_image_2/training/image_2'
label_dir = 'data_object_label_2/training/label_2'
train_dir = 'train'
val_dir = 'val'
test_dir = 'test'

# Set the fraction of data to use for training, validation, and test
train_frac = 0.7
val_frac = 0.2
test_frac = 0.1

# Create the output directories if they do not exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Iterate over the images and labels and randomly assign each to a set
for image_file in os.listdir(image_dir):
    if image_file.endswith('.png'):
        image_path = os.path.join(image_dir, image_file)
        label_path = os.path.join(label_dir, image_file.replace('.png', '.txt'))
        if not os.path.exists(label_path):
            continue
        
        rand_num = random.random()
        if rand_num < train_frac:
            output_dir = os.path.join(train_dir, 'images')
        elif rand_num < train_frac + val_frac:
            output_dir = os.path.join(val_dir, 'images')
        else:
            output_dir = os.path.join(test_dir, 'images')
        
        # Copy the image and label to the appropriate directory
        shutil.copy(image_path, os.path.join(output_dir, image_file))
        shutil.copy(label_path, os.path.join(output_dir.replace('images', 'labels'), image_file.replace('.png', '.txt')))
