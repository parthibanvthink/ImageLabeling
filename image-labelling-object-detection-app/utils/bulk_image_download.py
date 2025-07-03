# # utils/bulk_image_download.py

import ssl
import os
import requests
import urllib3
from duckduckgo_search import DDGS

ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def download_images(classes, images_per_class):
    OUTPUT_ROOT = "dataset/images/train"
    os.makedirs(OUTPUT_ROOT, exist_ok=True)

    for obj_class in classes:
        class_folder = os.path.join(OUTPUT_ROOT, obj_class.replace(" ", "_"))
        os.makedirs(class_folder, exist_ok=True)

        print(f"🔄 Downloading images for: {obj_class}")
        with DDGS() as ddgs:
            results = ddgs.images(keywords=obj_class, max_results=images_per_class)
            for idx, result in enumerate(results):
                try:
                    image_url = result["image"]
                    image_data = requests.get(image_url, timeout=5, verify=False).content
                    file_path = os.path.join(class_folder, f"{obj_class.replace(' ', '_')}_{idx}.jpg")
                    with open(file_path, "wb") as f:
                        f.write(image_data)
                except Exception as e:
                    print(f"⚠️ Failed to download image {idx}: {e}")
        print(f"✅ Completed: {obj_class}")
