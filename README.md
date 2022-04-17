# vivaldi-feed-exporter

Since [Vivaldi](https://vivaldi.com) does not currently have the ability to export feeds,
I created a command line tool to generate [OPML](http://opml.org) based on a profile.

*Disclaimer : It depends on Vivaldi's implementation, so it may stop working at any time*

## Usage

- Follow [this page](https://help.vivaldi.com/ja/desktop-ja/tools-ja/import-and-export-browser-data/#Vivaldi) to identify your Vivaldi profile folder
- Install `vivaldi-feed-exporter` via `pipx install vivaldi-feed-exporter`
- Running `vivaldi-feed-exporter <profile folder path>` will output OPML to standard output

## Mapping of Vivaldi feed properties to OPML `outline` element attributes

Vivaldi feed property |`outline` attribute
-|-
title|`text`, `title`
address|`xmlUrl`
