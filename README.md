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

🧩 Dataset

A synthetic dataset of 5,000 images (256×256) containing randomly placed geometric objects.
Each label file includes bounding boxes and class indices for three object types.

| Class     | Count | Example |
| --------- | ----: | :-----: |
| Rectangle | 2,500 |    🟥   |
| Circle    | 1,500 |    🟠   |
| Triangle  | 1,000 |    🔺   |



📊 Results
| Metric             |                       Value |
| ------------------ | --------------------------: |
| **mAP@0.5**        |                        0.87 |
| **Precision**      |                        0.91 |
| **Recall**         |                        0.88 |
| **Inference Time** | 14 ms / image (on RTX 3060) |





[▶ Try Live Demo on Streamlit](https://object-detection-app.streamlit.app)

### Future Work
- Extend dataset to real-world photos
- Support multi-object detection and YOLOv8 comparison
- Add model quantization for mobile deployment

