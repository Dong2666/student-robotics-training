# Tuesday Daily Report

## Date

2026-09-10 (Week 1, Day 2)

## Today's Goal

Learn Git branch and pull request workflow.

## Completed

- Learned the four core Git concepts: repository, commit, branch,
  pull request
- Created feature branch `feature/hello-robot`
- Wrote `scripts/hello_robot.py` (with `main()` and
  `if __name__ == "__main__"` guard)
- Ran the script and verified the output and exit code
- Updated README with a "Running the Hello Robot Script" section
- Removed `scripts/.gitkeep` (directory now has a real file)
- Committed and pushed the branch
- Opened [Pull Request #1](https://github.com/Dong2666/student-robotics-training/pull/1)
  with a structured description
- **PR #1 was reviewed and merged into main** (merge commit `e11c5b6`)
- Synced local main and deleted the merged local branch with
  `git branch -d`

## Problems Encountered

- First version of the PR description was incomplete: the
  "How I Tested", "Claude Code Usage" and "Notes" sections were lost
  while pasting (nested code blocks broke the markdown).

## How I Solved Them

- Edited the PR description and added the missing sections without
  nested code blocks, so the description answered all four review
  questions (what / why / how tested / what to look at).

## Claude Code Usage

- Used Claude Code to explain Day 2 concepts (repository, commit,
  branch, PR) with examples from my own repo.
- Used Claude Code to execute the branch → commit → push workflow,
  explaining each command as it ran.
- Claude Code performed a mock mentor review of PR #1 via the GitHub
  API and found the incomplete description.
- I answered the 5 mentor review questions (branch vs main, commit,
  PR purpose, undoing changes, what I tested) and studied the
  reference answers.

## What I Learned

- A branch is an isolated workspace; main stays clean and always
  usable.
- A commit is a small, focused, reversible checkpoint — one commit,
  one logical change.
- A PR is a communication tool, not just a merge button: it must say
  what changed, why, how it was tested.
- `if __name__ == "__main__"` makes a file work both as a script and
  as an importable module.
- To undo a pushed/merged change, use `git revert` (new inverse
  commit), never rewrite shared history with reset.
- `git branch -d` only deletes branches that are fully merged — a
  built-in safety net.
- GitHub shows the PR-creation URL right after pushing a new branch.

## Questions for Mentor

- When should a feature branch be deleted after merge — is remote
  branch cleanup also expected?
- For bigger features, is it better to open one PR per feature, or
  can one PR contain several related commits?

## Plan for Tomorrow

Build a more serious Python utility (`scripts/system_info.py`) using
argparse and logging.
