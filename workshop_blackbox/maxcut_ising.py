import os 
import networkx as nx
import numpy as np
from amplify import VariableGenerator, solve, FixstarsClient
from dotenv import load_dotenv

# セキュリティ対策: トークンをコードに直書きせず、環境変数(.env)から読み込む
load_dotenv()

def create_random_graph(n_nodes: int, seed: int = 0):
    """
    NetworkXを使用してランダムグラフ(重み付き)を作成する。
    
    Args:
        n_nodes (int): 頂点の数
        seed (int): 乱数シード (実験の再現性を担保するために固定する)
    Returns:
        nx.Graph: 重み付きグラフ
    """
    G = nx.gnp_random_graph(n_nodes, 0.7, seed=seed)
    # 相互作用の強さにばらつきを持たせるため、エッジにランダムな重みを付与
    # 物理的意味: 相互作用 J_ij の強さ
    np.random.seed(seed)
    for (u,v) in G.edges():
        G.edges[u,v]["weight"] = np.random.randint(1, 10)
    return G

def build_maxcut_hamiltonian(G):
    #スピン変数の生成(+1 or -1)
    gen = VariableGenerator()
    # "Ising"を指定することで、変数は {+1, -1} の値を取る物理スピンとして定義される
    s = gen.array("Ising", len(G.nodes))
   
    #エネルギー関数(ハミルトニアン)の初期化
    energy = 0

    # グラフの全エッジ(相互作用)についてループ
    for u,v in G.edges:
        w = G.edges[u, v]["weight"]

        #ハミルトニアン
        """
        Max-Cut問題ではカットされる辺の重みの合計Cを最大化する
        AmplifyはエネルギーHを最小化するマシンなので、
        H = = -Cとすることで、対応づけが可能になる

        [項の解説]
        スピンが異符号 (+1, -1) のとき: (1 - (-1))/2 = 1  -> 重み w が加算される
        スピンが同符号 (+1, +1) のとき: (1 - 1)/2    = 0  -> 重みは加算されない (カット失敗)
        """
        term = - w * (1 - s[u] * s[v]) / 2
        energy += term

    return energy, s

def main():
    # 1. トークンの確認 (環境変数)
    token = os.getenv("AMPLIFY_TOKEN")
    if not token:
        print("Error: .envファイルに AMPLIFY_TOKEN が設定されていません")
        return

    # 2. 問題設定 (物理実験のセットアップ)
    N = 10
    G = create_random_graph(N)

    # 3. ハミルトニアンの構築 (数式モデル化)
    print("Building Hamiltonian...")
    hamiltonian, spins = build_maxcut_hamiltonian(G)

    # 4. ソルバー実行 (実験開始)
    print("Solving...")
    client = FixstarsClient()
    client.token = token
    client.parameters.timeout = 1000

    result = solve(hamiltonian, client)

    # 5. 結果の解析
    if len(result) > 0:
        #エネルギーを元のカット値に戻して表示
        print(f"Max-Cut Value: {-result.best.objective}")
        
        # 数式上の記号 s に、計算結果の値(+1, -1)を代入して表示
        print(f"Spins: {spins.evaluate(result.best.values)}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()







    
