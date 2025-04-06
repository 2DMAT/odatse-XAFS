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

    $ cp ../feff/feff85L .

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
    R-factor = 0.7762817472030608 Polarization [0.0, 1.0, 0.0] R-factor1 = 0.26218705791753616  Polarization [1.0, 0.0, 0.0] R-factor2 = 0.3520528886264926  Polarization [0.0, 0.0, 1.0] R-factor3 = 1.7146052950651536 
    value_01 = 1.12000000
    value_02 = 0.96000000
    value_03 = -1.57000000
    R-factor = 0.7762817472030608 Polarization [0.0, 1.0, 0.0] R-factor1 = 0.26218705791753616  Polarization [1.0, 0.0, 0.0] R-factor2 = 0.3520528886264926  Polarization [0.0, 0.0, 1.0] R-factor3 = 1.7146052950651536 
    value_01 = 1.37000000
    value_02 = 0.96000000
    value_03 = -1.57000000
    R-factor = 7.006992151846735 Polarization [0.0, 1.0, 0.0] R-factor1 = 2.097374935360426  Polarization [1.0, 0.0, 0.0] R-factor2 = 3.7994697622892972  Polarization [0.0, 0.0, 1.0] R-factor3 = 15.124131757890481 
    value_01 = 1.12000000
    value_02 = 1.21000000
    value_03 = -1.57000000
    R-factor = 5.73016510319226 Polarization [0.0, 1.0, 0.0] R-factor1 = 3.5024285153919115  Polarization [1.0, 0.0, 0.0] R-factor2 = 2.0041674778416843  Polarization [0.0, 0.0, 1.0] R-factor3 = 11.683899316343183 
    value_01 = 1.12000000
    value_02 = 0.96000000
    value_03 = -1.32000000
    R-factor = 56.31862514558586 Polarization [0.0, 1.0, 0.0] R-factor1 = 6.4008790163862015  Polarization [1.0, 0.0, 0.0] R-factor2 = 9.109651695414557  Polarization [0.0, 0.0, 1.0] R-factor3 = 153.44534472495684 
    value_01 = 1.28666667
    value_02 = 1.12666667
    value_03 = -1.82000000
    R-factor = 32.91890925644038 Polarization [0.0, 1.0, 0.0] R-factor1 = 2.2301127998431753  Polarization [1.0, 0.0, 0.0] R-factor2 = 5.050496886392638  Polarization [0.0, 0.0, 1.0] R-factor3 = 91.47611808308534 
    value_01 = 1.24500000
    value_02 = 1.08500000
    value_03 = -1.69500000
    R-factor = 14.218592101199897 Polarization [0.0, 1.0, 0.0] R-factor1 = 3.3863023885318193  Polarization [1.0, 0.0, 0.0] R-factor2 = 5.0060964449177945  Polarization [0.0, 0.0, 1.0] R-factor3 = 34.26337747015008 
    eval: x=[ 1.12  0.96 -1.57], fun=0.7762817472030608
    value_01 = 1.16166667
    value_02 = 1.00166667
    value_03 = -1.44500000
    R-factor = 7.048842595863635 Polarization [0.0, 1.0, 0.0] R-factor1 = 1.224939069135288  Polarization [1.0, 0.0, 0.0] R-factor2 = 1.8540984688270858  Polarization [0.0, 0.0, 1.0] R-factor3 = 18.06749024962853 
    value_01 = 1.18250000
    value_02 = 1.02250000
    value_03 = -1.50750000
    R-factor = 0.4469433592171206 Polarization [0.0, 1.0, 0.0] R-factor1 = 0.2535379790399123  Polarization [1.0, 0.0, 0.0] R-factor2 = 0.20069518356682897  Polarization [0.0, 0.0, 1.0] R-factor3 = 0.8865969150446205 
    eval: x=[ 1.1825  1.0225 -1.5075], fun=0.4469433592171206
    ...

        
``value_01``, ``value_02``, ``value_03`` に各ステップでの候補パラメータと、その時の ``R-factor`` が出力されます。
また各ステップでの計算結果は ``output/0/LogXXXX_YYYY`` (XXXX, YYYYはステップ数)のフォルダに出力されます。
最終的に推定されたパラメータは、 ``output/res.dat`` に出力されます。今の場合、

.. code-block::

    fx = 0.20606977805890725
    x_S = 1.125299780290939
    y_S = 0.9597181918334485
    z_S = -1.596967599355829

となります。リファレンス ref.txt が再現されていることが分かります。

なお、一連の計算を行う ``do.sh`` スクリプトが用意されています。
