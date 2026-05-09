import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')

        self.subscription = self.create_subscription(
            String,
            'drone_status',
            self.status_callback,
            10
        )

        self.subscription

    def status_callback(self, msg):
        self.get_logger().info(f'Received status: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
