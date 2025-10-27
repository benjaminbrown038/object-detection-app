# object-detection-app

# 🎯 Object Detection App

A simple web app using **YOLOv5** and **Streamlit** to perform real-time object detection on uploaded images.

## 🚀 Features
- Upload `.jpg`, `.jpeg`, or `.png` images
- Detect multiple object classes (COCO dataset)
- View annotated image + detection table (class names & confidence)
- Easy to run locally or deploy with Streamlit Cloud

## 🛠️ Setup

```bash
git clone https://github.com/<your-username>/object-detection-app.git
cd object-detection-app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
