# utils/generate_data_yaml.py

import os
import yaml

def generate_data_yaml(image_train_dir="dataset/images/train", yaml_path="dataset/data.yaml"):
    """
    Scans train image directory for subfolders (class names), writes data.yaml
    """

    # Extract class names from subfolder names
    class_names = sorted([
        d for d in os.listdir(image_train_dir)
        if os.path.isdir(os.path.join(image_train_dir, d))
    ])

    yaml_content = {
        "train": "dataset/images/train",
        "val": "dataset/images/val",
        "nc": len(class_names),
        "names": class_names
    }

    # Write to data.yaml
    with open(yaml_path, "w") as f:
        yaml.dump(yaml_content, f, default_flow_style=False)

    # Return both path and text content for UI display
    formatted_text = yaml.dump(yaml_content, sort_keys=False, default_flow_style=False)
    return yaml_path, formatted_text
