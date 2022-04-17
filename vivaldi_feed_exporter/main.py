from argparse import ArgumentParser
from collections.abc import Sequence
from pathlib import Path
from typing import Optional


def run():
    parse_args()


def parse_args(args: Optional[Sequence[str]] = None):
    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--profile-folder", type=_existent_directory, required=True
    )
    return parser.parse_args(args)


def _existent_directory(value: str):
    path = Path(value)
    if path.exists() and path.is_dir():
        return path
    raise Exception
