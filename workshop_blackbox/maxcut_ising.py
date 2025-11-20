import os 
import networkx as nx
import numpy as np
from amplify import VariableGenerator, solve, FixstarsClient
from dotenv import load_dotenv

#.envの読み込み
load_dotenv()

def create_random_graph(n_nodes: int, seed: int = 0):
    #グラフ作成
    G = nx.gnp_random_graph(n_nodes, 0.7, seed=seed)
    np.random.seed(seed)
    for (u,v) in G.edges():
        G.edges[u,v]["weight"] = np.random.randint(1, 10)
    return G

def build_maxcut_hamiltonian(G):
    #スピン変数の生成(+1 or -1)
    gen = VariableGenerator()
    s = gen.array("Ising", len(G.nodes))

    #エネルギー関数(ハミルトニアン)の初期化
    energy = 0

    for u,v in G.edges:
        w = G.edges[u, v]["weight"]

        #ハミルトニアン
        """
        Max-Cut問題ではカットされる辺の重みの合計Cを最大化する
        AmplifyはエネルギーHを最小化するマシンなので、
        H = = -Cとすることで、対応づけが可能になる
        """
        term = - w * (1 - s[u] * s[v]) / 2
        energy += term

    return energy, s

def main():
    "トークン確認"
    token = os.getenv("AMPLIFY_TOKEN")
    if not token:
        print("Error: .envファイルに AMPLIFY_TOKEN が設定されていません")
        return

    #問題設定
    N = 10
    G = create_random_graph(N)

    #ハミルトニアンの構築
    print("Building Hamiltonian...")
    hamiltonian, spins = build_maxcut_hamiltonian(G)

    #ソルバー実行
    print("Solving...")
    client = FixstarsClient()
    client.token = token
    client.parameters.timeout = 1000

    result = solve(hamiltonian, client)

    #結果表示
    if len(result) > 0:
    #エネルギーを元のカット値に戻して表示
        print(f"Max-Cut Value: {-result.best.objective}")
        print(f"Spins: {spins.evaluate(result.best.values)}")

if __name__ == "__main__":
    main()







    