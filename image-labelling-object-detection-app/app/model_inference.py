from flask import Flask, request, jsonify
from PIL import Image
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO('runs/train/exp/weights/best.pt')

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['image']
    image = Image.open(file.stream)
    results = model(image)
    detections = results[0].boxes.data.tolist()
    return jsonify({'detections': detections})

if __name__ == '__main__':
    app.run(debug=True)
