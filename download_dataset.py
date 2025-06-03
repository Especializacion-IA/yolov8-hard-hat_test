from roboflow import Roboflow
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('ROBOFLOW_API_KEY')
if not api_key:
    raise ValueError("ROBOFLOW_API_KEY not found in environment variables")

rf = Roboflow(api_key=api_key)
project = rf.workspace("iaespecializacion").project("hard_hat_detection-3onnc")
version = project.version(3)
dataset = version.download("yolov8")