import time

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String

STATUS_TOPIC = 'status'
DEFAULT_RATE = 1.0


class StatusPublisher(Node):
    """Publishes a status message with sequence number and uptime.

    The publish rate is configurable through the `rate` parameter (Hz).
    """

    def __init__(self):
        super().__init__('status_publisher')
        self.declare_parameter('rate', DEFAULT_RATE)
        rate = self.get_parameter('rate').get_parameter_value().double_value
        self.get_logger().info(f'publishing {STATUS_TOPIC!r} at {rate} Hz')
        self.publisher = self.create_publisher(String, STATUS_TOPIC, 10)
        self.timer = self.create_timer(1.0 / rate, self.publish_status)
        self.sequence = 0
        self.start_time = time.monotonic()

    def publish_status(self):
        self.sequence += 1
        elapsed = time.monotonic() - self.start_time
        msg = String()
        msg.data = f'status {self.sequence} uptime={elapsed:.1f}s'
        self.publisher.publish(msg)
        self.get_logger().info(f'published: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = StatusPublisher()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
