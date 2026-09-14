# Wednesday Daily Report

## Date

2026-09-14 (Week 1, Day 3)

## Today's Goal

Build a Python command-line utility using argparse and logging.

## Completed

- Wrote `scripts/system_info.py` on branch `feature/system-info`
  (argparse `--name`, system info, logging, log level from YAML config)
- Added `config/example_config.yaml`, `pyyaml` in `requirements.txt`,
  manual tests, README instructions
- Both manual tests pass (basic run exit 0; missing `--name` exit 2)
- Pushed the branch (`2ebb97c`)

## Problems Encountered

- `platform.release()` returns `10` on Windows 11; README initially said `11`.

## How I Solved Them

- Fixed the README to match actual output and documented the quirk.

## Claude Code Usage

- Explained argparse/logging/pathlib and drafted the script from the
  handbook starter; I reviewed each function and ran the tests myself.

## What I Learned

- argparse auto-rejects missing required arguments (non-zero exit).
- logging separates diagnostics from user output; level is configurable.
- pathlib builds paths safely; YAML config avoids hard-coded behavior.
- YAML `safe_load` is the standard way to read config.
- Document quirks instead of hiding them.

## Plan for Tomorrow

Open and merge the system-info PR; start Day 4 documentation work.
