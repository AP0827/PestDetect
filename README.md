# 🐛 Pest Detection using YOLOv8n 🚀

This project implements a lightweight and accurate **pest detection system** using **YOLOv8n** from Ultralytics. It benchmarks pest recognition across a **custom dataset** inspired by real-world agricultural pest distributions like IP102.

We aim to aid agricultural monitoring systems with **fast and reliable pest identification**, focusing on ease of deployment, real-time inference, and clarity in evaluation metrics like **mAP**, **IoU**, and **Confusion Matrix**.

---

## 📦 Dataset Description

- **Custom dataset** with labeled pest images (bounding boxes included)
- Directory structure:
- **Over 18,000+ images** (placeholder; replace with actual count)
- **Hierarchical pest labels** (e.g., `caterpillar` → `maize pest`)
- Long-tailed class distribution (realistic to field conditions)
- **Split using** `image_split.py` into `train`, `val`, `test`

📂 `classes.txt` contains the pest class names  
📂 Labels are in **YOLO format** (`.txt` files matching image names)

---

## 📈 Noteworthy Pest Classes with High Precision

✅ `Lycorma delicatula`  
✅ `Mole Cricket`  
✅ `Paddy Stem Maggot`  
✅ `Green Bug`  
✅ `Cerodonta denticornis`

---

## 🧠 Model: YOLOv8n (Ultralytics)

- 🔬 Architecture: CNN-based, with C2f blocks and decoupled heads  
- ⚡ Real-time performance suitable for embedded devices  
- 🔁 Anchor-free detection  
- 📊 Built-in evaluation: `mAP`, `IoU`, `Precision`, `Recall`, `Confusion Matrix`  
- 📦 Export to ONNX, TensorFlow, and CoreML supported

### 🛠️ Installation

```bash
pip install -r requirements.txt
Where requirements.txt includes:
ultralytics
opencv-python
matplotlib
numpy
scikit-learn
seaborn
### **📊 Evaluation & Metrics**
All evaluation metrics are automatically computed after training and stored under:
runs/detect/train/
  - results.png         # Training curves
  - confusion_matrix.png
  - F1_curve.png
  - PR_curve.png
To re-evaluate manually:
yolo val model=runs/detect/train/weights/best.pt data=data.yaml imgsz=640

🐞 High Precision Pest Detections
Some pest classes that achieved notably high precision in validation/testing:

  -  ✅ Lycorma delicatula
  -  ✅ Mole Cricket
  -  ✅ Paddy Stem Maggot
  -  ✅ Green Bug
  -  ✅ Cerodonta denticornis
These species had distinct visual features, leading to confident bounding boxes and low false positives.
