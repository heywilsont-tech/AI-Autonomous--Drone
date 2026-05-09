import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DroneNode(Node):
    def __init__(self):
        super().__init__('drone_node')
        self.publisher_ = self.create_publisher(String, 'drone_status', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.publish_status)

    def publish_status(self):
        msg = String()
        msg.data = 'Drone system active'
        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = DroneNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
