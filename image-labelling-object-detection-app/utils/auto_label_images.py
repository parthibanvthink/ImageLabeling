import os
import cv2
from ultralytics import YOLO
from PIL import Image

model = YOLO("yolov8n.pt")

image_dir = "dataset/images/train"
label_dir = "dataset/labels/train"
os.makedirs(label_dir, exist_ok=True)

def clean_dataset(directory):
    """
    Removes unreadable or corrupted images from the dataset.
    """
    removed = 0
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                img = cv2.imread(path)
                if img is None:
                    os.remove(path)
                    print(f"🧹 Removed invalid image: {path}")
                    removed += 1
    return removed

def label_image(img_path, label_output_dir):
    filename = os.path.basename(img_path)
    try:
        results = model.predict(source=img_path, save=False, conf=0.25, verbose=False)
    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")
        return f"❌ Failed to process: {filename}"

    for result in results:
        if len(result.boxes) == 0:
            print(f"⚠️ No detections for {filename}, skipping label.")
            return f"⚠️ No detection: {filename}"

        os.makedirs(label_output_dir, exist_ok=True)
        label_path = os.path.join(label_output_dir, os.path.splitext(filename)[0] + ".txt")

        with open(label_path, "w") as f:
            for box in result.boxes:
                cls = int(box.cls[0])
                x_center, y_center, width, height = box.xywh[0]
                x_center /= result.orig_shape[1]
                y_center /= result.orig_shape[0]
                width /= result.orig_shape[1]
                height /= result.orig_shape[0]
                f.write(f"{cls} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
        print(f"✅ Labeled: {filename}")
        return f"✅ Labeled: {filename}"

def run_auto_labeling():
    logs = []

    # ✅ Clean up unreadable/corrupted images first
    removed_count = clean_dataset(image_dir)
    logs.append(f"🧹 Removed {removed_count} unreadable/corrupt images.")

    # ✅ Start labeling
    for entry in os.listdir(image_dir):
        full_path = os.path.join(image_dir, entry)

        if os.path.isdir(full_path):
            for img_file in os.listdir(full_path):
                if img_file.lower().endswith((".jpg", ".jpeg", ".png")):
                    img_path = os.path.join(full_path, img_file)
                    label_subdir = os.path.join(label_dir, entry)
                    log = label_image(img_path, label_subdir)
                    if log:
                        logs.append(log)
        elif entry.lower().endswith((".jpg", ".jpeg", ".png")):
            log = label_image(full_path, label_dir)
            if log:
                logs.append(log)

    return logs
