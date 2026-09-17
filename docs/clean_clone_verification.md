# Clean-Clone Verification Record

## Goal

Verify that another engineer can clone `main`, follow only the
repository documentation, and reproduce every Week 1 deliverable
without asking the author anything.

## Verification Details

- Date: 2026-09-18
- Source: fresh `git clone` of `main` from GitHub into a new
  directory (`clean-clone-test`, outside the development working copy)
- Environment: Windows 11, Python 3.11.7 (system Python, new venv)

## Steps Performed and Results

| # | Step (from docs) | Result |
|---|---|---|
| 1 | `git clone https://github.com/Dong2666/student-robotics-training.git` | OK |
| 2 | `python -m venv .venv` | OK |
| 3 | `.venv\Scripts\activate` + `pip install -r requirements.txt` | OK (PyYAML 6.0.3 installed) |
| 4 | `python scripts/hello_robot.py` | OK — expected greeting |
| 5 | `python scripts/system_info.py --name Student` | OK — output matches README expected output exactly (including `os_release: 10` on Windows 11) |
| 6 | `python scripts/system_info.py` (missing `--name`) | OK — argparse error, exit code 2, as documented in `tests/test_system_info.md` |

## Issues Found

None. Every documented command worked on the first attempt from the
clean clone; no documentation gaps were discovered.

## Conclusion

main is releasable: a fresh clone plus `docs/setup.md` and the README
is sufficient to reproduce Week 1. This satisfies the acceptance
criteria of Week 2 Milestone 2.1.
