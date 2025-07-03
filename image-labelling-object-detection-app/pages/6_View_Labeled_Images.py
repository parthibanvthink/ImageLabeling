import streamlit as st
import os
import cv2
import random

CLASS_MAP = {
    0: "Book",
    1: "Bottle",
    2: "Phone"
}

st.set_page_config(page_title="Labeled Image Preview", layout="wide")

st.markdown("""
    <style>
        .section-title {
            font-size: 2.3rem;
            font-weight: 700;
            color: #0e76a8;
            margin-bottom: 1rem;
        }
        .note {
            font-size: 1rem;
            color: #555;
            margin-bottom: 1.5rem;
        }
        .img-caption {
            text-align: center;
            font-size: 0.85rem;
            color: #555;
            margin-top: 0.3rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">🔍 View Labeled Images</div>', unsafe_allow_html=True)
st.markdown('<div class="note">Preview your labeled training images with bounding boxes and class names.</div>', unsafe_allow_html=True)

image_dir = "dataset/images/train"
label_dir = "dataset/labels/train"

max_images = st.slider("How many images to preview?", 1, 50, 12)
columns_per_row = st.selectbox("Images per row", [2, 3, 4], index=2)


def load_labels(label_file):
    boxes = []
    with open(label_file, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 5:
                cls_id, x, y, w, h = map(float, parts)
                boxes.append((int(cls_id), x, y, w, h))
    return boxes


def collect_labeled_images():
    labeled = []
    for root, _, files in os.walk(image_dir):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                img_path = os.path.join(root, file)
                rel = os.path.relpath(img_path, image_dir)
                label_path = os.path.join(label_dir, os.path.splitext(rel)[0] + ".txt")
                if os.path.exists(label_path) and os.path.getsize(label_path) > 0:
                    labeled.append((img_path, label_path))
    return labeled


labeled_images = collect_labeled_images()

if not labeled_images:
    st.warning("⚠️ No labeled images found. Please run Auto Labeling first.")
else:
    st.success(f"✅ Found {len(labeled_images)} labeled images.")
    selected = random.sample(labeled_images, min(max_images, len(labeled_images)))

    with st.spinner("Loading labeled images..."):
        for i in range(0, len(selected), columns_per_row):
            row = st.columns(columns_per_row)
            for j, col in enumerate(row):
                if i + j >= len(selected):
                    break
                img_path, label_path = selected[i + j]
                image = cv2.imread(img_path)
                if image is None:
                    continue
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                h, w = image.shape[:2]
                for cls_id, x, y, bw, bh in load_labels(label_path):
                    x1 = int((x - bw / 2) * w)
                    y1 = int((y - bh / 2) * h)
                    x2 = int((x + bw / 2) * w)
                    y2 = int((y + bh / 2) * h)
                    label = CLASS_MAP.get(cls_id, f"Class {cls_id}")
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(image, label, (x1, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
                col.image(image, use_container_width=True, caption=os.path.basename(img_path))


