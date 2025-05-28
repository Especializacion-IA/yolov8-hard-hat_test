# 🦺 YOLOv8 – Detección de Cascos de Seguridad

Proyecto para detectar personas **con casco** y **sin casco** en imágenes utilizando **YOLOv8**.

---

## 📦 Tecnologías utilizadas

- Python 3.10+  
- Ultralytics YOLOv8  
- OpenCV / Matplotlib  
- Pandas / Seaborn  
- Jupyter / VSCode  
- CUDA *(opcional, para entrenamiento más rápido)*

---

## 📁 Estructura del proyecto

```
YOLOv8_hard_hut/
├── dataset/              # Dataset en formato YOLO (images/labels)
├── runs/              # Resultados del entrenamiento/inferencia 
├── infer.py           # Script de inferencia
├── train.py           # Script de entrenamiento
├── README.md
└── requirements.txt
```

---

## 🚀 Cómo ejecutar el proyecto

### 1. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Entrenar el modelo

```bash
yolo detect train data=data.yaml model=yolov8m.pt epochs=50 imgsz=640
```

### 3. Ejecutar inferencia

```bash
python infer.py
```

---

## 📊 Métricas (después de 50 épocas)

| Métrica   | Valor |
|-----------|--------|
| mAP50     | 0.571  |
| Recall    | 0.558  |
| Precisión | 0.652  |

---

## 🧠 Objetivo

Automatizar el control de seguridad en obras de construcción.  
La detección del casco es el primer paso hacia un sistema más amplio de monitoreo EHS *(Environment, Health, Safety)*.

---

## 📌 Ejemplo de resultado

📷 Se puede incluir una imagen de ejemplo antes/después aquí más adelante.

---

## 📃 Licencia

Proyecto con fines educativos o de investigación. Libre para adaptar según necesidades propias.
