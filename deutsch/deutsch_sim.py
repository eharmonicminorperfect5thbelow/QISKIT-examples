# QISKITのクラス、関数をインポート
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import register, execute
#from qiskit.tools.visualization import plot_histogram
# 量子オラクル
from deutsch_oracle import *


# 回路の作成
q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

qc.x(q[1])
qc.h(q[0])
qc.h(q[1])

# どれか一つ実行
Uf_00(qc, q, c)
# Uf_11(qc, q, c)
# Uf_01(qc, q, c)
# Uf_10(qc, q, c)

qc.h(q[0])
qc.h(q[1])
qc.measure(q, c)

# コンパイル&シミュレータで実行
sim = execute(qc, 'local_qasm_simulator')

# 結果を取得
result = sim.result()

# 結果を表示
# 'counts': {'10': 1024} のとき一定
# 'counts': {'11': 1024} のとき均等
print(result)
print(result.get_data())
#plot_histogram(result.get_counts(qc))
