odatse-XAFS のインストール
================================================================

実行環境・必要なパッケージ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- python 3.9 以上

    - 必要なpythonパッケージ

        - numpy (>= 1.14)
        - pydantic (>= 2.0)

- ODAT-SE version 3.0 以降

- FEFF 8.5light または version 9以降(有償版)


ダウンロード・インストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. ODAT-SE をインストールする

   - ソースコードからのインストール

     リポジトリから ODAT-SE のソースファイルを取得します。

     .. code-block:: bash

	$ git clone https://github.com/issp-center-dev/ODAT-SE.git

     pip コマンドを実行してインストールします。

     .. code-block:: bash

	$ cd ODAT-SE
	$ python3 -m pip install .

	
     ``--user`` オプションを付けるとローカル (``$HOME/.local``) にインストールできます。
	
     ``python3 -m pip install .[all]`` を実行するとオプションのパッケージも同時にインストールします。
	
2. FEFF をインストールする

   - 配布サイトからソースコードを取得し、コンパイルします。

     - コードの取得:

       .. code-block:: bash

          $ git clone https://github.com/eucall-software/feff8.5light.git
          $ cd feff8.5light
          $ mkdir build && cd build

     - GCC (gfortran) の場合はコンパイラオプションを指定してビルドする必要があります。
	
       .. code-block:: bash

          $ cmake -DCMAKE_Fortran_FLAGS="-fallow-argument-mismatch -std=legacy" ..
          $ make

     - intel compiler (ifort) の場合は次のようにコンパイラを指定してビルドします。

       .. code-block:: bash

          $ cmake -DCMAKE_Fortran_COMPILER=ifort ..
          $ make

     ビルドに成功すると実行形式 ``feff85L`` が作成されます。
     ``feff85L`` を PATH の通ったディレクトリ (環境変数 PATH に列挙された、実行プログラムを探索するディレクトリ) に配置するか、実行時にディレクトリ名をつけて指定します。

3. odatse-XAFS をインストールする

   - ソースコードからのインストール

     odatse-XAFS のソースファイルは GitHub リポジトリから取得できます。以下の手順でリポジトリをクローンした後、pip コマンドを実行してインストールします。

     .. code-block:: bash

        $ git clone https://github.com/2DMAT/odatse-XAFS.git
	$ cd odatse-XAFS
	$ python3 -m pip install .

     ``--user`` オプションを付けるとローカル (``$HOME/.local``) にインストールできます。
	
     odatse-XAFS のライブラリと、実行コマンド ``odatse-XAFS`` がインストールされます。


実行方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ODAT-SE では順問題ソルバと逆問題解析アルゴリズムを組み合わせて解析を行います。
XAFSの解析を行うには次の2通りの方法があります。

1. このパッケージに含まれる odatse-XAFS プログラムを利用して解析を行います。ユーザは、プログラムの入力となるパラメータファルを TOML 形式で作成し、プログラムの引数に指定してコマンドを実行します。逆問題解析のアルゴリズムはパラメータで選択できます。

2. odatse-XAFS ライブラリと ODAT-SE フレームワークを用いてプログラムを作成し、解析を行います。逆問題解析アルゴリズムは import するモジュールで選択します。プログラム中に入力データの生成を組み込むなど、柔軟な使い方ができます。

パラメータの種類やライブラリの利用方法については以降の章で説明します。


アンインストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

odatse-XAFS モジュールおよび ODAT-SE モジュールをアンインストールするには、以下のコマンドを実行します。

.. code-block:: bash

    $ python3 -m pip uninstall odatse-XAFS ODAT-SE
