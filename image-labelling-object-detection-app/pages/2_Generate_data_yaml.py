# pages/2_Generate_data_yaml.py

import streamlit as st
from utils.generate_data_yaml import generate_data_yaml

st.set_page_config(page_title="Generate data.yaml", layout="wide")

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
        .code-block {
            background: #f0f0f0;
            padding: 1rem;
            border-radius: 8px;
            font-family: monospace;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="section-title">📄 Generate data.yaml</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">This will auto-create your YOLO training config file from the folder structure of your training dataset.</div>', unsafe_allow_html=True)

if st.button("Generate YAML"):
    yaml_path, content_text = generate_data_yaml()

    st.success(f"✅ `data.yaml` created successfully at `{yaml_path}`")

    st.markdown("### 📝 Preview:")
    st.markdown('<div class="code-block">', unsafe_allow_html=True)
    st.code(content_text, language="yaml")
    st.markdown("</div>", unsafe_allow_html=True)
