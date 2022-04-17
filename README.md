# vivaldi-feed-exporter

Since [Vivaldi](https://vivaldi.com) does not currently have the ability to export feeds,
I created a command line tool to generate [OPML](http://opml.org) based on a profile.

*Disclaimer : It depends on Vivaldi's implementation, so it may stop working at any time*

## Usage

- Follow [this page](https://help.vivaldi.com/desktop/tools/import-and-export-browser-data/#Transfer_the_full_Vivaldi_browser_profile) 
  to identify your Vivaldi profile folder
- Install `vivaldi-feed-exporter` via `pipx install vivaldi-feed-exporter`
- Running `vivaldi-feed-exporter <profile folder path>` will output OPML to standard output

## Mapping of Vivaldi feed properties to OPML `outline` element attributes

Vivaldi feed property |`outline` attribute
-|-
title|`text`, `title`
address|`xmlUrl`
