import cv2

class ObjectTracker:
    def __init__(self):
        self.tracker = cv2.TrackerCSRT_create()
        self.initialized = False

    def initialize(self, frame, bbox):
        self.tracker.init(frame, bbox)
        self.initialized = True

    def update(self, frame):
        if not self.initialized:
            return False, None

        success, bbox = self.tracker.update(frame)
        return success, bbox

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    tracker = ObjectTracker()

    initialized = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if not initialized:
            bbox = cv2.selectROI('Tracking', frame, False)
            tracker.initialize(frame, bbox)
            initialized = True

        success, bbox = tracker.update(frame)

        if success:
            x, y, w, h = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
