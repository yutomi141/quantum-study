#!/usr/bin/env python
# coding: utf-8

# {/* cspell:ignore operatorname */}
# 
# 

# <span id="quantum-information" />
# 
# # 量子情報
# 
# さて、量子情報の話に移ろう。そこでは、考えている系の状態（この場合は*量子状態* ）を表すベクトルの種類を別のものにする。
# 前回の古典的情報の議論と同様、ここでは有限で空でない古典的状態の集合を持つシステムを扱う。
# 
# <span id="quantum-state-vectors" />
# 
# ## 量子状態ベクトル
# 
# システムの*量子状態は*、確率的状態と同様に列ベクトルで表される。 先ほどと同様、ベクトルの添字はシステムの古典的な状態を示す。
# 量子状態を表すベクトルは、この2つの性質によって特徴づけられる：
# 
# 1.  量子状態ベクトルのエントリーは*複素数*である。
# 2.  量子状態ベクトルのエントリーの*絶対値の二乗*和は次のようになる。 $1.$
# 
# したがって、確率的な状態とは対照的に、量子状態を表すベクトルは非負の実数エントリを持つ必要はなく、エントリの絶対値の2乗の和（エントリの和ではなく）が等しくなければならない。 $1.$。このような単純な変化が、量子情報と古典情報の違いを生み出している。量子コンピュータの高速化や量子通信プロトコルの改善は、結局のところ、このような単純な数学的変化に由来する。
# 
# 列ベクトルの*ユークリッド・ノルム*
# 
# $$
#   v = \begin{pmatrix}
#     \alpha_1\\
#     \vdots\\
#     \alpha_n
#   \end{pmatrix}
# $$
# 
# は以下のように定義される：
# 
# $$
#   \| v \| = \sqrt{\sum_{k=1}^n |\alpha_k|^2}.
# $$
# 
# 量子状態ベクトルの絶対値の2乗の和が $1$ に等しいという条件は、そのベクトルが次のユークリッドノルムを持つことと等価である。 $1.$ つまり、量子状態ベクトルはユークリッドノルムに関して*単位ベクトル*である。
# 
# <span id="examples-of-qubit-states" />
# 
# ### 量子ビット状態の例
# 
# *量子ビット（qubit* ）という用語は、古典的な状態集合が次のような量子系を指す。 $\{0,1\}.$ つまり、qubitは実際には単なるビットであるが、この名前を使うことで、このビットが量子状態になりうることを明確に認識することができる。
# 
# これらは量子ビットの量子状態の例である：
# 
# $$
#   \begin{pmatrix}
#     1\\[2mm]
#     0
#   \end{pmatrix}
#   = \vert 0\rangle
#   \quad\text{and}\quad
#   \begin{pmatrix}
#     0\\[2mm]
#     1
#   \end{pmatrix}
#   = \vert 1\rangle,
# $$
# 
# $$
#   \begin{pmatrix}
#     \frac{1}{\sqrt{2}}\\[2mm]
#     \frac{1}{\sqrt{2}}
#   \end{pmatrix}
#   = \frac{1}{\sqrt{2}}\,\vert 0\rangle + \frac{1}{\sqrt{2}}\,\vert 1\rangle,
#   \tag{1}
# $$
# 
# および
# 
# $$
#   \begin{pmatrix}
#     \frac{1+2i}{3}\\[2mm]
#     -\frac{2}{3}
#   \end{pmatrix}
#   = \frac{1+2i}{3}\,\vert 0\rangle - \frac{2}{3}\,\vert 1\rangle.
# $$
# 
# 最初の2つの例、 $\vert 0\rangle$ と $\vert 1\rangle,$ は、標準的な基底要素が有効な量子状態ベクトルであることを示している。それらのエントリは複素数であり、これらの数の虚部はすべて偶然にも $0,$、エントリの絶対値の2乗の和を計算すると次のようになる
# 
# $$
#   \vert 1\vert^2 + \vert 0\vert^2 = 1
#   \quad\text{and}\quad
#   \vert 0\vert^2 + \vert 1\vert^2 = 1,
# $$
# 
# ください。
# 古典的な設定と同様に、量子状態ベクトル $\vert 0\rangle$、 $\vert 1\rangle$、量子ビットがそれぞれ古典状態 $0$、 $1,$。
# 
# 他の2つの例では、やはり複素数のエントリーがあり、エントリーの絶対値の2乗の和を計算すると、次のようになる
# 
# $$
#   \biggl\vert\frac{1}{\sqrt{2}}\biggr\vert^2 +
#   \biggl\vert\frac{1}{\sqrt{2}}\biggr\vert^2 = \frac{1}{2} + \frac{1}{2} = 1
# $$
# 
# および
# 
# $$
#   \biggl\vert \frac{1+2i}{3} \biggr\vert^2 +
#   \biggl\vert -\frac{2}{3} \biggr\vert^2 = \frac{5}{9} + \frac{4}{9} = 1.
# $$
# 
# したがって、これらは有効な量子状態ベクトルである。 これらは標準基底状態 $\vert 0 \rangle$ と $\vert 1 \rangle,$ の線形結合であることに注意してください。このため、私たちはしばしばこれらの状態を $0$ と の*重ね合わせだと*言います。 $1.$ 量子状態の文脈では、 *重ね合わせと* *線形結合は*本質的に同義である。
# 
# 上記の量子ビット状態ベクトルの例（ $(1)$ ）は、非常によく遭遇するもので、 *プラス状態と*呼ばれ、次のように表記される：
# 
# $$
#   \vert {+} \rangle = \frac{1}{\sqrt{2}} \vert 0\rangle + \frac{1}{\sqrt{2}} \vert 1\rangle.
# $$
# 
# また、以下の表記も使用する
# 
# $$
#   \vert {-} \rangle = \frac{1}{\sqrt{2}} \vert 0\rangle - \frac{1}{\sqrt{2}} \vert 1\rangle
# $$
# 
# この状態を*マイナス状態と*呼ぶ。
# 
# 古典的な状態を指す記号以外の記号がケットの中に現れる、このような表記法は一般的である。
# 標準的な基底ベクトルとは限らない任意のベクトルを指すために、 $\psi,$ の代わりに $\vert\psi\rangle,$ という表記や別の名前を使うことはよくある。
# 
# ベクトル $\vert \psi \rangle$ の添字が古典状態集合 $\Sigma,$ に対応し、 $a\in\Sigma$ がこの古典状態集合の要素である場合、行列積 $\langle a\vert \vert \psi\rangle$ は、添字が $\vert \psi \rangle$ に対応するベクトルのエントリーに等しいことに注意。 $a.$ $\vert \psi \rangle$ が標準基底ベクトルであったときと同様、読みやすくするために、 $\langle a \vert \psi \rangle$ と表記する。 $\langle a\vert \vert \psi\rangle$ と表記する。
# 
# 例えば、 $\Sigma = \{0,1\}$
# 
# $$
# \vert \psi \rangle =
# \frac{1+2i}{3} \vert 0\rangle - \frac{2}{3} \vert 1\rangle
# = \begin{pmatrix}
#     \frac{1+2i}{3}\\[2mm]
#     -\frac{2}{3}
#   \end{pmatrix},
#   \tag{2}
# $$
# 
# その場合
# 
# $$
#   \langle 0 \vert \psi \rangle = \frac{1+2i}{3}
#   \quad\text{and}\quad
#   \langle 1 \vert \psi \rangle = -\frac{2}{3}.
# $$
# 
# 一般に、任意のベクトルに対してディラック表記法を用いる場合、 $\langle \psi \vert$ という表記は、列ベクトルから行ベクトルへベクトルを転置し、各エントリーをその複素共役で置き換えた列ベクトル $\vert\psi\rangle,$ の*共役転置を*とることによって得られる行ベクトルを指す。
# 例えば、 $\vert\psi\rangle$ が $(2),$ で定義されたベクトルである場合、次のようになる
# 
# $$
# \langle\psi\vert = \frac{1-2i}{3} \langle 0\vert - \frac{2}{3} \langle 1\vert
# = \begin{pmatrix}
#     \frac{1-2i}{3} &
#     -\frac{2}{3}
#   \end{pmatrix}.
# $$
# 
# 転置に加えて複素共役を取る理由は、後で内積について詳しく説明する。
# 
# <span id="quantum-states-of-other-systems" />
# 
# ### 他の系の量子状態
# 
# 任意の古典的状態集合を持つ系の量子状態を考えることができる。
# 例えば、扇風機のスイッチの量子状態ベクトルである：
# 
# $$
#   \begin{pmatrix}
#     \frac{1}{2}\\[1mm]
#     0 \\[1mm]
#     -\frac{i}{2}\\[1mm]
#     \frac{1}{\sqrt{2}}
#   \end{pmatrix}
#   = \frac{1}{2} \vert\mathrm{high}\rangle
#   - \frac{i}{2} \vert\mathrm{low}\rangle
#   + \frac{1}{\sqrt{2}} \vert\mathrm{off}\rangle.
# $$
# 
# ここでの仮定は、古典的な状態は*高*、 *中*、 *低、* *オフの*順に並ぶというものだ。
# 扇風機のスイッチの量子状態を考えたい特別な理由はないかもしれないが、原理的には可能である。
# 
# もうひとつ例を挙げよう。古典的な状態が次のような量子10進数である場合だ。 $0, 1, \ldots, 9:$
# 
# $$
#   \frac{1}{\sqrt{385}}
#   \begin{pmatrix}
#     1\\
#     2\\
#     3\\
#     4\\
#     5\\
#     6\\
#     7\\
#     8\\
#     9\\
#     10
#   \end{pmatrix}
#   =
#   \frac{1}{\sqrt{385}}\sum_{k = 0}^9 (k+1) \vert k \rangle.
# $$
# 
# この例は、ディラック記法を用いて状態ベクトルを書くことの利便性を示している。
# この特殊な例では、列ベクトル表現は単に面倒なだけだが、もし古典的な状態が大幅に増えれば、使い物にならなくなるだろう。
# これに対してディラック記法は、大きくて複雑なベクトルをコンパクトな形で正確に記述することができる。
# 
# ディラック記法はまた、ベクトルのさまざまな側面が*不確定である、* つまり未知である、あるいはまだ確立されていないベクトルを表現することもできる。
# 例えば、任意の古典状態集合 $\Sigma,$ に対して、量子状態ベクトルを考えることができる
# 
# $$
#   \frac{1}{\sqrt{|\Sigma|}} \sum_{a\in\Sigma} \vert a \rangle,
# $$
# 
# ここで、 $\vert\Sigma\vert$ という表記は、 の要素の数を表している。 $\Sigma.$ の古典的状態に対する*一様な重ね合わせである*。 $\Sigma.$
# 
# この後のレッスンでは、列ベクトルを使用することが現実的でない、あるいは不可能な、より複雑な量子状態ベクトルの表現に出会うことになる。
# 実際、ステート・ベクトルの列ベクトル表現については、少数のエントリーを持つベクトル（多くの場合、例題の文脈で使われる）を除き、そのほとんどを放棄する。
# 
# ディラック記法を用いて状態ベクトルを表現するのが便利なもう一つの理由がここにある。それは、古典的状態の順序（あるいは、等価的に、古典的状態とベクトル・インデックスの対応関係）を明示的に指定する必要がなくなるからだ。
# 
# 例えば、以下のような古典的な状態セットを持つシステムの量子状態ベクトル。 $\{\clubsuit,\diamondsuit,\heartsuit,\spadesuit\},$ 例えば
# 
# $$
#     \frac{1}{2} \vert\clubsuit\rangle
#   + \frac{i}{2} \vert\diamondsuit\rangle
#   - \frac{1}{2} \vert\heartsuit\rangle
#   - \frac{i}{2} \vert\spadesuit\rangle,
# $$
# 
# この式を理解するために、この古典的状態集合の順序を選んだり指定したりする必要はない。
# この場合、標準的なカードのスートの並び順を指定するのは難しいことではない： $\clubsuit,$ $\diamondsuit,$ $\heartsuit,$ $\spadesuit.$ このような順序を選ぶと、上の量子状態ベクトルは列ベクトル
# 
# $$
# \begin{pmatrix}
#  \frac{1}{2}\\[2mm]
#  \frac{i}{2}\\[2mm]
#  -\frac{1}{2}\\[2mm]
#  -\frac{i}{2}
# \end{pmatrix}.
# $$
# 
# しかし、一般的には、古典的な状態セットがどのように並べられるかという問題を単純に無視できるのは便利である。
# 
# <span id="measuring-quantum-states" />
# 
# ## 量子状態の測定
# 
# 次に、量子状態が*測定さ*れたときに何が起こるかを、 *標準基底測定として*知られる単純な測定に焦点を当てて考えてみよう。
# (後ほど述べるが、測定にはもっと一般的な概念がある)
# 
# 確率論的な設定と同様に、量子状態にある系が測定されるとき、測定を行う仮想的な観測者は量子状態のベクトルを見ることはなく、むしろ古典的な状態を見ることになる。
# この意味で、測定は量子情報と古典情報のインターフェースとして機能し、これを通じて量子状態から古典情報が抽出される。
# 
# 量子状態が測定された場合、系の各古典状態は、その古典状態に対応する量子状態ベクトルの*絶対値の2乗に*等しい確率で現れる。
# これは量子力学の*ボルン則として*知られている。
# このルールは、量子状態ベクトルのエントリーの絶対値の2乗の和が $1,$、異なる古典状態の測定結果の確率の和が になることを意味する。 $1.$
# 
# 例えば、プラス状態の測定
# 
# $$
#   \vert {+} \rangle =
#   \frac{1}{\sqrt{2}} \vert 0 \rangle
#   + \frac{1}{\sqrt{2}} \vert 1 \rangle
# $$
# 
# の結果、2つの可能な結果、 $0$ と $1,$ が、確率は以下のようになる。
# 
# $$
#   \operatorname{Pr}(\text{outcome is 0})
#   = \bigl\vert \langle 0 \vert {+} \rangle \bigr\vert^2
#   = \biggl\vert \frac{1}{\sqrt{2}} \biggr\vert^2
#   = \frac{1}{2}
# $$
# 
# $$
#   \operatorname{Pr}(\text{outcome is 1})
#   = \bigl\vert \langle 1 \vert {+} \rangle \bigr\vert^2
#   = \biggl\vert \frac{1}{\sqrt{2}} \biggr\vert^2
#   = \frac{1}{2}
# $$
# 
# 興味深いことに、マイナス状態を測定すると
# 
# $$
#   \vert {-} \rangle =
#   \frac{1}{\sqrt{2}} \vert 0 \rangle
#   - \frac{1}{\sqrt{2}} \vert 1 \rangle
# $$
# 
# の結果は、2つの結果についてまったく同じ確率となる。
# 
# $$
#   \operatorname{Pr}(\text{outcome is 0})
#   = \bigl\vert \langle 0 \vert {-} \rangle \bigr\vert^2
#   = \biggl\vert \frac{1}{\sqrt{2}} \biggr\vert^2
#   = \frac{1}{2}
# $$
# 
# $$
#   \operatorname{Pr}(\text{outcome is 1})
#   = \bigl\vert \langle 1 \vert {-} \rangle \bigr\vert^2
#   = \biggl\vert -\frac{1}{\sqrt{2}} \biggr\vert^2
#   = \frac{1}{2}
# $$
# 
# このことは、標準的な基礎測定に関する限り、プラスとマイナスの状態に違いはないことを示唆している。
# では、なぜ両者を区別する必要があるのか？
# その答えは、次のサブセクションで説明するように、この2つの状態に対して操作が行われたときの挙動が異なるからである。
# 
# もちろん、量子状態（ $\vert 0\rangle$ ）を測定すれば、確実に古典状態（ $0$ ）が得られ、同様に量子状態（ $\vert 1\rangle$ ）を測定すれば、確実に古典状態（ $1$ ）が得られる。
# これは、以前に示唆されたように、システムが対応する古典的な状態に*ある*ことと、これらの量子状態を同一視することと一致する。
# 
# 最後の例として
# 
# $$
#   \vert \psi \rangle = \frac{1+2i}{3} \vert 0\rangle - \frac{2}{3} \vert 1\rangle
# $$
# 
# によって、2つの可能性のある結果が以下のような確率で現れる：
# 
# $$
#   \operatorname{Pr}(\text{outcome is 0})
#   = \bigl\vert \langle 0 \vert \psi \rangle \bigr\vert^2
#   = \biggl\vert \frac{1+2i}{3} \biggr\vert^2
#   = \frac{5}{9},
# $$
# 
# および
# 
# $$
#   \operatorname{Pr}(\text{outcome is 1})
#   = \bigl\vert \langle 1 \vert \psi \rangle \bigr\vert^2
#   = \biggl\vert -\frac{2}{3} \biggr\vert^2
#   = \frac{4}{9}.
# $$
# 
# <span id="unitary-operations" />
# 
# ## ユニタリーオペレーション
# 
# これまでのところ、量子情報が古典情報と根本的に異なる理由は明らかではないかもしれない。
# つまり、量子状態が測定されたとき、それぞれの古典状態が得られる確率は、対応するベクトルのエントリーの絶対値の2乗で与えられる。 ベクトルに記録しておけばよいではないか。
# 
# その答えは、少なくとも部分的には、量子状態に対して実行可能な*操作の*セットが、古典的な情報の場合とは異なるからである。
# しかし、古典的な場合のように確率行列で表現されるのではなく、 *ユニタリー* 行列で表現される。
# 
# 複素数のエントリを持つ正方行列 $U$ は、以下の方程式を満たす場合、 *ユニタリー* である
# 
# $$
#   \begin{aligned}
#     U U^{\dagger} &= \mathbb{I} \\
#     U^{\dagger} U &= \mathbb{I}.
#   \end{aligned}
#   \tag{3}
# $$
# 
# ここで、 $\mathbb{I}$ は恒等行列であり、 $U^{\dagger}$ は $U,$ の*共役転置*である。つまり、 $U$ を転置し、各エントリーの複素共役をとることによって得られる行列を意味する。
# 
# $$
#   U^{\dagger} = \overline{U^T}
# $$
# 
# 上記の2つの等号（ $(3)$ ）のどちらかが真であれば、もう一方も真でなければならない。
# どちらの等式も、 $U^{\dagger}$ の逆数であることと等価である。 $U:$
# 
# $$
#   U^{-1} = U^{\dagger}.
# $$
# 
# (警告： $M$ が正方行列でない場合、例えば $M^{\dagger} M = \mathbb{I}$ と $M M^{\dagger} \neq \mathbb{I},$ が正方行列である可能性がある。
# 上の最初の式における2つの等式の等価性は、正方行列に対してのみ成り立つ)
# 
# $U$ がユニタリーであるという条件は、 $U$ の掛け算がどのベクトルのユークリッドノルムも変えないという条件と等価である。
# すなわち、 $n\times n$ 行列 $U$ は、以下の場合にのみユニタリーである。 $\| U \vert \psi \rangle \| = \|\vert \psi \rangle \|$ 複素数エントリを持つすべての $n$ -次元列ベクトル $\vert \psi \rangle$。
# したがって、すべての量子状態ベクトルの集合は、ユークリッドノルムが $1,$ に等しいベクトルの集合と同じであるため、量子状態ベクトルにユニタリー行列を乗算すると、別の量子状態ベクトルになる。
# 
# 実際、ユニタリー行列は、量子状態ベクトルを常に他の量子状態ベクトルに変換する線形写像の集合である。 ここでは、確率ベクトルを確率ベクトルに変換する確率行列に関連した操作が行われる、古典的な確率論的ケースに似ていることに注目してほしい。
# 
# <span id="examples-of-unitary-operations-on-qubits" />
# 
# ### 量子ビットに対するユニタリー演算の例
# 
# 以下のリストでは、量子ビットに対する一般的なユニタリー演算について説明する。
# 
# 1.  *パウリのオペレーション* つのパウリ行列は以下の通り：
# 
# $$
# \mathbb{I} =
# \begin{pmatrix}
# 1 & 0\\
# 0 & 1
# \end{pmatrix},
# \quad
# \sigma_x =
# \begin{pmatrix}
# 0 & 1\\
# 1 & 0
# \end{pmatrix},
# \quad
# \sigma_y =
# \begin{pmatrix}
# 0 & -i\\
# i & 0
# \end{pmatrix},
# \quad
# \sigma_z =
# \begin{pmatrix}
# 1 & 0\\
# 0 & -1
# \end{pmatrix}.
# $$
# 
# 一般的な代替表記は、 $X = \sigma_x,$ $Y = \sigma_y,$、 $Z = \sigma_z$ （ただし、 $X,$ $Y,$、 $Z$ という文字も他の目的でよく使われるので注意）。 $X$、ビットにこのような作用を引き起こすため、 *ビットフリップ*または *NOT演算とも*呼ばれる：
# 
# $$
# X \vert 0\rangle = \vert 1\rangle
# \quad \text{and} \quad
# X \vert 1\rangle = \vert 0\rangle.
# $$
# 
# $Z$ 操作は*位相反転とも*呼ばれ、次のような作用がある：
# 
# $$
# Z \vert 0\rangle = \vert 0\rangle
# \quad \text{and} \quad
# Z \vert 1\rangle = - \vert 1\rangle.
# $$
# 
# 2.  *ハダマード演算*。 ハダマード演算はこの行列によって記述される：
# 
# $$
# H = \begin{pmatrix}
# \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[2mm]
# \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
# \end{pmatrix}.
# $$
# 
# 3.  *段階的なオペレーション。*  位相操作とは、行列
# 
# $$
# P_{\theta} =
# \begin{pmatrix}
# 1 & 0\\
# 0 & e^{i\theta}
# \end{pmatrix}
# $$
# 
# 任意の実数 $\theta.$ 演算
# 
# $$
# S = P_{\pi/2} =
# \begin{pmatrix}
# 1 & 0\\
# 0 & i
# \end{pmatrix}
# \quad \text{and} \quad
# T = P_{\pi/4} =
# \begin{pmatrix}
# 1 & 0\\
# 0 & \frac{1 + i}{\sqrt{2}}
# \end{pmatrix}
# $$
# 
# は特に重要な例である。 その他の例としては、 $\mathbb{I} = P_0$ や $Z = P_{\pi}.$
# 
# 今定義した行列はすべてユニタリー行列であり、1量子ビットに対する量子演算を表している。
# 例えば、 $H$ がユニタリーであることを検証する計算がある：
# 
# $$
# \begin{pmatrix}
#   \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[2mm]
#   \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
# \end{pmatrix}^{\dagger}
# \begin{pmatrix}
#   \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[2mm]
#   \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
# \end{pmatrix}
# = \begin{pmatrix}
#   \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[2mm]
#   \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
# \end{pmatrix}
# \begin{pmatrix}
#   \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[2mm]
#   \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
# \end{pmatrix}
# = \begin{pmatrix}
#   \frac{1}{2} + \frac{1}{2} & \frac{1}{2} - \frac{1}{2}\\[2mm]
#   \frac{1}{2} - \frac{1}{2} & \frac{1}{2} + \frac{1}{2}
# \end{pmatrix}
# = \begin{pmatrix}
#   1 & 0\\
#   0 & 1
# \end{pmatrix}.
# $$
# 
# そして、よく遭遇するいくつかの量子ビット状態ベクトルに対するハダマード演算の作用は以下の通りである。
# 
# $$
# \begin{aligned}
#   H \vert 0 \rangle & =
#   \begin{pmatrix}
#     \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[2mm]
#     \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
#   \end{pmatrix}
#   \begin{pmatrix}
#     1\\[2mm]
#     0
#   \end{pmatrix}
#   = \begin{pmatrix}
#     \frac{1}{\sqrt{2}}\\[2mm]
#     \frac{1}{\sqrt{2}}
#   \end{pmatrix}
#   = \vert + \rangle\\[6mm]
#   H \vert 1 \rangle
#   & =
#   \begin{pmatrix}
#     \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[2mm]
#     \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
#   \end{pmatrix}
#   \begin{pmatrix}
#     0\\[2mm]
#     1
#   \end{pmatrix}
#   = \begin{pmatrix}
#     \frac{1}{\sqrt{2}}\\[2mm]
#     -\frac{1}{\sqrt{2}}
#   \end{pmatrix}
#   = \vert - \rangle\\[6mm]
#   H \vert + \rangle
#   & =
#   \begin{pmatrix}
#     \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[2mm]
#     \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
#   \end{pmatrix}
#   \begin{pmatrix}
#     \frac{1}{\sqrt{2}}\\[2mm]
#     \frac{1}{\sqrt{2}}
#   \end{pmatrix}
#   = \begin{pmatrix}
#     1\\[2mm]
#     0
#   \end{pmatrix}
#   = \vert 0 \rangle\\[6mm]
#   H \vert - \rangle
#   & =
#   \begin{pmatrix}
#     \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[2mm]
#     \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
#   \end{pmatrix}
#   \begin{pmatrix}
#     \frac{1}{\sqrt{2}}\\[2mm]
#     -\frac{1}{\sqrt{2}}
#   \end{pmatrix}
#   = \begin{pmatrix}
#     0\\[2mm]
#     1
#   \end{pmatrix}
#   = \vert 1 \rangle
# \end{aligned}
# $$
# 
# より簡潔に言えば、以下の4つの方程式が得られる。
# 
# $$
#   \begin{aligned}
#     H \vert 0 \rangle = \vert {+} \rangle & \qquad H \vert {+} \rangle = \vert 0 \rangle \\[1mm]
#     H \vert 1 \rangle = \vert {-} \rangle & \qquad H \vert {-} \rangle = \vert 1 \rangle
#   \end{aligned}
# $$
# 
# $H\vert {+} \rangle = \vert 0\rangle$。 $H\vert {-} \rangle = \vert 1\rangle,$ 前節で示唆された、 $\vert {+} \rangle$ と $\vert {-} \rangle.$
# 
# 量子ビットが2つの量子状態 $\vert {+} \rangle$ と $\vert {-} \rangle,$ の2つの量子状態のうちの1つが用意されているが、それがどちらであるかはわからないという状況を考えてみよう。
# どちらの状態を測定しても、すでに観察したように、もう一方と同じ出力分布が得られる： $0$ と $1$、どちらも同じ確率で現れる。 $1/2,$、2つの状態のどちらが準備されたのかについての情報はまったく得られない。
# 
# しかし、最初にハダマード演算を適用してから測定すると、元の状態が $\vert {+} \rangle,$ ならば、確実に結果 $0$ が得られ、元の状態が $1,$ ならば、再び確実に結果 が得られる。 $\vert {-} \rangle.$ したがって、量子状態 $\vert {+} \rangle$ と $\vert {-} \rangle$ は*完全に*識別できる。
# これにより、符号の変化、より一般的には量子状態ベクトルの複素数エントリーの*位相* （伝統的には*引数とも*呼ばれる）の変化が、その状態を大きく変化させることが明らかになった。
# 
# ここにもう一つの例を挙げ、ハダマード演算が前述の状態ベクトルにどのように作用するかを示す。
# 
# $$
#   H \biggl(\frac{1+2i}{3} \vert 0\rangle - \frac{2}{3} \vert 1\rangle\biggr)
#   = \begin{pmatrix}
#     \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[2mm]
#     \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
#   \end{pmatrix}
#   \begin{pmatrix}
#     \frac{1+2i}{3}\\[2mm]
#     -\frac{2}{3}
#   \end{pmatrix}
#   = \begin{pmatrix}
#     \frac{-1+2i}{3\sqrt{2}}\\[2mm]
#     \frac{3+2i}{3\sqrt{2}}
#   \end{pmatrix}
#   = \frac{-1+2i}{3\sqrt{2}} | 0 \rangle
#   + \frac{3+2i}{3\sqrt{2}} | 1 \rangle
# $$
# 
# 次に、プラス状態に対する $T$。
# 
# $$
#   T \vert {+} \rangle
#   = T \biggl(\frac{1}{\sqrt{2}} \vert 0\rangle + \frac{1}{\sqrt{2}} \vert 1\rangle\biggr)
#   = \frac{1}{\sqrt{2}} T\vert 0\rangle + \frac{1}{\sqrt{2}} T\vert 1\rangle
#   = \frac{1}{\sqrt{2}} \vert 0\rangle + \frac{1+i}{2} \vert 1\rangle
# $$
# 
# ここでは、等価な行列／ベクトル形式にわざわざ変換する必要はなく、行列の乗算の線形性と以下の公式を併用したことに注目されたい
# 
# $$
# T \vert 0\rangle = \vert 0\rangle
# \quad\text{and}\quad
# T \vert 1\rangle = \frac{1 + i}{\sqrt{2}} \vert 1\rangle.
# $$
# 
# 同じように、得られた量子状態ベクトルにハダマード演算を適用した結果を計算することもできる：
# 
# $$
# \begin{aligned}
# H\, \biggl(\frac{1}{\sqrt{2}} \vert 0\rangle + \frac{1+i}{2} \vert 1\rangle\biggr)
# & = \frac{1}{\sqrt{2}} H \vert 0\rangle + \frac{1+i}{2} H \vert 1\rangle\\
# & = \frac{1}{\sqrt{2}} \vert +\rangle + \frac{1+i}{2} \vert -\rangle \\
# & = \biggl(\frac{1}{2} \vert 0\rangle + \frac{1}{2} \vert 1\rangle\biggr)
# + \biggl(\frac{1+i}{2\sqrt{2}} \vert 0\rangle - \frac{1+i}{2\sqrt{2}} \vert 1\rangle\biggr)\\
# & = \biggl(\frac{1}{2} + \frac{1+i}{2\sqrt{2}}\biggr) \vert 0\rangle
# + \biggl(\frac{1}{2} - \frac{1+i}{2\sqrt{2}}\biggr) \vert 1\rangle.
# \end{aligned}
# $$
# 
# 明示的に行列表現に変換するアプローチと、線形性を利用して標準基底状態に対する演算の作用をプラグインするアプローチの2つは等価である。
# どちらか都合のいい方を使えばいい。
# 
# <span id="compositions-of-qubit-unitary-operations" />
# 
# ### 量子ビット単位演算の構成
# 
# ユニタリー演算の合成は、確率的設定と同じように行列の乗算で表現される。
# 
# 例えば、最初にハダマード演算を適用し、次に $S$、さらにハダマード演算を適用するとする。
# その結果、この例では $R$ と呼ぶことにする：
# 
# $$
#   R = H S H =
#   \begin{pmatrix}
#     \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[2mm]
#     \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
#   \end{pmatrix}
#   \begin{pmatrix}
#     1 & 0\\
#     0 & i
#   \end{pmatrix}
#   \begin{pmatrix}
#     \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[2mm]
#     \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
#   \end{pmatrix}
#   = \begin{pmatrix}
#     \frac{1+i}{2} & \frac{1-i}{2} \\[2mm]
#     \frac{1-i}{2} & \frac{1+i}{2}
#   \end{pmatrix}.
# $$
# 
# このユニタリー・オペレーション（ $R$ ）は興味深い例だ。
# この演算を2回適用することで、行列表現を2乗するのと同じことになり、NOT演算が得られる：
# 
# $$
#   R^2 =
#   \begin{pmatrix}
#     \frac{1+i}{2} & \frac{1-i}{2} \\[2mm]
#     \frac{1-i}{2} & \frac{1+i}{2}
#   \end{pmatrix}^2
#   = \begin{pmatrix}
#     0 & 1 \\[2mm]
#     1 & 0
#   \end{pmatrix}.
# $$
# 
# つまり、 $R$ は *NOT演算の平方根*です。
# このような動作は、同じ演算が2回適用されてNOT演算になるもので、1ビットに対する古典的な演算では不可能である。
# 
# <span id="unitary-operations-on-larger-systems" />
# 
# ### より大きなシステムでの単体演算
# 
# この後のレッスンでは、2つ以上の古典的な状態を持つシステムに対するユニタリー演算の例をたくさん見ていく。
# つの古典的な状態を持つシステムに対するユニタリー演算の例は、以下の行列で与えられる。
# 
# $$
#   A =
#   \begin{pmatrix}
#     {0} & {0} & {1} \\
#     {1} & {0} & {0} \\
#     {0} & {1} & {0}
#   \end{pmatrix}
# $$
# 
# システムの古典的な状態が $0,$ $1,$ と $2,$ であると仮定すると、この操作は加算モジュロとして記述できる。 $3.$
# 
# $$
#   A \vert 0\rangle = \vert 1\rangle,
#   \quad
#   A \vert 1\rangle = \vert 2\rangle,
#   \quad\text{and}\quad
#   A \vert 2\rangle = \vert 0\rangle
# $$
# 
# 行列 $A$ は*並べ替え行列の*一例であり、すべての行と列が正確に1つずつを持つ行列である。 $1.$ このような行列は、作用するベクトルのエントリを並べ替える、つまり並べ替えるだけである。
# 恒等行列は、おそらく順列行列の最も単純な例であり、もう一つの例は、ビットまたは量子ビットに対するNOT演算である。
# すべての順列行列は、任意の正の整数次元において、ユニタリーである。
# 行列が確率的かつユニタリーであるのは、それが並べ替え行列である場合に限られる。
# 
# ユニタリー行列のもう一つの例として、今度は $4\times 4$ ：
# 
# $$
#   U =
#   \frac{1}{2}
#   \begin{pmatrix}
#     1 & 1 & 1 & 1 \\[1mm]
#     1 & i & -1 & -i \\[1mm]
#     1 & -1 & 1 & -1 \\[1mm]
#     1 & -i & -1 & i
#   \end{pmatrix}.
# $$
# 
# この行列は、特に $4\times 4$、 *量子フーリエ変換として*知られる操作を記述している。
# 量子フーリエ変換は、より一般的に、任意の正の整数次元 $n,$ に対して定義することができ、量子アルゴリズムにおいて重要な役割を果たす。
# 
# 

# © IBM Corp., 2017-2025
