# QISKITのクラス、関数をインポート
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import register, execute
#from qiskit.tools.visualization import plot_histogram
# 量子オラクル
from deutsch_jozsa_oracle import *


# 回路の作成
q = QuantumRegister(3)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

qc.x(q[2])
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])

# どれか一つ実行
# 一定(2ビット)
Uf_c2_1(qc, q, c)
# Uf_c2_2(qc, q, c)
# 均等(2ビット)
# Uf_b2_1(qc, q, c)
# Uf_b2_2(qc, q, c)
# Uf_b2_3(qc, q, c)
# Uf_b2_4(qc, q, c)
# Uf_b2_5(qc, q, c)
# Uf_b2_6(qc, q, c)

qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])

# コンパイル&シミュレータで実行
sim = execute(qc, 'local_qasm_simulator')

# 結果を取得
result = sim.result()

# 結果を表示
# 'counts': {'00': 1024} のとき一定
# その他のとき均等
print(result)
print(result.get_data())
#plot_histogram(result.get_counts(qc))
