# Changelog

## 2026-09-15

### Added

- Initial repository structure (README, docs/, scripts/, config/, tests/)
- `scripts/hello_robot.py` — first Git branch/PR workflow exercise
- `scripts/system_info.py` — system information utility using argparse
  and logging, with log level read from YAML config
- `config/example_config.yaml` — example configuration file
- `requirements.txt` — Python dependencies (`pyyaml`)
- `tests/test_system_info.md` — manual tests (basic run, missing argument)
- Daily reports for Days 1–3 (`docs/daily_reports/`)

### Changed

- Improved README with purpose, structure, setup, run, and testing
  sections
- Added a quick-start section to `docs/setup.md`

### Known Issues

- No automated tests yet (manual tests only)
- Proxy port for GitHub access is machine-specific; see `docs/setup.md`
