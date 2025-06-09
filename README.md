README

Title: Pest Detection Using YOLOv8 and Faster R-CNN

This project benchmarks two powerful object detection models — YOLOv8 and Faster R-CNN — for pest detection. The dataset used is inspired by large-scale datasets like IP102, containing multiple pest species across various crop types.

Dataset Description:

We use a custom pest dataset with labeled images for classification and object detection tasks.

Contains over XX,XXX images across multiple pest categories

Includes bounding boxes for detection

Hierarchical labels (example: caterpillar -> maize pests)

Long-tailed data distribution typical of real-world field conditions

Download the dataset from:

Google Drive: [Insert Link]
Aliyun Drive (optional): [Insert Link]

Class names are listed in the file classes.txt.

Model 1: YOLOv8 (Ultralytics)

Architecture: CNN-based with C2f blocks
Detection: Anchor-free, decoupled classification and regression head

Advantages:

Real-time performance

Built-in evaluation metrics: mAP, IoU, confusion matrix

Easy export to ONNX, TensorFlow, and CoreML formats

Suitable for edge deployment

Installation:
pip install ultralytics

Training Example:
yolo detect train model=yolov8s.pt data=data.yaml epochs=50 imgsz=640

Export Model:
yolo export model=path/to/best.pt format=onnx

Model 2: Faster R-CNN (Detectron2)

Architecture: ResNet-50 with Feature Pyramid Network, Region Proposal Network (RPN), and RoIAlign

Advantages:

High accuracy, especially on small object detection

Strong bounding box refinement

Good for complex and dense pest images

Installation:

pip install torch torchvision torchaudio
pip install git+https://github.com/facebookresearch/detectron2.git

Dataset Registration:

from detectron2.data.datasets import register_coco_instances
register_coco_instances("pest_train", {}, "annotations/train.json", "images/train")

Training Command:

python train_net.py --config-file configs/COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml --num-gpus 1 OUTPUT_DIR ./output

Export Model (TorchScript):

torch.jit.save(torch.jit.trace(model, dummy_input), "faster_rcnn_model.pt"
