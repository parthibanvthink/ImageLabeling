# pages/2_Auto_Label_Images.py

import streamlit as st
from utils.auto_label_images import run_auto_labeling

st.set_page_config(page_title="Auto Label Images", layout="wide")

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
        .label-log {
            font-family: monospace;
            font-size: 0.95rem;
            background-color: grey;
            padding: 1rem;
            border-radius: 8px;
            max-height: 300px;
            overflow-y: scroll;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">🏷️ Auto Label Images</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">This step uses a pretrained YOLO model to automatically detect and label objects in your training dataset.</div>', unsafe_allow_html=True)

if st.button("Run Auto Labeling 🚀"):
    with st.spinner("Running YOLO model... this may take a moment depending on the number of images."):
        logs = run_auto_labeling()
    st.success("✅ Auto labeling complete.")
    
    st.markdown("#### 📝 Labeling Summary:")
    st.markdown('<div class="label-log">' + "<br>".join(logs) + '</div>', unsafe_allow_html=True)
