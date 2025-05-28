from roboflow import Roboflow

rf = Roboflow(api_key="d7VSK4YxfjrKftXojiIN")
project = rf.workspace("iaespecializacion").project("hard_hat_detection-3onnc")
dataset = project.version(1).download("yolov8")

                