# ROS 2 Setup Guide

## Platform and Distribution

| Item | Choice | Reason |
|---|---|---|
| ROS 2 distribution | Humble | LTS (supported to 2027), matches the internship handbook |
| OS | Ubuntu 22.04 (jammy) | Officially paired with Humble |
| Virtualization | WSL2 (WSLg enabled) | Windows host; WSLg provides GUI support (RViz) without a VM |
| Install location | `D:\WSL\Ubuntu22` | C: drive had insufficient free space for the ~2.5 GB install |

Host: Windows 11, WSL version 2.7.14.

## Step 1 — apt Sources (China network)

The default archive servers were slow, so apt was pointed at the Tsinghua
TUNA mirror (original `sources.list` backed up first):

```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo tee /etc/apt/sources.list > /dev/null << 'EOF'
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
EOF
sudo apt-get update
```

Expected output: indexes fetched at several MB/s, no errors.

An engineer outside China can skip this step and use the official
archive.ubuntu.com sources with the official ROS 2 documentation.

## Step 2 — ROS 2 apt Repository

Key downloaded from `raw.githubusercontent.com` (direct connection worked
that day; via a local proxy is the usual fallback) and converted to a
keyring, then the ROS 2 repo was added — using the TUNA mirror of the
official ROS 2 apt repository:

```bash
curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] https://mirrors.tuna.tsinghua.edu.cn/ros2/ubuntu jammy main" | sudo tee /etc/apt/sources.list.d/ros2.list
sudo apt-get update
```

Expected output: `Get: ... https://mirrors.tuna.tsinghua.edu.cn/ros2/ubuntu jammy InRelease` with no GPG errors.

## Step 3 — Install

```bash
sudo apt-get install ros-humble-desktop python3-colcon-common-extensions ros-dev-tools
```

Expected result: `ros-humble-desktop` and its dependencies fully set up
(roughly 2.5 GB). A harmless warning `libcuda.so.1 is not a symbolic
link` appears on WSL — known WSL/CUDA interop noise, safe to ignore.

## Step 4 — Environment

```bash
echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
source ~/.bashrc
```

Verification:

```bash
which ros2          # /opt/ros/humble/bin/ros2
ros2 --help         # usage text
ros2 pkg prefix ros_base   # /opt/ros/humble
```

## Step 5 — Official talker/listener Verification

Two terminals (each with the environment sourced):

```bash
# Terminal 1
ros2 run demo_nodes_cpp talker
# Terminal 2
ros2 run demo_nodes_cpp listener
```

Actual output (2026-09-22):

```text
[INFO] [...8851...] [talker]: Publishing: 'Hello World: 1'
[INFO] [...8852...] [talker]: Publishing: 'Hello World: 2'
...
[INFO] [...8896...] [listener]: I heard: [Hello World: 8]
[INFO] [...8897...] [listener]: I heard: [Hello World: 9]
...
[INFO] [...8907...] [listener]: I heard: [Hello World: 19]
```

The listener received every message the talker published (8–19 in the
captured window) — publish/subscribe over DDS works end to end.

## Step 6 — Workspace

```bash
mkdir -p ~/robot_ws/src
cd ~/robot_ws
colcon build
source install/setup.bash
```

Expected output: `Summary: 0 packages finished` (empty workspace build),
and `build/ install/ log/` directories created.

Verification after sourcing the workspace overlay:

```text
COLCON_PREFIX_PATH: /home/<user>/robot_ws/install
AMENT_PREFIX_PATH: /opt/ros/humble   (underlay; no overlay entries yet — no packages installed)
ros2 pkg prefix demo_nodes_cpp      # still resolves: /opt/ros/humble
```

Note: `build/`, `install/`, and `log/` are generated artifacts and are
NOT committed to Git.

## Problems Encountered and Fixes

1. **C: drive too small for the install** — installed the Ubuntu 22.04
   WSL distribution to `D:\WSL\Ubuntu22` using
   `wsl --install --location`.
2. **Local proxy port stale** — the proxy port recorded earlier (10808)
   was not listening when the ROS key needed downloading; a direct
   connection to `raw.githubusercontent.com` succeeded instead. The
   general lesson from Week 1 stands: check what is actually listening
   before trusting a remembered port.
3. **Slow default apt mirrors** — switched to the TUNA mirror before the
   large ROS download (4.5 MB/s observed).

## Why the Workspace Must Be Sourced

`source install/setup.bash` prepends the workspace's `install` directory
to the environment (via `COLCON_PREFIX_PATH` and, once packages exist,
`AMENT_PREFIX_PATH` / `CMAKE_PREFIX_PATH`). Without it, `ros2` only sees
the underlay (`/opt/ros/humble`) and cannot find any package you built
in the workspace.
