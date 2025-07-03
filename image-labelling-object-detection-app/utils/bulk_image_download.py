# import ssl
# # Disable SSL certificate verification globally
# ssl._create_default_https_context = ssl._create_unverified_context

# import os
# from icrawler.builtin import GoogleImageCrawler

# # Classes you want to generate images for (should match COCO classes for detection)
# COCO_CLASSES = [
#     "mobile phone", "pen"
# ]

# # Number of images per class
# IMAGES_PER_CLASS = 500

# # Output directory
# OUTPUT_ROOT = "dataset/images/train"

# os.makedirs(OUTPUT_ROOT, exist_ok=True)

# for obj_class in COCO_CLASSES:
#     class_folder = os.path.join(OUTPUT_ROOT, obj_class.replace(" ", "_"))
#     os.makedirs(class_folder, exist_ok=True)

#     print(f"🔄 Downloading images for: {obj_class}")
#     crawler = GoogleImageCrawler(storage={"root_dir": class_folder})
#     crawler.crawl(keyword=obj_class, max_num=IMAGES_PER_CLASS)
#     print(f"✅ Completed: {obj_class}")


import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import os
from icrawler.builtin import GoogleImageCrawler

def download_images(classes, images_per_class):
    """
    Downloads images for the specified object classes.

    Args:
        classes (list): List of object class names.
        images_per_class (int): Number of images to download per class.
    """
    OUTPUT_ROOT = "dataset/images/train"
    os.makedirs(OUTPUT_ROOT, exist_ok=True)

    for obj_class in classes:
        class_folder = os.path.join(OUTPUT_ROOT, obj_class.replace(" ", "_"))
        os.makedirs(class_folder, exist_ok=True)

        print(f"🔄 Downloading images for: {obj_class}")
        crawler = GoogleImageCrawler(storage={"root_dir": class_folder})
        crawler.crawl(keyword=obj_class, max_num=images_per_class)
        print(f"✅ Completed: {obj_class}")