import cv2
import threading

class CameraStream:
    def __init__(self, source=0):
        self.capture = cv2.VideoCapture(source)
        self.frame = None
        self.running = False

    def start(self):
        self.running = True
        thread = threading.Thread(target=self.update_frames)
        thread.daemon = True
        thread.start()
        return self

    def update_frames(self):
        while self.running:
            success, frame = self.capture.read()
            if success:
                self.frame = frame

    def read(self):
        return self.frame

    def stop(self):
        self.running = False
        self.capture.release()

if __name__ == '__main__':
    stream = CameraStream().start()

    while True:
        frame = stream.read()

        if frame is not None:
            cv2.imshow('Camera Stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    stream.stop()
    cv2.destroyAllWindows()
