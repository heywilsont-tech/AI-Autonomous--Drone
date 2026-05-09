import cv2

class ObstacleDetector:
    def __init__(self, threshold=100):
        self.threshold = threshold

    def detect_edges(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        return edges

if __name__ == '__main__':
    detector = ObstacleDetector()

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        edges = detector.detect_edges(frame)

        cv2.imshow('Obstacle Detection', edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
