import yaml

def load_class_names_from_yaml(path="dataset/data.yaml"):
    try:
        with open(path, "r") as f:
            data = yaml.safe_load(f)
            names = data.get("names", [])
            if isinstance(names, list):
                return {i: name for i, name in enumerate(names)}
            return names
    except Exception as e:
        print(f"Error loading class names: {e}")
        return {}
