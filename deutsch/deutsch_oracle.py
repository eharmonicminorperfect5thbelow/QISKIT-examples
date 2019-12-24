# f(0)=f(1)=0
def Uf_00(qc, q, c):
    pass

# f(0)=f(1)=1
def Uf_11(qc, q, c):
    qc.x(q[1])

# f(0)=0, f(1)=1
def Uf_01(qc, q, c):
    qc.h(q[0])
    qc.h(q[1])
    qc.cx(q[1], q[0])
    qc.h(q[0])
    qc.h(q[1])

# f(0)=1, f(0)=0
def Uf_10(qc, q, c):
    qc.h(q[0])
    qc.h(q[1])
    qc.cx(q[1], q[0])
    qc.h(q[0])
    qc.h(q[1])
    qc.x(q[1])
