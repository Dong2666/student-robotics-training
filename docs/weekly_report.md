# Week 1 Report

## Summary

Week 1 built the engineering foundation for the rest of the internship:
a working development environment, a GitHub repository with a clean
history, a branch/PR workflow, two small Python utilities, manual
tests, and complete documentation. Three pull requests were opened and
merged (hello-robot, system-info, week1-documentation).

## Deliverables Completed

- Development environment: Git, Python 3.11.7, VS Code, Claude Code
- GitHub repository `student-robotics-training` (cloned, structured)
- `scripts/hello_robot.py` (first branch/PR exercise)
- `scripts/system_info.py` (argparse, logging, pathlib, YAML config)
- `config/example_config.yaml`, `requirements.txt`
- Manual tests (`tests/test_system_info.md`)
- Documentation: README, `docs/setup.md`, `docs/project_structure.md`,
  `docs/changelog.md`
- Daily reports Monday–Thursday
- 3 PRs opened, 3 PRs merged

## Technical Skills Practiced

- Git: status/add/commit/push, branches, merge, branch cleanup,
  revert-vs-reset concepts, amend (once, on a solo branch)
- GitHub: pull requests, PR descriptions, merge flow
- Python: argparse, logging, pathlib, yaml, functions and main() guard
- Markdown documentation
- Claude Code as a supervised engineering tool

## Problems Encountered

1. `git clone` failed with "Connection was reset": Git proxy pointed to
   a stale port (13839) while the proxy software listened on 10808.
2. First PR description lost several sections when pasting (nested
   code blocks broke the markdown).
3. One push failed with `SSL_ERROR_SYSCALL` (transient network issue,
   succeeded on retry).
4. `platform.release()` returns `10` on Windows 11, mismatching the
   README's expected output.

## Lessons Learned

1. Stale tool config produces misleading errors — check the real
   listening port before blaming the network.
2. `netstat -ano` finds which process owns a port; `curl -x` tests a
   proxy before wiring it into a tool.
3. Git does not track empty directories; `.gitkeep` is the workaround.
4. Branches isolate experiments; main stays clean and always usable.
5. A commit is one small, focused, reversible change with a clear
   message.
6. A PR is communication: what changed, why, how tested — and plain
   markdown without nested code fences survives pasting.
7. Undo shared/pushed changes with `git revert`, never by rewriting
   history; `git branch -d` refuses to delete unmerged work.
8. logging separates diagnostics from user output; print is for users.
9. argparse gives argument validation and non-zero exits for free.
10. pathlib plus a YAML config keeps behavior out of source code.
11. Documentation must match actual output; document quirks (Windows 11
    reporting release "10") instead of hiding them.
12. Write reports and docs for the next reader, not for memory.

## What I Would Improve

- Start daily reports earlier in the day instead of at the end.
- Turn the manual tests into automated tests (pytest) soon.
- Preview PR markdown rendering before submitting the description.
- Make smaller, more frequent commits within a day.

## Plan for Week 2

Prepare for ROS 2: review Week 1 notes, keep the same Git/PR discipline,
and apply the documentation habits to ROS 2 setup and package work.
