# QISKITのクラス、関数をインポート
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import register, execute

# 量子オラクル
# f(0)=0, f(1)=1
def Uf(qc, q, c):
    qc.h(q[0])
    qc.h(q[1])
    qc.cx(q[1], q[0])
    qc.h(q[0])
    qc.h(q[1])

# 回路の作成
q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

qc.x(q[1])
qc.h(q[0])
qc.h(q[1])

Uf(qc, q, c)

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