# Twitter に自動でツイートをする

## 概要

IFTTT を用いて Python から Twitter に自動でツイートをするプログラム

## 準備

### IFTTT の登録設定

IFTTT の登録設定をする。
こちらの記事の Line の箇所を Twitter に変更する。
https://chasuke.com/python_ifttt/

IFTTT の Webhook 呼ぶための URL をコピー、
`.env`ファイルを作成し、下記のように記述をする。

```
webhook_url="Webhook呼ぶためのURL"
```

Twiiter の設定は、こちらにする
<img width="100%" alt="スクリーンショット 2020-11-22 15 38 32" src="https://user-images.githubusercontent.com/52241300/99897108-2169b300-2cda-11eb-961a-d0a77ac0ac65.png">

## 使い方

下記のコマンドを実行する

```
$ ifttt_twitter.py
```

こちらが表示されれば、成功

```
<Response [200]>
```

## 参考情報

- Python を使って『IFTTT（Webhook）』を呼び出す方法
  - https://chasuke.com/python_ifttt/
- IFTTT を使ってブログ更新時に自動で Twitter にシェアする
  - https://qiita.com/donchan922/items/7389a76cc666a5f9d3b4
- 【IFTTT（イフト）が便利すぎる】 web サービスやアプリを連携して自動化できる
  - https://vacks.paid.jp/?p=3800
