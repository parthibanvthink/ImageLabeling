import os

def rename_images(folder_path, prefix):
    files = sorted(os.listdir(folder_path))
    count = 1

    print(f"\n📂 Renaming files in: {folder_path}\n{'-'*40}")
    
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            ext = os.path.splitext(file)[1]
            new_name = f"{prefix}_{count:03d}{ext}"
            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_name)
            
            os.rename(old_path, new_path)
            print(f"✅ {file} → {new_name}")
            count += 1

# Paths
train_path = 'dataset/images/train'
val_path = 'dataset/images/val'

# Rename
rename_images(train_path, 'train')
rename_images(val_path, 'val')
