import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int8


class Listener(Node):

    def __init__(self):
        super().__init__('numeric_listener')

        # Original subscriber
        self.text_subscriber = self.create_subscription(
            String,
            'chatter',
            self.text_callback,
            10
        )

        # New numeric subscriber
        self.number_subscriber = self.create_subscription(
            Int8,
            'numeric_chatter',
            self.number_callback,
            10
        )

    # Callback for /chatter
    def text_callback(self, msg):
        self.get_logger().info(f'I heard text: "{msg.data}"')

    # Callback for /numeric_chatter
    def number_callback(self, msg):
        self.get_logger().info(f'I heard number: {msg.data}')


def main(args=None):
    rclpy.init(args=args)

    node = Listener()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

