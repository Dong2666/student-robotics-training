# ROS 2 Communication Tests — student_robotics

Manual tests for the publisher/subscriber pair (Milestone 2.4).

## Prerequisites

Two terminals, each with the environment sourced:

```bash
source /opt/ros/humble/setup.bash
cd robot_ws
colcon build
source install/setup.bash
```

## Test 1 — Publisher rate is ~1 Hz

Terminal 1:

```bash
ros2 run student_robotics status_publisher
```

Terminal 2:

```bash
timeout 6 ros2 topic hz /status
```

Expected: `average rate: 0.9-1.1` (1 Hz nominal, small measurement jitter).

## Test 2 — Message content carries sequence and uptime

```bash
ros2 topic echo /status
```

Expected (sequence increments by 1 per message, uptime monotonic):

```text
data: status 3 uptime=2.0s
---
data: status 4 uptime=3.0s
---
```

## Test 3 — Subscriber logs every received message

Terminal 2 (while the publisher runs in terminal 1):

```bash
ros2 run student_robotics status_subscriber
```

Expected — one INFO line per published message:

```text
[INFO] [...] [status_subscriber]: received: status 5 uptime=4.0s
```

## Test 4 — Graph discovery

```bash
ros2 node list     # /status_publisher, /status_subscriber
ros2 topic list    # /status present (plus /parameter_events, /rosout)
```

## Test 5 — Clean shutdown

Ctrl+C in each node terminal. Expected: the process exits without a
Python traceback (both KeyboardInterrupt and
ExternalShutdownException are handled, node destroyed, rclpy shut
down).

## Observed Evidence (2026-09-26)

Test 1 (rate):

```text
average rate: 1.002
        min: 0.975s max: 1.024s std dev: 0.02015s window: 3
average rate: 0.999
```

Test 2 (content):

```text
data: status 15 uptime=15.0s
---
data: status 16 uptime=16.0s
---
```

Test 3 (subscriber): `received: status 21 uptime=21.0s` — consecutive
messages 21, 22, 23 received with no gaps.

Test 5: both nodes exited with code 0 after SIGINT, no traceback.

Note: when killing `ros2 run` from a script, signal the whole process
group (`kill -INT -<pgid>`); Ctrl+C in a terminal does this
automatically, which is why the interactive case is clean.
