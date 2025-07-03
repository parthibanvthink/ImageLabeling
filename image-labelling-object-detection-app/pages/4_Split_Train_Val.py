# pages/4_Split_Train_Val.py

import streamlit as st
from utils.split_train_val_preserve_structure import split_dataset

st.set_page_config(page_title="Split Train/Val", layout="wide")

# Style
st.markdown("""
    <style>
        .section-title {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color: #0e76a8;
        }
        .desc {
            font-size: 1.1rem;
            color: #444;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# UI Layout
st.markdown('<div class="section-title">🔀 Split into Train and Val</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Split your dataset while keeping folder structures for class-wise organization.</div>', unsafe_allow_html=True)

# Inputs
val_ratio = st.slider("Validation set percentage", 5, 50, 20, step=5)

image_dir = "dataset/images/train"
label_dir = "dataset/labels/train"

# Split trigger
if st.button("Run Train/Val Split"):
    with st.spinner(f"Splitting dataset with {val_ratio}% for validation..."):
        split_dataset(image_dir, label_dir, val_ratio / 100)
    st.success(f"✅ Train/Val split complete! {val_ratio}% moved to validation set.")
