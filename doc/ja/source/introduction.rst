はじめに
================================

ODAT-SEとは
--------------------------------

ODAT-SEは、順問題ソルバーに対して探索アルゴリズムを適用して最適解を探すためのフレームワークです。
順問題ソルバーはユーザー自身で定義できるほか、標準的な順問題ソルバーとして2次元物質構造解析向け実験データ解析ソフトウェアが用意されています。
順問題ソルバーでは、原子位置などをパラメータとして得られたデータと実験データとのずれを損失関数として与えます。
探索アルゴリズムによりこの損失関数を最小化する最適なパラメータを推定します。
現バージョンでは、順問題ソルバーとして量子ビーム回折実験の全反射高速陽電子回折法(Total-Reflection High-Energy Positron Diffraction: TRHEPD), 表面X線回折法(Surface X-ray Diffraction: SXRD), 低速電子線回折法(Low Energy Electron Diffraction: LEED)に対応しており、
探索アルゴリズムはNelder-Mead法, グリッド型探索法, ベイズ最適化, レプリカ交換モンテカルロ法, ポピュレーションアニーリングモンテカルロ法が実装されています。


odatse-XAFSとは
--------------------------------

偏光全反射蛍光 X線吸収微細構造解析 (Polarization-dependent Total Reflection Fluorescence X-ray Absorption Fine Structure: PTRF-XAFS) は、X線吸収スペクトルから得られる吸収原子の対称性や電子状態などを用いて物質構造解析を行う手法で、X線吸収原子の周りに存在する原子の座標を得ることができます。特に全反射法を適用することにより表面の構造解析に有効な方法です。

X線スペクトル解析のための第一原理計算ソフトウェアとして FEFF [1,2]が開発されています。原子位置を入力としてX線分光スペクトルの理論予測を行うプログラムで、Fortran で書かれており、標準的な Linux 環境で動作します。
odatse-XAFS は、この FEFF を ODAT-SE の順問題ソルバとして利用するためのアダプタライブラリです。2DMAT v2.x の順問題ソルバーの一つとして開発されたコンポーネントを、独立なモジュールとして再構成したものです。ODAT-SE および FEFF と組み合わせて使用します。

[1] Ab initio theory and calculation of X-ray spectra, J. J. Rehr, J. J. Kas, M. P. Prange, A. P. Sorini, Y. Takimoto, F. D. Vila, `Comptes Rendus Physique 10 (6) 548-559 (2009) <https://doi.org/10.1016/j.crhy.2008.08.004>`_.

[2] Theoretical Approaches to X-ray Absorption Fine Structure, J. J. Rehr and R. C. Albers, `Rev. Mod. Phys. 72, 621 (2000) <https://doi.org/10.1103/RevModPhys.72.621>`_.


ライセンス
--------------------------------
| 本ソフトウェアのプログラムパッケージおよびソースコード一式はGNU
  General Public License version 3 (GPL v3) に準じて配布されています。

Copyright (c) <2025-> The University of Tokyo. All rights reserved.

本ソフトウェアは2024年度 東京大学物性研究所 ソフトウェア高度化プロジェクトの支援を受け開発されました。
2DMAT / ODAT-SEを引用する際には以下の文献を引用してください。

"Data-analysis software framework 2DMAT and its application to experimental measurements for two-dimensional material structures", Y. Motoyama, K. Yoshimi, I. Mochizuki, H. Iwamoto, H. Ichinose, and T. Hoshi, `Computer Physics Communications 280, 108465 (2022) <https://doi.org/10.1016/j.cpc.2022.108465>`_.

Bibtex::

  @article{MOTOYAMA2022108465,
    title = {Data-analysis software framework 2DMAT and its application to experimental measurements for two-dimensional material structures},
    journal = {Computer Physics Communications},
    volume = {280},
    pages = {108465},
    year = {2022},
    issn = {0010-4655},
    doi = {https://doi.org/10.1016/j.cpc.2022.108465},
    url = {https://www.sciencedirect.com/science/article/pii/S0010465522001849},
    author = {Yuichi Motoyama and Kazuyoshi Yoshimi and Izumi Mochizuki and Harumichi Iwamoto and Hayato Ichinose and Takeo Hoshi}
  }



バージョン履歴
--------------------------------

odatse-XAFS

- v1.0.0 : 2025-04-07

  
主な開発者
--------------------------------

odatse-XAFS は以下のメンバーで開発しています.

- odatse-XAFS v1.0.0 -

  - 本山 裕一 (東京大学 物性研究所)
  - 吉見 一慶 (東京大学 物性研究所)
  - 青山 龍美 (東京大学 物性研究所)
  - 中野 陽斗 (核融合科学研究所)
  - 星 健夫　 (核融合科学研究所)
