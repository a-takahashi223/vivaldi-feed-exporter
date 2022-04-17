# vivaldi-feed-exporter

[Vivaldi](https://vivaldi.com)には現在のところフィードのエクスポート機能がないので、プロファイルを元に[OPML](http://opml.org)を生成する
コマンドラインツールを作りました。

*おことわり : Vivaldiの実装依存なのでいつ動かなくなるかわかりません*

## 使い方

- [このページ](https://help.vivaldi.com/ja/desktop-ja/tools-ja/import-and-export-browser-data/#Vivaldi)に従ってVivaldiプロファイルフォルダを特定
- `pipx install vivaldi-feed-exporter`で`vivaldi-feed-exporter`をインストールする
- `vivaldi-feed-exporter -p <プロファイルフォルダのパス>`を実行すると、標準出力にOPMLが出力される

## VivaldiのフィードプロパティとOPMLの`outline`要素の属性との対応

Vivaldiフィードプロパティ|`outline`属性
-|-
タイトル|`text`, `title`
アドレス|`xmlUrl`
