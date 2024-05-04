from ultralytics import YOLO
#A

# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch

if __name__=='__main__':
    #hello from adi
    model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

#this is the good code
# model = YOLO('yolov8n.pt')
#
# # Use the model batch=-1 best results
    model.train(data="config.yaml", epochs=1)  # train the model






