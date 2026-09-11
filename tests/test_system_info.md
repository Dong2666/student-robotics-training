# Manual Tests for system_info.py

## Test 1: Basic Run

Command:

```
python scripts/system_info.py --name Student
```

Expected:

- Program exits without error
- Output includes `Hello Student`
- Output includes Python version
- Output includes operating system and machine architecture
- A `Collecting system information` log line appears (from logging)

## Test 2: Missing Name

Command:

```
python scripts/system_info.py
```

Expected:

- argparse shows an error about the missing `--name` argument
- Program exits with a non-zero status
