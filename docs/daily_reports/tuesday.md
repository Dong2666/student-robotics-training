# Tuesday Daily Report

## Date

2026-09-10 (Week 1, Day 2)

## Today's Goal

Learn Git branch and pull request workflow.

## Completed

- Created branch `feature/hello-robot`, wrote and ran
  `scripts/hello_robot.py` (`python scripts/hello_robot.py`, exit code 0)
- Updated README with run instructions
- Opened [PR #1](https://github.com/Dong2666/student-robotics-training/pull/1)
  and merged it (`e11c5b6`)
- Synced local main, deleted the merged branch with `git branch -d`

## Problems Encountered

- First PR description was incomplete: the "How I Tested" and later
  sections were lost while pasting (nested code blocks broke the markdown).

## How I Solved Them

- Edited the PR description and re-added the missing sections without
  nested code blocks, so it answered what/why/how-tested.

## Claude Code Usage

- Used it to explain branch/commit/PR concepts and run the git workflow
  step by step; it also mock-reviewed PR #1 and caught the missing
  "How I Tested" section.
- I answered the mentor review questions myself before merging.

## What I Learned

- Branches isolate work; main stays clean and usable.
- One commit = one logical change (small, focused, reversible).
- A PR must say what changed, why, and how it was tested.
- `if __name__ == "__main__"` lets a file run as a script and stay importable.
- Undo pushed/merged changes with `git revert`; never rewrite shared history.

## Plan for Tomorrow

Build `scripts/system_info.py` with argparse and logging.
