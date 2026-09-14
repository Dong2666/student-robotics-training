# student-robotics-training

This repository contains my software engineering training work for the Berkeley Humanoid Lite project.

## Week 1 Goals

- Set up development environment
- Learn Git workflow
- Write a small Python utility
- Practice documentation

## Running the Hello Robot Script

```
python scripts/hello_robot.py
```

Expected output:

```
Hello, Berkeley Humanoid Lite software project!
```

## Running the System Info Script

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

Dependencies are listed in `requirements.txt`:

```
pip install -r requirements.txt
```
