from ultralytics import YOLO
import cv2

class YOLOInference:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)

    def run_inference(self, frame):
        results = self.model(frame)
        return results[0].plot()

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    detector = YOLOInference()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        output = detector.run_inference(frame)

        cv2.imshow('YOLOv8 Inference', output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
