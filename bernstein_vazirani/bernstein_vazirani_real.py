# QISKITのクラス、関数をインポート
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import register, execute
#from qiskit.tools.visualization import plot_histogram
# 量子オラクル
from bernstein_vazirani_oracle import *


TOKEN = 'トークン'
URL = 'https://quantumexperience.ng.bluemix.net/api'
BACKEND = 'ibmq_qasm_simulator'
# BACKEND = 'ibmqx4'

# 実機で実行するための認証
register(TOKEN, URL)

# 回路の作成
q = QuantumRegister(3)
# q = QuantumRegister(4)
c = ClassicalRegister(2)
# c = ClassicalRegister(3)
qc = QuantumCircuit(q, c)

qc.x(q[2])
#qc.x(q[3])
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
#qc.h(q[3])

Uf_2(qc, q, c)
# Uf_3(qc, q, c)


qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
# qc.h(q[3])
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
# qc.measure(q[2], c[2])

# コンパイル&実機で実行
exp = execute(qc, BACKEND, shots=1024, max_credits=10)

# 結果を取得
result = exp.result()

# 結果を表示
print(result)
print(result.get_data())
#plot_histogram(result.get_counts(qc))
