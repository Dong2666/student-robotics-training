# Development Environment Setup

This document records how the development environment for this
repository was set up, so that another student could rebuild it.

## Computer

- Operating system: Windows 11 Home China (build 10.0.26200)
- Python version: 3.11.7
- Git version: 2.41.0.windows.3
- VS Code installed: yes
- Claude Code installed: yes (version 2.1.143)

## Steps Completed

1. Installed Git (already installed, verified with `git --version`)
2. Configured Git username and email (already configured)
3. Installed Python (3.11.7, verified with `python --version`)
4. Installed VS Code (already installed)
5. Installed Claude Code (already installed, verified with `claude --version`)
6. Created GitHub repository
   [student-robotics-training](https://github.com/Dong2666/student-robotics-training)
   (initialized with a README)
7. Cloned the repository locally to `Desktop/student-robotics-training`
8. Created the Week 1 folder structure:
   `docs/daily_reports`, `scripts`, `tests`, `config`

## Problems Encountered

### Problem 1: `git clone` failed with "Connection was reset"

- Command: `git clone https://github.com/Dong2666/student-robotics-training.git`
- Error: `fatal: unable to access ... Recv failure: Connection was reset`

**Diagnosis:**

1. The Git global config had `http.proxy=http://127.0.0.1:13839`,
   but `netstat -ano` showed **no process listening on port 13839**.
2. The proxy software (v2rayN with sing-box core) was running, but its
   mixed proxy port is actually **10808** (found via `netstat -ano` and
   checking which process owns the port).
3. Direct connection (no proxy) to `https://github.com` also timed
   out, so this network requires a proxy for GitHub.
4. Verified the port with
   `curl -x http://127.0.0.1:10808 https://github.com` → HTTP 200.

**Fix:**

```
git config --global http.proxy http://127.0.0.1:10808
```

After this, `git clone` worked immediately.

## Commands Used

```
git --version
python --version
code --version
claude --version
git config --global --list
git config --global http.proxy http://127.0.0.1:10808
git clone https://github.com/Dong2666/student-robotics-training.git
mkdir -p docs/daily_reports scripts tests config
```

## Notes for Future Students

- If `git clone` fails with a connection error in this network
  environment, first check which port your proxy software is really
  listening on (`netstat -ano | findstr LISTENING`), then make sure
  Git's `http.proxy` matches that port. Proxy software updates can
  change the default port and leave a stale value in Git config.
- `curl -x <proxy> https://github.com` is a quick way to test a proxy
  before wiring it into any tool.
- Git does not track empty directories; `.gitkeep` placeholder files
  are used to keep `scripts/`, `tests/`, and `config/` in the
  repository.
