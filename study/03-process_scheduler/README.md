## plot_sched.py 実行時のエラー

```s
findfont: Generic family 'sans-serif' not found because none of the following families were found: TakaoPGothic
```

この場合、 font がインストールされていない可能性がある

```s
$ sudo apt install fonts-takao
```

これでインストールした後、 `.cache/matplotlib/fontlist-v330.json` などのキャッシュファイルを削除してもう一度実行してみること