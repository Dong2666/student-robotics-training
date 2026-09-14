"""System information utility for Week 1 engineering onboarding."""

import argparse
import logging
import platform
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Print basic system information."
    )
    parser.add_argument("--name", required=True, help="Name of the user")
    return parser.parse_args()


def load_default_log_level(project_root):
    config_path = project_root / "config" / "example_config.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config.get("default_log_level", "INFO")


def collect_system_info():
    return {
        "python_version": platform.python_version(),
        "operating_system": platform.system(),
        "os_release": platform.release(),
        "machine": platform.machine(),
    }


def main():
    project_root = Path(__file__).resolve().parents[1]
    logging.basicConfig(level=load_default_log_level(project_root))
    args = parse_args()
    logger.info("Collecting system information")
    info = collect_system_info()
    print(f"Hello {args.name}")
    for key, value in info.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
