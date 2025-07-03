import os
import yaml

def generate_data_yaml(image_train_dir="dataset/images/train", yaml_path="dataset/data.yaml"):
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

    with open(yaml_path, "w") as f:
        yaml.dump(yaml_content, f, default_flow_style=False)

    return yaml_path, yaml_content
