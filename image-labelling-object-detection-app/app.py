import streamlit as st

st.set_page_config(page_title="YOLOFlow", layout="wide")

# Set background color using markdown & HTML
st.markdown(
    """
   <style>
    .main {
        background-color: #f9fafc;
        padding: 2rem;
        font-family: "Segoe UI", sans-serif;
    }
    .yoloflow-header {
        background: linear-gradient(to right, #24292e, #0e76a8);
        padding: 2.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .yoloflow-header h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    .yoloflow-header p {
        font-size: 1.25rem;
        color: #d1d5db;
    }
    .features {
        font-size: 1.1rem;
        padding: 0 1rem;
        margin-bottom: 2rem;
    }

    /* Center ALL stButton widgets */
    .stButton {
        display: flex;
        justify-content: center !important;
        margin-top: 2rem;
    }

    .stButton>button {
        background-color: #0e76a8;
        color: white;
        font-size: 1.1rem;
        padding: 0.6rem 1.5rem;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #095a85;
    }
</style>
    """,
    unsafe_allow_html=True
)

# App state
if "started" not in st.session_state:
    st.session_state.started = False

# Landing page
if not st.session_state.started:
    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.markdown("""
    <div class="yoloflow-header">
        <h1>YOLOFlow Customizer</h1>
        <p>Welcome to YOLOFlow — Your end-to-end pipeline for training custom object detection models with YOLO.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="features">
        This tool helps you:
        <ul>
            <li>📥 <strong>Generate bulk images</strong> by class</li>
            <li>🏷️ <strong>Auto-label</strong> them using pretrained YOLO</li>
            <li>✅ <strong>Validate</strong> label outputs</li>
            <li>🔀 <strong>Split</strong> into train/val sets</li>
            <li>📄 <strong>Auto-generate</strong> <code>data.yaml</code></li>
            <li>🧪 <strong>Train and test</strong> your own model</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # ✅ Centered Button Container
    st.markdown('<div class="start-button-center">', unsafe_allow_html=True)
    if st.button("🚀 Get Started"):
        st.session_state.started = True
        st.switch_page("pages/1_Generate_Bulk_Images.py")
    st.markdown('</div>', unsafe_allow_html=True)
