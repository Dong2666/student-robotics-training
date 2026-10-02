# Clean-Clone Verification — Week 2 Release

Reproducibility test for the Week 2 (ROS 2) milestone, per the handbook
release checklist: a fresh clone of `main` must build and run by
following only the repository documentation.

## Procedure

1. Cloned `https://github.com/Dong2666/student-robotics-training`
   into an empty home directory (WSL Ubuntu 22.04, ROS 2 Humble).
2. Followed only the README, no prior state:

   ```
   cd robot_ws
   colcon build
   source install/setup.bash
   ros2 launch student_robotics status_demo.launch.py
   ```

3. Measured the topic rate while the launch file ran.
4. Ran the automated end-to-end check: `bash scripts/verify_pubsub.sh`.

## Results (2026-09-29)

| Check | Expected | Observed |
|---|---|---|
| clone from GitHub | succeeds | succeeded |
| `colcon build` | no errors | clean build |
| launch, `ros2 topic hz /status` | ~1.0 Hz | 1.000 Hz |
| launch Ctrl+C exit code | 0 | 0 |
| `verify_pubsub.sh` rate check | PASS | PASS: 0.999 Hz |
| `verify_pubsub.sh` subscriber check | PASS | PASS: 3 messages |
| `verify_pubsub.sh` shutdown check | PASS | PASS: both exited 0 |
| `verify_pubsub.sh` overall | `VERIFY_OK`, exit 0 | `VERIFY_OK`, exit 0 |

Everything a new student needs to run the Week 2 example is in the
repository: no hidden steps, no machine-specific fixes.

## Re-run After M3.1 Cleanup (2026-10-03)

Same procedure on a fresh clone of `main` after PR #12 hardened the
verification script:

| Check | Expected | Observed |
|---|---|---|
| clone from GitHub | succeeds | succeeded |
| `colcon build` | no errors | clean build |
| launch, `ros2 topic hz /status` | ~1.0 Hz | 1.000 Hz |
| launch Ctrl+C exit code | 0 | 0 |
| `verify_pubsub.sh` rate check | PASS | PASS: 1.000 Hz |
| `verify_pubsub.sh` subscriber check | PASS | PASS: 1 message (polled startup) |
| `verify_pubsub.sh` shutdown check | PASS | PASS: both exited 0 |
| `verify_pubsub.sh` overall | `VERIFY_OK`, exit 0 | `VERIFY_OK`, exit 0 |

The hardened script also aborts on build failure (pipefail) and cleans
up background nodes on every exit path; these paths were exercised by
an earlier run after a WSL VM restart, where the script honestly
reported check 2/3 failures on a cold start before the polling fix.
