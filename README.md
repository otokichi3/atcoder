# AtCoder

入水（生きる）したい

# atcoder-tools をPyPy向けに改造

[atcoder-tools](https://github.com/kyuridenamida/atcoder-tools)でファイルの作成、テストおよび提出を行う。ただしPyPyには対応していないため、PyPyを使いたければインストールしたファイルの一部を編集する必要がある。

変更ファイルのディレクトリは以下の通り確認できる。

```sh
$ pip3 show atcoder-tools | grep Location
Location: /home/otokichi3/.local/lib/python3.10/site-packages
```

対象ファイルは `language.py` で、私の場合は以下にある。

```
/home/otokichi3/.local/lib/python3.10/site-packages/atcodertools/common/language.py`
```

変更の方法として、提出言語を選択する正規表現の先頭にPyPyを無理やり持ってくる。ただしこのやり方は以下の点に留意する必要がある

- atcoder-toolsの更新時に元に戻る（きっとCPythonで提出することになる）
- プルダウンの言語名変更時に提出できなくなる

なのでこまめに変更が必要。

```diff
   122  PYTHON = Language(
   123      name="python",
   124      display_name="Python",
   125      extension="py",
+  126      submission_lang_pattern=re.compile(".*Python \\(PyPy.*|.*Python \\(CPython 3.*"),
-  127      submission_lang_pattern=re.compile(".*Python \\(3.*|.*Python \\(CPython 3.*"),
   128      default_code_generator=python.main,
   129      default_template_path=get_default_template_path('py'),
   130      compile_command="python3 -mpy_compile {filename}.py",
   131      test_command="python3 {filename}.py",
   132      exec_filename="{filename}.pyc"
   133  )
```
