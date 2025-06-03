from ultralytics import YOLO

# download YOLOv8 pretrained model
model = YOLO("yolov8x.pt")

# train the model with local dataset
model.train(data="hard_hat_detection-3/data.yaml", epochs=50, imgsz=640)