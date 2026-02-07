import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int8


class Talker(Node):

    def __init__(self):
        super().__init__('numeric_talker')

        # String publisher (original)
        self.string_publisher = self.create_publisher(String, 'chatter', 10)

        # New numeric publisher
        self.number_publisher = self.create_publisher(Int8, 'numeric_chatter', 10)

        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.talker_callback)

        self.counter = 0

    def talker_callback(self):

        # String message
        msg = String()
        msg.data = f'Hello World: {self.counter}'

        # Numeric message
        number = Int8()
        number.data = self.counter

        # Publish both
        self.string_publisher.publish(msg)
        self.number_publisher.publish(number)

        # Log
        self.get_logger().info(f'Publishing text: "{msg.data}" | number: {number.data}')

        # Increment and reset at 127
        self.counter += 1
        if self.counter > 127:
            self.counter = 0


def main(args=None):
    rclpy.init(args=args)

    node = Talker()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

