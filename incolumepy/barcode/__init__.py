"""
Principal Module.

Update metadata from version by semver
"""
import logging

from tomli import load
from pathlib import Path


configfile = Path(__file__).parents[2].joinpath("pyproject.toml")
versionfile = Path(__file__).parent.joinpath("version.txt")

try:
    with configfile.open('rb') as cf:
        versionfile.write_text(f"{load(cf)['tool']['poetry']['version']}\n")
except ValueError as e:
    logging.error(e)

__version__ = versionfile.read_text().strip()


if __name__ == '__main__':
    print(__version__)
