from roboflow import Roboflow

rf = Roboflow(api_key="d7VSK4YxfjrKftXojiIN")
project = rf.workspace("iaespecializacion").project("hard_hat_detection-3onnc")
version = project.version(2)
dataset = version.download("yolov8")
                