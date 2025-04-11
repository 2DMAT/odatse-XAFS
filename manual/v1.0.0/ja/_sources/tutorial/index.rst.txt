.. 2dmat documentation master file, created by
   sphinx-quickstart on Tue May 26 18:44:52 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

チュートリアル
==================================

順問題ソルバーとして用意されている ``odatse-XAFS`` は、University of Washington の J. J. Rehr らにより開発された FEFF を ODAT-SE フレームワークで利用するためのモジュールです。
FEFF は XAFS などの X線分光スペクトルの理論予測を行うプログラムで、原子位置などのパラメータに対して多重散乱による第一原理計算を行いスペクトルを計算します。これを原子位置から分光スペクトルへの順問題としたとき、実験で得られたスペクトルを再現するように原子位置を推定する逆問題を考えます。
ODAT-SEでは、逆問題を解くためのアルゴリズムとして、以下の5つのアルゴリズムが用意されています。

- ``minsearch``

  Nelder-Mead法

- ``mapper_mpi``

  与えられたパラメータの探索グリッドを全探索

- ``bayes``

  ベイズ最適化

- ``exchange``

  レプリカ交換モンテカルロ法

- ``pamc``

  ポピュレーションアニーリング法

本チュートリアルでは、最初に順問題プログラム ``FEFF`` の実行方法を説明した後、 ``mapper_mpi`` による逆問題解析の実行方法について説明します。
以下では odatse-XAFS に付属の ``odatse-XAFS`` プログラムを利用し、TOML形式のパラメータファイルを入力として解析を実行します。

チュートリアルの最後に、ユーザープログラムの項で、メインプログラムを自分で作成して使う方法を minsearch を例に説明します。

.. toctree::
   :maxdepth: 1

   feff
   mapper
   user_program
