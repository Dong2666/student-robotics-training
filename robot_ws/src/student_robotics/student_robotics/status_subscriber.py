import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String

STATUS_TOPIC = 'status'


class StatusSubscriber(Node):
    """Logs every message received on the status topic."""

    def __init__(self):
        super().__init__('status_subscriber')
        self.subscription = self.create_subscription(
            String, STATUS_TOPIC, self.on_status, 10)

    def on_status(self, msg):
        self.get_logger().info(f'received: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = StatusSubscriber()
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
