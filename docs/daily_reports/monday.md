# Monday Daily Report

## Date

2026-09-10 (Week 1, Day 1)

## Today's Goal

Set up development tools and create the first repository.

## Completed

- Installed/verified Git (2.41.0.windows.3)
- Installed/verified Python (3.11.7)
- Installed/verified VS Code
- Installed/verified Claude Code (2.1.143)
- Confirmed Git username and email were already configured
- Created GitHub repository `student-robotics-training` (with README init)
- Cloned the repository locally to `Desktop/student-robotics-training`
- Created the Week 1 folder structure (`docs/daily_reports`, `scripts`,
  `tests`, `config`, plus `.gitkeep` placeholders for the empty ones)
- Wrote `README.md` with Week 1 goals
- Wrote `docs/setup.md` documenting the setup steps and problems
- Made the first commit and pushed it to GitHub

## Problems Encountered

- `git clone` failed with `fatal: unable to access ... Recv failure:
  Connection was reset`. The Git global config pointed to a proxy on
  `127.0.0.1:13839`, but no process was listening on that port. The
  proxy software (v2rayN + sing-box) was running, but its actual mixed
  port is `10808`. Direct connection to GitHub also timed out.

## How I Solved Them

1. Used `netstat -ano` to find which ports were listening and which
   process owned them → found sing-box listening on `127.0.0.1:10808`.
2. Tested the port with `curl -x http://127.0.0.1:10808
   https://github.com` → HTTP 200.
3. Updated the Git proxy:
   `git config --global http.proxy http://127.0.0.1:10808`
4. Retried `git clone` → succeeded.

## Claude Code Usage

- Used Claude Code to verify installed tool versions (git, python,
  code, claude).
- Used Claude Code to diagnose the proxy problem: check the listening
  ports, test the proxy with curl, and apply the config fix.
- I followed the diagnosis step by step and understood the cause
  (stale proxy port in Git config) before applying the fix.

## What I Learned

- Git uses `http.proxy` from global config for HTTPS operations; if the
  configured port is stale, remote operations fail with confusing
  errors like "Connection was reset".
- `netstat -ano` shows which process is listening on which port —
  useful to discover a proxy's real port.
- `curl -x <proxy>` tests a proxy before wiring it into a tool.
- Git does not track empty directories; `.gitkeep` files are the
  standard workaround.
- Git on Windows converts line endings (LF/CRLF) automatically — the
  warning during `git add` is normal.
- Setup problems are normal engineering problems; writing them down
  (in `docs/setup.md`) turns them into documentation.

## Questions for Mentor

- Should the repository stay Public, or is Private preferred for
  training work?

## Plan for Tomorrow

Learn Git branches and pull requests, and open my first PR with a
`hello_robot.py` script.
