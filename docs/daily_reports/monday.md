# Monday Daily Report

## Date

2026-09-10 (Week 1, Day 1)

## Today's Goal

Set up development tools and create the first repository.

## Completed

- Verified tools: Git 2.41.0, Python 3.11.7, VS Code, Claude Code 2.1.143
- Created GitHub repo `student-robotics-training`, cloned to Desktop
- Created Week 1 folder structure, wrote `README.md` and `docs/setup.md`
- First commit pushed

## Problems Encountered

- `git clone` failed with `Recv failure: Connection was reset`. Git's
  proxy was set to port 13839, but the proxy software (v2rayN/sing-box)
  actually listens on 10808; direct connection to GitHub also failed.

## How I Solved Them

- Found the real listening port with `netstat -ano`, verified it with
  `curl -x http://127.0.0.1:10808 https://github.com` (HTTP 200), then
  ran `git config --global http.proxy http://127.0.0.1:10808`.
  Clone worked right after.

## Claude Code Usage

- Used it to verify tool versions and diagnose the proxy port mismatch.
- I followed each diagnosis step and applied the config fix with it.

## What I Learned

- A stale `http.proxy` port in Git config causes confusing connection errors.
- `netstat -ano` shows which process listens on which port.
- `curl -x` tests a proxy before wiring it into a tool.
- Git does not track empty directories; `.gitkeep` is the workaround.
- Setup problems are normal engineering problems — document them.

## Plan for Tomorrow

Learn Git branches and pull requests.
