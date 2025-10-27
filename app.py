# app.py
import streamlit as st
from detect import load_model, detect_objects
from PIL import Image
import numpy as np

st.title("🎯 Object Detection App")
st.write("Upload an image and detect objects using a pretrained YOLOv5 model.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    st.write("Detecting objects...")

    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    model = load_model()
    annotated, detections = detect_objects(model, "temp.jpg")

    st.subheader("Detections:")
    st.dataframe(detections[['name', 'confidence']])

    st.image(annotated, caption="Detection Results", use_container_width=True)
