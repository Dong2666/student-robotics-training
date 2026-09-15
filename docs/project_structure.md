# Project Structure

## docs/

Documentation and reports: this file, the setup guide
([setup.md](setup.md)), the changelog ([changelog.md](changelog.md)),
and daily reports in `daily_reports/`.

## scripts/

Small Python utilities:

- `hello_robot.py` — prints a greeting
- `system_info.py` — prints system information (argparse + logging)

## config/

Example configuration files. `example_config.yaml` holds the project
name, the default log level read by `system_info.py`, and the student
role.

## tests/

Manual or automated tests. Currently `test_system_info.md` documents
two manual test procedures for `system_info.py`.

## requirements.txt

Python dependencies (currently `pyyaml`), installable with
`pip install -r requirements.txt`.

---

This repository is intentionally simple during Week 1. We avoid
unnecessary architecture until the project needs it.
