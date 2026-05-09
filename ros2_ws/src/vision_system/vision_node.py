import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class VisionNode(Node):
    def __init__(self):
        super().__init__('vision_node')

        self.publisher = self.create_publisher(Image, 'camera/image_raw', 10)
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(0)

        self.timer = self.create_timer(0.03, self.publish_frame)

    def publish_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            self.get_logger().warning('Failed to capture frame')
            return

        msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.publisher.publish(msg)

        self.get_logger().info('Publishing camera frame')


def main(args=None):
    rclpy.init(args=args)
    node = VisionNode()
    rclpy.spin(node)

    node.cap.release()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
