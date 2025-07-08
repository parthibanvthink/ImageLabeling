# pages/3_Validate_Labels.py

import streamlit as st
import os
import glob
from utils.validate_labels import validate_labels

st.set_page_config(page_title="Validate Labels", layout="wide")

# Styling
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
        .error-box {
            font-family: monospace;
            font-size: 0.95rem;
            background-color: grey;
            padding: 1rem;
            border-left: 6px solid red;
            border-radius: 5px;
            margin-bottom: 1rem;
            max-height: 200px;
            overflow-y: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Title and desc
st.markdown('<div class="section-title">✅ Validate Labels</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Check for missing or empty label files in your training dataset to ensure integrity before splitting and training.</div>', unsafe_allow_html=True)

# Paths
image_dir = "dataset/images/train"
label_dir = "dataset/labels/train"

# Button to trigger validation
if st.button("Run Validation"):
    with st.spinner("Validating image-label consistency..."):
        result = validate_labels(image_dir, label_dir)

    st.success(f"Validation complete: {result['checked']} images scanned")

    if result["missing"]:
        st.error(f"❌ {len(result['missing'])} images are missing label files")
        st.markdown('<div class="error-box">' + "<br>".join(result["missing"]) + '</div>', unsafe_allow_html=True)

    if result["empty"]:
        st.warning(f"⚠️ {len(result['empty'])} label files are empty")
        st.markdown('<div class="error-box">' + "<br>".join(result["empty"]) + '</div>', unsafe_allow_html=True)

    if not result["missing"] and not result["empty"]:
        st.success("🎉 All image-label pairs are valid!")

# 📂 Optional: show checked folder info
st.caption("📂 Checked folder: `dataset/images/train` vs `dataset/labels/train`")

# ✅ Labeled image check for navigation
label_files = glob.glob(os.path.join(label_dir, "**/*.txt"), recursive=True)
valid_labeled_count = sum(1 for f in label_files if os.path.getsize(f) > 0)

if valid_labeled_count > 0:
    st.markdown("---")
    st.success(f"🔍 {valid_labeled_count} labeled images found.")
    if st.button("👁️ View Labeled Images"):
        st.switch_page("pages/6_View_Labeled_Images.py")
else:
    st.info("ℹ️ No labeled images with valid content found. Run Auto Labeling first.")
