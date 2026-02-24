#!/usr/bin/env python
# coding: utf-8

# <span id="qiskit-implementation" />
# 
# # Qiskit の実装
# 
# このセクションでは、このレッスンで紹介したコンセプトのQiskit実装をいくつか見てみましょう。
# これらの実装を自分で実行することを強くお勧めします。Qiskit のセットアップ方法の詳細については、 [IBM Quantum ドキュメント](https://docs.quantum.ibm.com)の [「Qiskit のインストール」](/docs/guides/install-qiskit) ページを参照してください。
# 
# Qiskitは継続的に開発されており、主に量子コンピュータの性能を最大化することに重点を置いている。
# その結果、Qiskitは時折コードの非推奨化につながる変更の対象となります。
# このことを念頭に置き、本コースではQiskitのコード例を紹介する前に必ず以下のコマンドを実行し、どのバージョンのQiskitが使用されているかを明確にします。
# Qiskit v1.0 を始め、現在インストールされているQiskitのバージョンを確認する簡単な方法です。
# 
# 

# In[1]:


from qiskit import __version__

print(__version__)


# <span id="vectors-and-matrices-in-python" />
# 
# ## のベクトルと行列。 Python
# 
# Qiskit は Python プログラ ミ ング言語を使用するので、 Qiskit について具体的に説明する前に、 Python における行列とベクトルの計算について簡単に説明しておくとよいでしょう。
# 
# Python では、 `NumPy` ライブラリの `array` クラスを使って行列やベクトルの計算を行うことができます。 クラスは、多くの数値計算や科学計算のための機能を提供しています。
# 次のコードはこのライブラリをロードし、量子ビット状態ベクトル $\vert 0\rangle$ と $\vert 1\rangle,$ に対応する2つの列ベクトル `ket0` と `ket1` を定義し、それらの平均を表示します。
# 
# 

# In[2]:


import numpy as np

ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

print(ket0 / 2 + ket1 / 2)


# また、 `array` 、演算を表す行列を作ることもできる。
# 
# 

# In[3]:


M1 = np.array([[1, 1], [0, 0]])
M2 = np.array([[1, 0], [0, 1]])
M = M1 / 2 + M2 / 2
print(M)


# このコースのレッスン内に登場するすべてのコードは、連続して実行されることに注意してください。
# 従って、 `NumPy` はすでにインポートされているので、ここで改めてインポートする必要はない。
# 
# 行列とベクトルの掛け算を含む行列の掛け算は、 `NumPy` の `matmul` 関数を使って実行することができます。
# 
# 

# In[4]:


print(np.matmul(M1, ket1))
print(np.matmul(M1, M2))
print(np.matmul(M, M))


# この出力フォーマットは、ビジュアル的に言えば、何か不満が残る。
# もっときれいなものが必要な場合の一つの解決策は、Qiskitの `qiskit.visualization` モジュールの`array_to_latex` 関数を使うことです。
# この後のコードでは、 Python 'の一般的な `display` 関数を使用していることに注意してください。
# 対照的に、 `print` の具体的な動作は、 `NumPy` で定義された配列の場合のように、印刷される内容によって異なる場合がある。
# 
# 

# In[5]:


from qiskit.visualization import array_to_latex

display(array_to_latex(np.matmul(M1, ket1)))
display(array_to_latex(np.matmul(M1, M2)))
display(array_to_latex(np.matmul(M, M)))


# <span id="states-measurements-and-operations" />
# 
# ## 状態、測定、操作
# 
# Qiskit には、状態、測定、操作を作成および操作できるクラスがいくつか含まれているため、 Python で量子状態、測定、操作のシミュレーションに必要なすべてをプログラムする必要はありません。
# 以下はその一例です。
# 
# <span id="define-and-display-state-vectors" />
# 
# ### 状態ベクトルの定義と表示
# 
# Qiskitの`Statevector` クラスは、量子状態ベクトルを定義・操作する機能を提供します。
# 以下のコードでは、 `Statevector` クラスがインポートされ、いくつかのベクトルが定義されている。
# (平方根を計算するために、 `NumPy` ライブラリから `sqrt` 関数もインポートしている）。
# この関数は、上記のように `NumPy` がすでにインポートされていれば、 `np.sqrt` として呼び出すこともできる。これは単に、この特定の関数だけをインポートして使用する別の方法である)
# 
# 

# In[6]:


from qiskit.quantum_info import Statevector
from numpy import sqrt

u = Statevector([1 / sqrt(2), 1 / sqrt(2)])
v = Statevector([(1 + 2.0j) / 3, -2 / 3])
w = Statevector([1 / 3, 2 / 3])


# `Statevector` クラスには、状態ベクトルをさまざまな方法で表示するための `draw` メソッドが含まれています。 `text` プレーン・テキストの場合は `latex` 、レンダリングされた LaTeX, の場合は、そして LaTeX のコードの場合は `latex_source` となります。
# (最良の結果を得るために、 LaTeX のコードを表示するには、 `display` ではなく `print` を使用すること)
# 
# 

# In[7]:


display(u.draw("text"))
display(u.draw("latex"))
print(u.draw("latex_source"))


# `Statevector` クラスには、与えられたベクトルが有効な量子状態ベクトルであるか（言い換えれば、ユークリッドノルムが1に等しいか）をチェックする `is_valid` メソッドも含まれています：
# 
# 

# In[8]:


display(u.is_valid())
display(w.is_valid())


# <span id="simulating-measurements-using-statevector" />
# 
# ### Statevector\`を使った計測のシミュレーション
# 
# 次に、 `Statevector` クラスの `measure` メソッドを使って、量子状態の測定をQiskitでシミュレートする方法の1つを見てみましょう。
# 前回定義したのと同じ量子ビット状態ベクトル `v` 。
# 
# 

# In[9]:


display(v.draw("latex"))


# `measure` メソッドを実行すると、標準ベーシスの測定がシミュレートされる。
# その測定結果と、測定後のシステムの新しい量子状態ベクトルを返す。
# (ここでは、 Python 'の `print` 関数に、 `f` 接頭辞を付けて、埋め込み式の書式付き印刷に使用しています)
# 
# 

# In[10]:


outcome, state = v.measure()
print(f"Measured: {outcome}\nPost-measurement state:")
display(state.draw("latex"))


# 測定結果は確率的なものなので、このメソッドは複数回実行すると異なる結果を返す可能性がある。
# 上で定義したベクトル `v` の特定の例について、 `measure` 方法は、測定が行われた後の量子状態ベクトルを次のように定義する
# 
# $$
# \biggl(\frac{1 + 2i}{\sqrt{5}}\biggr) \vert 0\rangle
# $$
# 
# ( $\vert 0\rangle$ ）または
# 
# $$
# - \vert 1\rangle
# $$
# 
# (むしろ $\vert 1\rangle$ ）、測定結果によって異なる。
# どちらの場合も、 $\vert 0\rangle$ と $\vert 1\rangle$ の代替案は、実際には、これらの状態ベクトルと等価である。一方が他方に単位円上の複素数を掛けたものと等しいため、これらは*グローバル位相まで等価で*あると言われる。
# この問題については[量子回路の](/learning/courses/basics-of-quantum-information/quantum-circuits/introduction)レッスンで詳しく説明するので、今は無視しても構わない。
# 
# `Statevector` は、無効な量子状態ベクトルに対して `measure` メソッドを適用するとエラーをスローします。
# 
# `Statevector` また、 `sample_counts` メソッドも用意されており、システム上で任意の回数の測定シミュレーションが可能で、毎回新しい状態のコピーから始めることができる。 例えば、以下のコードは、ベクトル `v` $1000$ 回を測定した結果を示している。（高い確率で）結果 $0$ $9$ 回に約 $5$ 回（または $1000$ 試行の約 $556$ 回）、結果 $1$ $9$ 回に約 $4$ 回（または $1000$ 試行の約 $444$ 回）。
# 以下のコードでは、結果を視覚化するための `qiskit.visualization` モジュールの `plot_histogram` 関数も示している。
# 
# 

# In[11]:


from qiskit.visualization import plot_histogram

statistics = v.sample_counts(1000)
plot_histogram(statistics)


# このコードを、 $1000,$ の代わりに異なるサンプル数で何度も実行することは、試行回数が各結果の出現回数にどのように影響するかについての直感を養うのに役立つかもしれない。
# サンプルの数が増えれば増えるほど、それぞれの可能性のサンプルの割合は、対応する確率に近づいていくだろう。
# この現象は、より一般的に言えば、確率論における*大数の法則として*知られている。
# 
# 

# <span id="perform-operations-with-operator-and-statevector" />
# 
# ### 演算子 `Operator` と `Statevector` を使って演算を行う
# 
# Qiskitでは、次の例のように `Operator` クラスを使って単体演算を定義することができます。
# このクラスには、 `Statevector` と同様の引数を持つ `draw` メソッドが含まれている。
# なお、 `latex` オプションは、 `array_from_latex` と同等の結果をもたらす。
# 
# 

# In[12]:


from qiskit.quantum_info import Operator

Y = Operator([[0, -1.0j], [1.0j, 0]])
H = Operator([[1 / sqrt(2), 1 / sqrt(2)], [1 / sqrt(2), -1 / sqrt(2)]])
S = Operator([[1, 0], [0, 1.0j]])
T = Operator([[1, 0], [0, (1 + 1.0j) / sqrt(2)]])

display(T.draw("latex"))


# `evolve` 、状態ベクトルにユニタリー演算を施すことができる。
# 
# 

# In[13]:


v = Statevector([1, 0])

v = v.evolve(H)
v = v.evolve(T)
v = v.evolve(H)
v = v.evolve(S)
v = v.evolve(Y)

display(v.draw("latex"))


# <span id="a-preview-of-quantum-circuits" />
# 
# ### 量子回路のプレビュー
# 
# 量子回路は、このコースの3番目のレッスンである[量子回路の](/learning/courses/basics-of-quantum-information/quantum-circuits/introduction)レッスンまで正式には導入されませんが、それでも、Qiskitの`QuantumCircuit` クラスを使って、量子ビット単位演算の合成を実験することができます。
# 特に、量子回路（この場合、単に1つの量子ビットに対して実行されるユニタリー演算のシーケンスとなる）を次のように定義することができる。
# 
# 

# In[14]:


from qiskit import QuantumCircuit

circuit = QuantumCircuit(1)

circuit.h(0)
circuit.t(0)
circuit.h(0)
circuit.s(0)
circuit.y(0)

display(circuit.draw(output="mpl"))


# ここでは、 `QuantumCircuit` クラスの `draw` メソッドを、 `mpl` レンダラー（ `Matplotlib` の略、 Python 可視化ライブラリ）で使っている。
# このコースで量子回路に使うのはこのレンダラーだけだが、他にもテキストベースのレンダラーや LaTeX-based。
# 
# 操作は図の左から右へと順次適用される。
# この回路に対応するユニタリー行列を得る便利な方法は、 `Operator` クラスの `from_circuit` メソッドを使うことである。
# 
# 

# In[15]:


display(Operator.from_circuit(circuit).draw("latex"))


# また、量子状態ベクトルを初期化し、回路が記述する一連の操作に従ってその状態を進化させることもできる。
# 
# 

# In[16]:


ket0 = Statevector([1, 0])
v = ket0.evolve(circuit)
display(v.draw("latex"))


# 以下のコードは、上記の回路から得られた状態を標準基底測定で4000回測定する実験をシミュレートしている（毎回状態の新しいコピーを使用）。
# 
# 

# In[17]:


statistics = v.sample_counts(4000)
display(plot_histogram(statistics))


# © IBM Corp., 2017-2025
