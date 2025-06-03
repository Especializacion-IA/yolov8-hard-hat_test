from ultralytics import YOLO

model = YOLO("yolov8x.pt")

model.train(data="hard_hat_detection-3/data.yaml", epochs=50, imgsz=640)