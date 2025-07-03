import streamlit as st
import os

# Set up page
st.set_page_config(page_title="Generate Bulk Images", layout="wide")

# Custom CSS for consistent UI
st.markdown("""
    <style>
        .main {
            background-color: #f9fafc;
            padding: 2rem;
            font-family: "Segoe UI", sans-serif;
        }
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
        .footer-note {
            font-size: 0.9rem;
            color: #999;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)

# Title and description
st.markdown('<div class="section-title">📸 Generate Bulk Images</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="desc">This step downloads images from Google based on your specified object class names.</div>',
    unsafe_allow_html=True
)

# Inputs
classes_input = st.text_input("Enter Class Names (comma-separated)", value="book, bottle, cell phone")
num_images = st.number_input("Images per class", min_value=10, max_value=1000, value=100)
download_btn = st.button("Download Images")

if download_btn:
    class_list = [cls.strip() for cls in classes_input.split(",") if cls.strip()]
    if not class_list:
        st.error("❌ Please enter at least one valid class name.")
    else:
        st.subheader("📥 Download Progress")
        progress_bar = st.progress(0)
        status = st.empty()

        total = len(class_list)
        for idx, obj_class in enumerate(class_list, 1):
            status.write(f"🔄 Downloading images for: **{obj_class}** ({idx}/{total})...")
            from utils.bulk_image_download import download_images
            download_images([obj_class], num_images)
            progress_bar.progress(idx / total)

        status.success("✅ All downloads completed!")

# Optional back navigation
if st.button("🔙 Back to Home"):
    st.session_state.started = False
    st.switch_page("app.py")

st.markdown('<div class="footer-note">Images will be saved to: <code>dataset/images/train/&lt;class_name&gt;</code></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
