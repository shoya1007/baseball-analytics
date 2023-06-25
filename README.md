## このリポジトリは？
野球データを分析してその結果のグラフの画像を返すAPI。
現時点ではサンプル程度なので大谷翔平の2023シーズンの6/2までの登板時に投げた球種とその変化量を表すグラフを描画することができる。

## データソースについて
csvファイルを読み込んでグラフを描画している。
csvファイルは[MLB公式のデータサイト](https://baseballsavant.mlb.com/statcast_search)から任意の選手を指定してダウンロードすることができる。

## 描画されるグラフの見方
マウンド目線での変化量を表す。
グラフのx軸は横の変化量(pfx_x)、y軸は縦の変化量(pfx_z)を表す。
つまり、横方向については負の値がスライド方向、正の値がシュート方向になる。(大谷が右投げであるため。)

## 実行方法
以下のコマンドを実行
```
$ pipenv shell
$ python app.py
```