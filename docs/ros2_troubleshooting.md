# ROS 2 Troubleshooting — Real Errors from Week 2

Every entry below was actually hit during Week 2 and the fix was
verified. No generic advice.

## 1. Entry point exists but fails with StopIteration at runtime

Symptom: `ros2 run student_robotics status_subscriber` prints a
traceback ending in `StopIteration` from `load_entry_point`, even
though the script file exists in `install/.../lib/student_robotics/`.

Cause: the installed entry-point metadata
(`...egg-info/entry_points.txt`) was stale — generated during an
earlier build before the new `console_scripts` lines were added to
`setup.py`. The build "succeeds" but installs old metadata.

Fix: delete generated artifacts and rebuild clean, then re-source:

```bash
cd robot_ws
rm -rf build install log
colcon build
source install/setup.bash
```

Rule: after changing `entry_points` (or any packaging metadata), a
clean rebuild plus re-source is mandatory.

## 2. Traceback on Ctrl+C: ExternalShutdownException

Symptom: the node handles SIGINT but still prints
`rclpy.executors.ExternalShutdownException` and exits with code 1.

Cause: when SIGINT interrupts `rclpy.spin` inside the C wait call,
rclpy raises `ExternalShutdownException`, not `KeyboardInterrupt`. A
`try/except KeyboardInterrupt` alone misses it.

Fix (in every node's `main()`):

```python
from rclpy.executors import ExternalShutdownException
...
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
```

Verified: both nodes exit 0 with no traceback after the change.

## 3. Killing `ros2 run` from a script leaves the node alive

Symptom: a script starts `ros2 run ... &`, kills the stored PID, but
the node process keeps running (two publishers then publish together —
`ros2 topic hz` reports 2 Hz instead of 1 Hz).

Cause: `ros2 run` is a wrapper; the actual node is a child process.
Signaling the wrapper does not signal the child. Ctrl+C works
interactively because the terminal signals the whole foreground
process group.

Fix: start the node in its own session (`setsid`) and signal the
process group:

```bash
setsid ros2 run student_robotics status_publisher > pub.log 2>&1 &
PUB=$!
kill -INT -- -$PUB   # negative PID = process group
```

Check for strays before re-testing: `pkill -f 'status_p[u]blisher'`
(brackets stop the pattern matching the grep itself).

## 4. `ros2 launch` Ctrl+C prints "process has died [exit code -2]"

Symptom: after Ctrl+C, launch logs
`process has died [pid ..., exit code -2 ...]` for each node.

Cause: exit code -2 means the process was terminated by signal 2
(SIGINT) — launch is reporting the signal it forwarded, not a crash.
launch itself exits 0.

Fix: none needed. Distinguish real crashes (exit code 1, Python
traceback in the log) from signal reports (negative exit code, no
traceback).

## 5. First `ros2 topic` commands print nothing

Symptom: `ros2 topic hz /status` prints no measurements inside a short
timeout; `ros2 node list` returns an empty list even though nodes run.

Cause: the ROS 2 CLI daemon was not running (or died). The first CLI
calls wait for the daemon to spawn, which can exceed a short script
timeout — especially on a slow filesystem.

Fix: start the daemon explicitly before scripted checks, and use
generous timeouts:

```bash
ros2 daemon stop > /dev/null 2>&1
ros2 daemon start > /dev/null 2>&1
sleep 2
```

## 6. Driving WSL from Git Bash silently rewrites paths

Symptom (Windows host tooling): a `wsl -- bash -c "... /home/..."`
command fails with `C:/Program Files/Git/home/...` — Git Bash (MSYS)
converts arguments that begin with `/` into Windows paths before
wsl.exe sees them.

Fix: keep absolute POSIX paths inside the quoted command string (not
as bare arguments), or write the commands into a script file and run
`wsl -- bash /mnt/d/WSL/script.sh`. Also strip Windows line endings
(`tr -d '\r'`) when scripts travel through the Windows filesystem.
