from ultralytics import YOLO
import torch

class ModelLoader:
    def __init__(self, model_path='yolov8n.pt'):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = YOLO(model_path)

    def get_device(self):
        return self.device

    def predict(self, frame):
        return self.model(frame)

if __name__ == '__main__':
    loader = ModelLoader()

    print(f'Running on device: {loader.get_device()}')
