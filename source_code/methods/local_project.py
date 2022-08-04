from dolfin import *


deg = 2
metadata={"quadrature_degree": deg}
def local_project(v,V):
    dv = TrialFunction(V)
    v_ = TestFunction(V)
    a_proj = inner(dv,v_)*dx(metadata=metadata)
    b_proj = inner(v,v_)*dx(metadata=metadata)
    solver = LocalSolver(a_proj,b_proj)
    solver.factorize()
    u = Function(V)
    solver.solve_local_rhs(u)
    return u
