import os
import shutil
import random

def split_dataset(image_dir, label_dir, val_ratio=0.2):
    image_train_dir = image_dir
    image_val_dir = image_dir.replace("train", "val")

    label_train_dir = label_dir
    label_val_dir = label_dir.replace("train", "val")

    # Clear val folders
    for dir_path in [image_val_dir, label_val_dir]:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
        os.makedirs(dir_path)

    for root, _, files in os.walk(image_train_dir):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                rel_path = os.path.relpath(os.path.join(root, file), image_train_dir)
                label_path = os.path.join(label_train_dir, os.path.splitext(rel_path)[0] + ".txt")
                
                # Skip if label missing
                if not os.path.exists(label_path):
                    continue

                if random.random() < val_ratio:
                    # Copy to val
                    target_img = os.path.join(image_val_dir, rel_path)
                    target_lbl = os.path.join(label_val_dir, os.path.splitext(rel_path)[0] + ".txt")
                    os.makedirs(os.path.dirname(target_img), exist_ok=True)
                    os.makedirs(os.path.dirname(target_lbl), exist_ok=True)
                    shutil.move(os.path.join(root, file), target_img)
                    shutil.move(label_path, target_lbl)
