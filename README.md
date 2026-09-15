# student-robotics-training

Software engineering training repository for the Berkeley Humanoid Lite
software internship.

## Purpose

This repository contains my Week 1 engineering training work: environment
setup, Git/GitHub workflow practice, small Python utilities, and the
documentation that lets another student reproduce everything here.
It is written for my mentor and for future students.

## Repository Structure

- `docs/` — documentation: setup guide, project structure, changelog,
  and daily reports
- `scripts/` — small Python utilities
- `config/` — example configuration files
- `tests/` — manual test procedures
- `requirements.txt` — Python dependencies

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

## Current Status

Week 1 (in progress):

- [x] Day 1 — environment setup, repository creation
- [x] Day 2 — Git branch/PR workflow (`hello_robot.py`, PR #1 merged)
- [x] Day 3 — `system_info.py` with argparse/logging (PR #2 merged)
- [x] Day 4 — documentation pass
- [ ] Day 5 — weekly report and demo

## Next Steps

Finish the weekly report and demo. Week 2 will introduce ROS 2.
