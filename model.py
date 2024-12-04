from ultralytics import YOLO

# model
model = YOLO('yolov8.yaml')

# Training the model
# results = model.train(data="E://Animal_Detection//config//config.yaml", epochs=20 ,imgsz=640)
results = model.train(data="C://Users//Dell//Documents//GitHub//Animal_Detection_YOLOV8//BigCat.v5i.yolov8//data.yaml", epochs=20 ,imgsz=640)
