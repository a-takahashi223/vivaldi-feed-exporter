import json

from vivaldi_feed_exporter.opml import opml


def test_opml():
    title = "outline title"
    url = "http://www.example.com/foo.atom"
    assert json.loads(opml((dict(title=title, url=url),)).to_json()) == dict(
        version="2.0",
        head=dict(title="Vivaldi Subscriptions"),
        body=dict(outlines=[dict(text=title, xml_url=url, title=title, outlines=[])]),
    )
