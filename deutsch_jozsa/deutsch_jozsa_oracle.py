# 一定(2ビット)
# f(00)=f(10)=f(01)=f(11)=0
def Uf_c2_1(qc, q, c):
    pass

# f(00)=f(10)=f(01)=f(11)=1
def Uf_c2_2(qc, q, c):
    qc.x(q[2])

# 均等(2ビット)
# f(10)=f(11)=1
# f(00)=f(01)=0
def Uf_b2_1(qc, q, c):
    qc.h(q[0])
    qc.h(q[2])
    qc.cx(q[2], q[0])
    qc.h(q[0])
    qc.h(q[2])

# f(01)=f(11)=1
# f(00)=f(10)=0
def Uf_b2_2(qc, q, c):
    qc.h(q[1])
    qc.h(q[2])
    qc.cx(q[2], q[1])
    qc.h(q[1])
    qc.h(q[2])

# f(01)=f(10)=1
# f(00)=f(11)=0
def Uf_b2_3(qc, q, c):
    qc.h(q[0])
    qc.h(q[2])
    qc.cx(q[2], q[0])
    qc.h(q[0])
    qc.h(q[1])
    qc.cx(q[2], q[1])
    qc.h(q[1])
    qc.h(q[2])

# f(00)=f(01)=1
# f(10)=f(11)=0
def Uf_b2_4(qc, q, c):
    qc.x(q[0])
    qc.h(q[0])
    qc.h(q[2])
    qc.cx(q[2], q[0])
    qc.h(q[0])
    qc.h(q[2])
    qc.x(q[0])

# f(00)=f(10)=1
# f(01)=f(11)=0
def Uf_b2_5(qc, q, c):
    qc.x(q[1])
    qc.h(q[1])
    qc.h(q[2])
    qc.cx(q[2], q[1])
    qc.h(q[1])
    qc.h(q[2])
    qc.x(q[1])

# f(00)=f(11)=1
# f(10)=f(01)=0
def Uf_b2_6(qc, q, c):
    qc.x(q[0])
    qc.h(q[0])
    qc.h(q[2])
    qc.cx(q[2], q[0])
    qc.h(q[0])
    qc.h(q[1])
    qc.cx(q[2], q[1])
    qc.h(q[1])
    qc.h(q[2])
    qc.x(q[0])
