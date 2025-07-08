# detect.py
from ultralytics import YOLO

model = YOLO('runs/train/exp/weights/best.pt')
results = model('test_image.jpg')
results[0].show()
