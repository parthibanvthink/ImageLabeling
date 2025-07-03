import os

def validate_labels(image_dir, label_dir):
    missing_labels = []
    empty_labels = []
    checked = 0

    for root, _, files in os.walk(image_dir):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                checked += 1
                img_path = os.path.join(root, file)
                relative_path = os.path.relpath(img_path, image_dir)
                label_path = os.path.join(label_dir, os.path.splitext(relative_path)[0] + ".txt")

                if not os.path.exists(label_path):
                    missing_labels.append(relative_path)
                elif os.stat(label_path).st_size == 0:
                    empty_labels.append(relative_path)

    return {
        "checked": checked,
        "missing": missing_labels,
        "empty": empty_labels
    }
