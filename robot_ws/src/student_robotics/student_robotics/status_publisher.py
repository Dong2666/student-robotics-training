import time

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String

STATUS_TOPIC = 'status'


class StatusPublisher(Node):
    """Publishes a status message with sequence number and uptime at 1 Hz."""

    def __init__(self):
        super().__init__('status_publisher')
        self.publisher = self.create_publisher(String, STATUS_TOPIC, 10)
        self.timer = self.create_timer(1.0, self.publish_status)
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
