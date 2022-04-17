import json
from argparse import ArgumentParser
from collections.abc import Callable, Sequence
from pathlib import Path
from typing import Any, Optional

from vivaldi_feed_exporter.opml import opml

_PREFERENCE_FILENAME = "Preferences"
_FEEDS_GETTER: Callable[[dict[str, Any]], list[dict[str, str]]] = lambda p: p[
    "vivaldi"
]["rss"]["settings"]


def run():
    with open(parse_args().profile_folder / _PREFERENCE_FILENAME, encoding="utf8") as f:
        preferences = json.load(f)
    feeds = _FEEDS_GETTER(preferences)
    print(opml(feeds).to_xml())


def parse_args(args: Optional[Sequence[str]] = None):
    parser = ArgumentParser()
    parser.add_argument(
        "profile_folder", type=_existent_directory, metavar="<profile folder>"
    )
    return parser.parse_args(args)


def _existent_directory(value: str):
    path = Path(value)
    if path.exists() and path.is_dir():
        return path
    raise Exception
