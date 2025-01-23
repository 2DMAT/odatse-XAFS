ユーザープログラムによる解析
================================

ここでは、odatse-XAFS モジュールを用いたユーザプログラムを作成し、解析を行う方法を説明します。逆問題アルゴリズムは例としてNelder-Mead法を用います。


サンプルファイルの場所
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
サンプルファイルは ``sample/user_program`` にあります。
フォルダには以下のファイルが格納されています。

- ``simple.py``

  メインプログラム。パラメータを ``input.toml`` ファイルから読み込んで解析を行う。

- ``input.toml``

  ``simple.py`` で利用する入力パラメータファイル

- ``mock_data.txt``, ``template.txt``

  メインプログラムでの計算を進めるための参照ファイル

- ``ref.txt``

  本チュートリアルで求めたい回答が記載されたファイル

- ``prepare.sh`` , ``do.sh``

  本チュートリアルを一括計算するために準備されたスクリプト

以下、これらのファイルについて説明したのち、実際の計算結果を紹介します。

  
プログラムの説明
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``simple.py`` は odatse-XAFS モジュールを用いて解析を行うシンプルなプログラムです。
プログラムの全体を以下に示します。

.. code-block:: python

    import numpy as np

    import odatse
    import odatse.algorithm.min_search
    from odatse.extra.XAFS import Solver

    info = odatse.Info.from_file("input.toml")

    solver = Solver(info)
    runner = odatse.Runner(solver, info)
    alg = odatse.algorithm.min_search.Algorithm(info, runner)
    alg.main()

プログラムではまず、必要なモジュールを import します。

- ODAT-SE のメインモジュール ``odatse``

- 今回利用する逆問題解析アルゴリズム ``odatse.algorithm.min_search``

- 順問題ソルバーモジュール ``odatse.extra.XAFS``

次に、解析で利用するクラスのインスタンスを作成します。

- ``odatse.Info`` クラス

  パラメータを格納するクラスです。 ``from_file`` クラスメソッドに TOML ファイルのパスを渡して作成することができます。

- ``odatse.extra.XAFS.Solver`` クラス

  odatse-XAFS モジュールの順問題ソルバーです。Info クラスのインスタンスを渡して作成します。

- ``odatse.Runner`` クラス

  順問題ソルバーと逆問題解析アルゴリズムを繋ぐクラスです。Solver クラスのインスタンスおよび Info クラスのパラメータを渡して作成します。

- ``odatse.algorithm.min_search.Algorithm`` クラス

  逆問題解析アルゴリズムのクラスです。ここでは Nelder-Mead法による最適化アルゴリズムのクラスモジュール ``min_search`` を利用します。Runner のインスタンスを渡して作成します。

Solver, Runner, Algorithm の順にインスタンスを作成した後、Algorithm クラスの ``main()`` メソッドを呼んで解析を行います。
  

入力ファイルの説明
~~~~~~~~~~~~~~~~~~~
メインプログラム用の入力ファイル ``input.toml`` は前述のグリッド探索法による最適化で用いたのとほぼ同じファイルを利用できます。
``algorithm.param`` セクションには探索範囲 ``min_list``, ``max_list`` と初期値 ``initial_list`` を指定します。
なお、アルゴリズムの種類を指定する ``algorithm.name`` パラメータの値は無視されます。

その他、入力ファイルのテンプレートや測定データファイルは前述の tutorial と同様です。


計算実行
~~~~~~~~~~~~

最初にサンプルファイルが置いてあるフォルダへ移動します(以下、本ソフトウェアをダウンロードしたディレクトリ直下にいることを仮定します).

.. code-block::

    $ cd sample/user_program

``feff85L`` をコピーします。

.. code-block::

    $ cp ../../feff8.5light/build/feff85L .

メインプログラムを実行します。(計算時間は通常のPCで数分程度で終わります)

.. code-block::

    $ python3 simple.py | tee log.txt

実行すると、以下の様な出力がされます。

.. code-block::

    name            : minsearch
    label_list      : ['x_S', 'y_S', 'z_S']
    param.min_list  : [-2.0, -2.0, -2.0]
    param.max_list  : [2.0, 2.0, 2.0]
    param.initial_list: [1.12, 0.96, -1.57]
    value_01 = 1.12000000
    value_02 = 0.96000000
    value_03 = -1.57000000
    R-factor = 0.600274737286056 Polarization [0.0, 1.0, 0.0] R-factor1 = 0.351331393471473  Polarization [1.0, 0.0, 0.0] R-factor2 = 0.7068794828810981  Polarization [0.0, 0.0, 1.0] R-factor3 = 0.7426133355055966 
    remove directory: Log00000000_00000000
    value_01 = 1.12000000
    value_02 = 0.96000000
    value_03 = -1.57000000
    R-factor = 0.600274737286056 Polarization [0.0, 1.0, 0.0] R-factor1 = 0.351331393471473  Polarization [1.0, 0.0, 0.0] R-factor2 = 0.7068794828810981  Polarization [0.0, 0.0, 1.0] R-factor3 = 0.7426133355055966 
    remove directory: Log00000001_00000000
    value_01 = 1.37000000
    value_02 = 0.96000000
    value_03 = -1.57000000
    R-factor = 4.784551806438849 Polarization [0.0, 1.0, 0.0] R-factor1 = 1.3408785150447546  Polarization [1.0, 0.0, 0.0] R-factor2 = 2.312170159259668  Polarization [0.0, 0.0, 1.0] R-factor3 = 10.700606745012124 
    remove directory: Log00000002_00000000
    value_01 = 1.12000000
    value_02 = 1.21000000
    value_03 = -1.57000000
    R-factor = 4.117191586678408 Polarization [0.0, 1.0, 0.0] R-factor1 = 1.8602662077424392  Polarization [1.0, 0.0, 0.0] R-factor2 = 1.3907386197304963  Polarization [0.0, 0.0, 1.0] R-factor3 = 9.100569932562289 
    remove directory: Log00000003_00000000
    value_01 = 1.12000000
    value_02 = 0.96000000
    value_03 = -1.32000000
    R-factor = 9.423169910838718 Polarization [0.0, 1.0, 0.0] R-factor1 = 3.3998266834700908  Polarization [1.0, 0.0, 0.0] R-factor2 = 7.455741765410984  Polarization [0.0, 0.0, 1.0] R-factor3 = 17.41394128363508 
    remove directory: Log00000004_00000000
    ...

``value_01``, ``value_02``, ``value_03`` に各ステップでの候補パラメータと、その時の ``R-factor`` が出力されます。
また各ステップでの計算結果は ``output/0/LogXXXX_YYYY`` (XXXX, YYYYはステップ数)のフォルダに出力されます。
最終的に推定されたパラメータは、 ``output/res.dat`` に出力されます。今の場合、

.. code-block::

    fx = 0.5882857603777499
    x_S = 1.152284911047407
    y_S = 0.931495559770223
    z_S = -1.5710799186906792

となります。リファレンス ref.txt が再現されていることが分かります。

なお、一連の計算を行う ``do.sh`` スクリプトが用意されています。
