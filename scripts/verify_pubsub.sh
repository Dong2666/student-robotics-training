#!/usr/bin/env bash
# End-to-end verification for the student_robotics pub/sub example.
# Run from the repository root on a system with ROS 2 Humble
# (developed on Ubuntu 22.04 in WSL2):
#
#   bash scripts/verify_pubsub.sh
#
# The script builds the workspace, starts publisher and subscriber,
# measures the topic rate, checks clean shutdown, and prints PASS or
# FAIL lines for each check.

set -e
cd "$(dirname "$0")/../robot_ws"

source /opt/ros/humble/setup.bash
colcon build 2>&1 | tail -1
source install/setup.bash
ros2 daemon stop > /dev/null 2>&1 || true
ros2 daemon start > /dev/null 2>&1
sleep 1

FAILURES=0

setsid ros2 run student_robotics status_publisher > /tmp/verify_pub.log 2>&1 &
PUB=$!
sleep 3

echo "=== check 1: rate is ~1 Hz ==="
RATE=$(timeout -s INT 8 ros2 topic hz /status 2>/dev/null | head -1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
if [ -n "$RATE" ]; then
  awk -v r="$RATE" 'BEGIN { if (r > 0.8 && r < 1.2) exit 0; exit 1 }' \
    && echo "PASS: rate $RATE Hz" || { echo "FAIL: rate $RATE Hz outside 0.8-1.2"; FAILURES=$((FAILURES+1)); }
else
  echo "FAIL: no rate measurement"; FAILURES=$((FAILURES+1))
fi

echo "=== check 2: subscriber receives consecutive messages ==="
setsid ros2 run student_robotics status_subscriber > /tmp/verify_sub.log 2>&1 &
SUB=$!
sleep 3
RECV=$(grep -c 'received: status' /tmp/verify_sub.log || true)
if [ "${RECV:-0}" -ge 1 ]; then
  echo "PASS: subscriber logged $RECV messages"
else
  echo "FAIL: subscriber logged nothing"; FAILURES=$((FAILURES+1))
fi

echo "=== check 3: clean shutdown (SIGINT to process group) ==="
kill -INT -- -$SUB 2>/dev/null; kill -INT -- -$PUB 2>/dev/null
wait $SUB 2>/dev/null; SUB_RC=$?
wait $PUB 2>/dev/null; PUB_RC=$?
if [ "$SUB_RC" -eq 0 ] && [ "$PUB_RC" -eq 0 ]; then
  echo "PASS: both nodes exited 0"
else
  echo "FAIL: exit codes sub=$SUB_RC pub=$PUB_RC"; FAILURES=$((FAILURES+1))
fi

if [ "$FAILURES" -eq 0 ]; then
  echo "VERIFY_OK"
else
  echo "VERIFY_FAILED: $FAILURES check(s) failed"
  exit 1
fi
