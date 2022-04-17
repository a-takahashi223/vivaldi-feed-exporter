from collections.abc import Iterable

from opyml import OPML, Body, Head, Outline


def opml(feeds: Iterable[dict[str, str]]):
    return OPML(
        version="2.0",
        head=Head(title="Vivaldi Subscriptions"),
        body=Body(
            outlines=tuple(
                Outline(text=f["title"], xml_url=f["url"], title=f["title"])
                for f in feeds
            )
        ),
    )
