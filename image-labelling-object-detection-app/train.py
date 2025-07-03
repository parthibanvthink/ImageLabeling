import argparse
from ultralytics import YOLO
import torch.serialization

# ✅ Register ALL required classes explicitly
from torch.nn.modules.container import Sequential
from ultralytics.nn.tasks import DetectionModel
from ultralytics.nn.modules import (
    Conv, Bottleneck, C2f, SPPF, DWConv, RepConv
)

torch.serialization.add_safe_globals([
    Sequential,
    DetectionModel,
    Conv,
    Bottleneck,
    C2f,
    SPPF,
    DWConv,
    RepConv,
])

# ✅ CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument('--img', type=int, default=416, help='Image size')
parser.add_argument('--batch', type=int, default=4, help='Batch size')
parser.add_argument('--epochs', type=int, default=30, help='Number of epochs')
parser.add_argument('--data', type=str, required=True, help='Path to data.yaml')
parser.add_argument('--weights', type=str, default='yolov5su.pt', help='YOLO weights')
parser.add_argument('--cache', action='store_true', help='Use cache')
args = parser.parse_args()

# ✅ Load YOLO model
model = YOLO(args.weights)

# ✅ Train model
model.train(
    data=args.data,
    epochs=args.epochs,
    imgsz=args.img,
    batch=args.batch,
    cache=args.cache
)
