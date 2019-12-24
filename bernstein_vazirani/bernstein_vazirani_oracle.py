# a = (1, 0)
def Uf_2(qc, q, c):
    qc.h(q[0])
    qc.h(q[2])
    qc.cx(q[2], q[0])
    qc.h(q[0])
    qc.h(q[2])

# a = (1, 0, 1)
def Uf_3(qc, q, c):
    qc.h(q[0])
    qc.h(q[3])
    qc.cx(q[3], q[0])
    qc.h(q[0])
    qc.h(q[2])
    qc.cx(q[3], q[2])
    qc.h(q[2])
    qc.h(q[3])
