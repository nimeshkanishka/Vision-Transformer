import os
import shutil
from tqdm import tqdm

SOURCE_DIR = r"C:\Users\USER\Downloads\Oxford-IIIT-Pets"
DESTINATION_ROOT = r"D:\Datasets\Oxford-IIIT-Pets"

for file in tqdm(os.listdir(SOURCE_DIR)):
    # If the filename begins with lowercase, it is a dog
    # If the filename begins with uppercase, it is a cat
    category = "dog" if file[0].islower() else "cat"

    # Label will be <type>_<breed>
    # e.g. dog_yorkshire_terrier
    label = (f"{category}_" + "_".join(file.split("_")[:-1])).lower()

    # Make subfolder in destination folder for this class if it doesnt exist already
    destination_dir = os.path.join(DESTINATION_ROOT, label)
    os.makedirs(destination_dir, exist_ok=True)

    # Copy image to corresponding subfolder at destination
    shutil.copy(
        os.path.join(SOURCE_DIR, file),
        os.path.join(destination_dir, file)
    )