from ultralytics import YOLO
#A

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch



#model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

#this is the good code
# model = YOLO('yolov8n.pt')
#
# # Use the model batch=-1 best results
model.train(data="config.yaml", epochs=800)  # train the model






