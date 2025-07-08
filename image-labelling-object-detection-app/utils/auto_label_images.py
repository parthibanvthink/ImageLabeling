import os
from ultralytics import YOLO
import yaml
from PIL import Image

# # Load model
# model = YOLO("yolov8n.pt")

# New (higher accuracy)
model = YOLO("yolov8x.pt")


# Directories
image_dir = "dataset/images/train"
label_dir = "dataset/labels/train"
os.makedirs(label_dir, exist_ok=True)

# Load your class names from data.yaml
def load_custom_class_map(yaml_path="dataset/data.yaml"):
    if not os.path.exists(yaml_path):
        return {}
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)
    return {name: i for i, name in enumerate(data.get("names", []))}

CUSTOM_CLASS_MAP = load_custom_class_map()
ALLOWED_CLASSES = set(CUSTOM_CLASS_MAP.keys())

def is_valid_image(path):
    try:
        img = Image.open(path)
        img.verify()  # Checks for corruption
        return True
    except Exception:
        return False

def label_image(img_path, label_output_dir):
    filename = os.path.basename(img_path)

    # 🔒 Check if image is valid before proceeding
    if not is_valid_image(img_path):
        print(f"⚠️ Skipped invalid or unreadable image: {filename}")
        return

    # Run prediction
    results = model.predict(source=img_path, save=False, conf=0.15, verbose=False)

    for result in results:
        if len(result.boxes) == 0:
            print(f"⚠️ No detections for {filename}, skipping label.")
            return

        os.makedirs(label_output_dir, exist_ok=True)
        label_path = os.path.join(label_output_dir, os.path.splitext(filename)[0] + ".txt")

        with open(label_path, "w") as f:
            for box in result.boxes:
                class_name = model.names[int(box.cls[0])]
                if class_name not in ALLOWED_CLASSES:
                    continue
                cls_id = CUSTOM_CLASS_MAP[class_name]

                x_center, y_center, width, height = box.xywh[0]
                x_center /= result.orig_shape[1]
                y_center /= result.orig_shape[0]
                width /= result.orig_shape[1]
                height /= result.orig_shape[0]

                f.write(f"{cls_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
        print(f"✅ Labeled: {filename}")

def run_auto_labeling():
    logs = []
    for entry in os.listdir(image_dir):
        full_path = os.path.join(image_dir, entry)

        if os.path.isdir(full_path):
            for img_file in os.listdir(full_path):
                if img_file.lower().endswith((".jpg", ".jpeg", ".png")):
                    img_path = os.path.join(full_path, img_file)
                    label_subdir = os.path.join(label_dir, entry)
                    label_image(img_path, label_subdir)
                    logs.append(f"Labeled: {img_file}")
        elif entry.lower().endswith((".jpg", ".jpeg", ".png")):
            label_image(full_path, label_dir)
            logs.append(f"Labeled: {entry}")

    return logs
