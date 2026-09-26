# student-robotics-training

Software engineering training repository for the Berkeley Humanoid Lite
software internship.

## Purpose

This repository contains my internship training work: engineering
fundamentals (environment, Git/GitHub workflow, Python utilities) and,
from Week 2 on, ROS 2 development for the Berkeley Humanoid Lite
project. It is written for my mentor and for future students.

## Repository Structure

- `docs/` — documentation: setup guides, package structure, changelog,
  and daily reports
- `robot_ws/` — ROS 2 workspace (`src/student_robotics` package)
- `scripts/` — small Python utilities
- `config/` — example configuration files
- `tests/` — manual test procedures
- `requirements.txt` — Python dependencies
- `LICENSE` — MIT

## Setup

Requires Python 3.10+ (developed on 3.11.7, Windows 11).

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

(In Git Bash use `source .venv/Scripts/activate`; on Linux/macOS use
`source .venv/bin/activate`.)

The full setup history, including problems encountered and fixes, is in
[docs/setup.md](docs/setup.md).

## Running Examples

### Hello Robot

```
python scripts/hello_robot.py
```

Expected output:

```
Hello, Berkeley Humanoid Lite software project!
```

### System Info

```
python scripts/system_info.py --name Student
```

Expected output:

```
Hello Student
python_version: 3.11.7
operating_system: Windows
os_release: 10
machine: AMD64
```

Note: on Windows 11, `platform.release()` still reports `10`.

## Testing

Manual test procedures live in `tests/`:

- `tests/test_system_info.md` — two manual tests for `system_info.py`
  (basic run, and the missing-argument error case)

## ROS 2 Workspace

Requires ROS 2 Humble on Ubuntu 22.04 — see
[docs/ros2_setup.md](docs/ros2_setup.md).

```
cd robot_ws
colcon build
source install/setup.bash
ros2 run student_robotics hello_node
```

Expected output (the node idles until interrupted):

```
[INFO] [...] [hello_node]: student_robotics hello node started
```

Package file roles and the build-to-run chain are explained in
[docs/ros2_package_structure.md](docs/ros2_package_structure.md).

### Publisher / Subscriber

Two terminals (each sourced as above):

```bash
# Terminal 1
ros2 run student_robotics status_publisher
# Terminal 2
ros2 run student_robotics status_subscriber
```

The publisher sends `status <n> uptime=<s>` on `/status` at 1 Hz; the
subscriber logs each message. Verify independently:

```bash
ros2 topic hz /status      # average rate ~1.0
ros2 topic echo /status    # message content
```

Manual test procedures: [docs/ros2_communication_tests.md](docs/ros2_communication_tests.md).

## Current Status

Week 1 — complete (environment, Git/PR workflow, Python utilities,
documentation; weekly report in `docs/weekly_report.md`).

Week 2 (ROS 2):

- [x] M2.1 — Week 1 release + clean-clone verification (PR #4)
- [x] M2.2 — ROS 2 Humble installed and verified (talker/listener,
      workspace, setup docs)
- [x] M2.3 — first ROS 2 package `student_robotics` with `hello_node`
- [x] M2.4 — publisher/subscriber communication (1 Hz status topic,
      CLI-verified with hz/echo)
- [ ] M2.5 — reusable onboarding example

## Next Steps

Milestone 2.5: launch file, parameters, troubleshooting docs.
