# @Author: charlesmann
# @Date:   2021-04-06T11:52:46-04:00
# @Last modified by:   charlesmann
# @Last modified time: 2021-11-19T14:09:42-05:00



#
# .. _demo_hyperelasticity:
#
# Hyperelasticity
# ===============
#
# This demo is implemented in a single Python file,
# :download:`demo_hyperelasticity.py`, which contains both the
# variational forms and the solver.
#
#
# Background
# ----------
#
# See the section :ref:`hyperelasticity` for some mathematical
# background on this demo.
#
#
# Implementation
# --------------
#
# This demo is implemented in the :download:`demo_hyperelasticity.py`
# file.
#
# First, the :py:mod:`dolfin` module is imported::

from dolfin import *
import numpy as np
import numpy.random as r

# The behavior of the form compiler FFC can be adjusted by prescribing
# various parameters. Here, we want to use the UFLACS backend of FFC::

def execute_demo(mesh,S_fcn_space,Fg,no_grow_mesh,iter_counter):


    import numpy as np
    import numpy.random as r

    # Note: no_grow_mesh is multiplied by the traction applied on the right
    # face. no_grow_mesh = 1 means we are solving the normal problem. no_grow_mesh
    # = 0 means we are just solving given a growth def. gradient

    # Optimization options for the form compiler
    parameters["form_compiler"]["cpp_optimize"] = True
    parameters["form_compiler"]["representation"] = "uflacs"
    parameters["form_compiler"]["quadrature_degree"] = 2

    # The first line tells the form compiler to use C++ compiler optimizations when
    # compiling the generated code. The remainder is a dictionary of options which
    # will be passed to the form compiler. It lists the optimizations strategies
    # that we wish the form compiler to use when generating code.
    #
    # .. index:: VectorFunctionSpace
    #
    # First, we need a tetrahedral mesh of the domain and a function space
    # on this mesh. Here, we choose to create a unit cube mesh with 25 ( =
    # 24 + 1) vertices in one direction and 17 ( = 16 + 1) vertices in the
    # other two direction. On this mesh, we define a function space of
    # continuous piecewise linear vector polynomials (a Lagrange vector
    # element space)::

    # Create mesh and define function space
    #mesh = UnitCubeMesh(24, 16, 16)

    V = VectorFunctionSpace(mesh, "Lagrange", 1)

    subdomains = MeshFunction('int', mesh, 3)
    no_of_cells = len(subdomains.array())


    sample_indices = r.choice(no_of_cells,int(0.8*no_of_cells),replace=False)
    test_param_values = [10,50]
    V0 = FunctionSpace(mesh,"DG",0)
    param = Function(V0)

    for cell_no in range(len(subdomains.array())):
        if cell_no in sample_indices:
            param.vector()[cell_no] = test_param_values[1]
        else:
            param.vector()[cell_no] = test_param_values[0]



    file2 = File("iter_"+str(iter_counter)+"/param_values.pvd");
    file2 << param;

    # Note that :py:class:`VectorFunctionSpace
    # <dolfin.functions.functionspace.VectorFunctionSpace>` creates a
    # function space of vector fields. The dimension of the vector field
    # (the number of components) is assumed to be the same as the spatial
    # dimension, unless otherwise specified.
    #
    # .. index:: compiled subdomain
    #
    # The portions of the boundary on which Dirichlet boundary conditions
    # will be applied are now defined::

    # Mark boundary subdomians
    left =  CompiledSubDomain("near(x[0], side) && on_boundary", side = 0.0)
    bottom = CompiledSubDomain("near(x[1], side) && on_boundary", side = 0.0)
    back = CompiledSubDomain("near(x[2], side) && on_boundary", side = 0.0)
    right = CompiledSubDomain("near(x[0], side) && on_boundary", side = 1.0)

    # The boundary subdomain ``left`` corresponds to the part of the
    # boundary on which :math:`x=0` and the boundary subdomain ``right``
    # corresponds to the part of the boundary on which :math:`x=1`. Note
    # that C++ syntax is used in the :py:func:`CompiledSubDomain`
    # <dolfin.compilemodules.subdomains.CompiledSubDomain>` function since
    # the function will be automatically compiled into C++ code for
    # efficiency. The (built-in) variable ``on_boundary`` is true for points
    # on the boundary of a domain, and false otherwise.
    #
    # .. index:: compiled expression
    #
    # The Dirichlet boundary values are defined using compiled expressions::

    # Define Dirichlet boundary (x = 0 or x = 1)
    c = Constant((0.0, 0.0, 0.0))
    r = Expression(("scale*0.0",
                    "scale*(y0 + (x[1] - y0)*cos(theta) - (x[2] - z0)*sin(theta) - x[1])",
                    "scale*(z0 + (x[1] - y0)*sin(theta) + (x[2] - z0)*cos(theta) - x[2])"),
                    scale = 0.5, y0 = 0.5, z0 = 0.5, theta = pi/3, degree=2)
    test = Function(V)

    # Note the use of setting named parameters in the :py:class:`Expression
    # <dolfin.functions.expression.Expression>` for ``r``.
    #
    # The boundary subdomains and the boundary condition expressions are
    # collected together in two :py:class:`DirichletBC
    # <dolfin.fem.bcs.DirichletBC>` objects, one for each part of the
    # Dirichlet boundary::

    bcl = DirichletBC(V.sub(0), Constant(0.0), left)
    bcb = DirichletBC(V.sub(1), Constant(0.0), bottom)
    bcback = DirichletBC(V.sub(2), Constant(0.0), back)
    bcr = DirichletBC(V, r, right)
    bcr2 = DirichletBC(V,test,right)
    #bcs = [bcl, bcr]
    bcs = [bcl,bcb,bcback]

    # The Dirichlet (essential) boundary conditions are constraints on the
    # function space :math:`V`. The function space is therefore required as
    # an argument to :py:class:`DirichletBC <dolfin.fem.bcs.DirichletBC>`.
    #
    # .. index:: TestFunction, TrialFunction, Constant
    #
    # Trial and test functions, and the most recent approximate displacement
    # ``u`` are defined on the finite element space ``V``, and two objects
    # of type :py:class:`Constant <dolfin.functions.constant.Constant>` are
    # declared for the body force (``B``) and traction (``T``) terms::

    # Define functions
    du = TrialFunction(V)            # Incremental displacement
    v  = TestFunction(V)             # Test function
    u  = Function(V)                 # Displacement from previous iteration
    B  = Constant((0.0, 0.0, 0.0))  # Body force per unit volume
    #T  = Constant((0.5,  0.0, 0.0))  # Traction force on the boundary
    T  = as_vector( [0.5, 0.0, 0.0])
    print T[0]

    # In place of :py:class:`Constant <dolfin.functions.constant.Constant>`,
    # it is also possible to use ``as_vector``, e.g.  ``B = as_vector( [0.0,
    # -0.5, 0.0] )``. The advantage of Constant is that its values can be
    # changed without requiring re-generation and re-compilation of C++
    # code. On the other hand, using ``as_vector`` can eliminate some
    # function calls during assembly.
    #
    # With the functions defined, the kinematic quantities involved in the model
    # are defined using UFL syntax::

    # Kinematics
    #i,k = indices(2)

    d = len(u)
    I = Identity(d)             # Identity tensor
    Fmat = I + grad(u)             # Total deformation gradient
    #Fe = as_tensor(Fmat[i,j]*inv(Fg)[j,k], (i,k)) # For identity Fg, Fe = F
    Fe = Fmat*inv(Fg)
    print project(Fe,TensorFunctionSpace(mesh,"DG",1)).vector().get_local()[0:15]

    #C = Fmat.T*Fmat                   # Right Cauchy-Green tensor
    C = Fe.T*Fe                   # Right Cauchy-Green tensor

    # Invariants of deformation tensors
    Ic = tr(C)
    J  = det(Fe)

    # Next, the material parameters are set and the strain energy density
    # and the total potential energy are defined, again using UFL syntax::

    # Elasticity parameters
    E, nu = 1000.0, 0.4
    mu, lmbda = Constant(E/(2*(1 + nu))), Constant(E*nu/((1 + nu)*(1 - 2*nu)))
    Press = Expression(("P"), P=0.0, degree=0)
    facetboundaries = MeshFunction('size_t', mesh, mesh.topology().dim()-1)
    ds = dolfin.ds(subdomain_data = facetboundaries)
    class Right(SubDomain):
        def inside(self, x, on_boundary):
            tol = 1E-10
            return on_boundary and abs(x[0]-1.0) < tol
    facetboundaries.set_all(0)
    right = Right()
    right.mark(facetboundaries, 2)


    N = FacetNormal (mesh)
    #F3 = inner(Press*N, v)*ds(2, domain=mesh)




    # Stored strain energy density (compressible neo-Hookean model)
    #psi = (mu/2)*(Ic - 3) - mu*ln(J) + (lmbda/2)*(ln(J))**2
    psi = lambda F: mu/2*(inner(F, F) - 3) - mu * ln(det(F)) + lmbda/2 * (ln(det(F)))**2

    psi1 = (mu/2)*(tr(Fe.T*Fe)-3) - mu*ln(det(Fe)) + (lmbda/2)*(ln(det(Fe)))**2
    # Total potential energy
    #Pi = psi1*dx - dot(B, u)*dx - dot(T, u)*ds

    # Just as for the body force and traction vectors, :py:class:`Constant
    # <dolfin.functions.constant.Constant>` has been used for the model
    # parameters ``mu`` and ``lmbda`` to avoid re-generation of C++ code
    # when changing model parameters. Note that ``lambda`` is a reserved
    # keyword in Python, hence the misspelling ``lmbda``.
    #
    # .. index:: directional derivative; derivative, taking variations; derivative, automatic differentiation; derivative
    #
    # Directional derivatives are now computed of :math:`\Pi` and :math:`L`
    # (see :eq:`first_variation` and :eq:`second_variation`)::

    # Compute first variation of Pi (directional derivative about u in the direction of v)
    #F = derivative(Pi, u, v)

    # Compute Jacobian of F
    #Jac = derivative(F, u, du)

    # The complete variational problem can now be solved by a single call to
    # :py:func:`solve <dolfin.fem.solving.solve>`::

    # File to save displacements
    file = File("iter_"+str(iter_counter)+"/displacement1.pvd");
    stress_file = File("iter_"+str(iter_counter)+"/pk2_x_projection.pvd")
    x_dir = as_vector([1,0,0])

    loading_steps = min(20,no_grow_mesh*19+1)

    # Save rxn force for each loading step
    # Get x dof
    x_dofs = V.sub(0).dofmap().dofs()
    rxn_force_trace = np.zeros(loading_steps)
    # It is increasing, so Press is per unit area.

    # Need to calculate the area of the right face of the grown mesh,
    # and use that to apply the same total force after each growth iteration
    forces_to_apply = np.linspace(10,200,20)

    # After some iteration, area_right = 0, gives infinite answer
    # save facetboundaries to make sure right face is always appropriately marked
    facets_file = File("iter_"+str(iter_counter)+"/facets.pvd")
    facets_file << facetboundaries

    # Indeed, after iteration 4, the right boundary is still labeled as 0
    # trying to decrease the tolerance for the class "Right" from 1E-14 to 1E-10.
    # Thinking about how we move the mesh nodes to grow, we use the displacement
    # obtained from the Newton solver. This has an absolute tolerance of 1E-10 I believe.
    # Thus, we aren' guaranteed that the right face of the cube remains at x=1.
    # Shouldn't be a problem with ventricle simulations. This seems to have worked.


    area_right = assemble(1*ds(2, domain=mesh)) # multiplying by a measure (ds, dx) is ufl's way of integrating
    print "area of right face", area_right

    for i in np.arange(loading_steps):
        #T = as_vector([0.5 + i,0.0,0.0])
        Press.P = forces_to_apply[i]/area_right
        Press.P *= no_grow_mesh
        print Press.P
        #Pi = psi1*dx - dot(B, u)*dx - dot(T, u)*ds(2, domain=mesh)
        Pi = psi1*dx - dot(B, u)*dx - inner(Press*N, u)*ds(2, domain=mesh)
        F = derivative(Pi, u, v)
        Jac = derivative(F, u, du)

        # Solve variational problem
        solve(F == 0, u, bcs, J=Jac)

        # Finally, the solution ``u`` is saved to a file named
        # ``displacement.pvd`` in VTK format, and the deformed mesh is plotted
        # to the screen::f

        # Calculate stress
        Fmat = variable(Fmat)
        Fe = variable(Fe)

        #P = diff(psi(Fmat),Fmat)
        P = diff(psi(Fe),Fe)
        S = inv(Fe)*P # Kurtis double check that you only use Fe in this transform
        pk2_x = inner(x_dir,S*x_dir)
        pk2_x_projection = project(pk2_x,S_fcn_space)
        pk2_x_projection.rename("PK2 x-dir","PK2 x-dir") #so paraview can find it through time
        stress_file << pk2_x_projection

        # I think Press is per unit area, so increasing the surface area by
        # growing the mesh isn't changing the end stress response. Going to calculate
        # the reaction force to see if this is increasing between iterations
        # reaction force at the left face*
        b = assemble(F,form_compiler_parameters={"representation":"uflacs"})

        for boundary_condition_i in np.arange(np.shape(bcs)[0]-1):
            bcs[boundary_condition_i+1].apply(b) # apply all boundary conditions except the left

        f_int_total = b.copy()
        rxn_force=0.0
        for kk in x_dofs:
            rxn_force += f_int_total[kk]

        rxn_force_trace[i] = abs(rxn_force)

        #print project(P,TensorFunctionSpace(mesh,"DG",1)).vector().array()


        # Save solution in VTK format if not growing
        if no_grow_mesh > 0:
            u.rename("displacement","displacement")
            file << u;


    """test.assign(u)
    bcs = [bcl,bcr2]
    B  = Constant((0.0, 0.0, 0.0))  # Body force per unit volume
    # Total potential energy
    Pi = psi*dx - dot(B, u)*dx - dot(T, u)*ds
    # Compute first variation of Pi (directional derivative about u in the direction of v)
    F = derivative(Pi, u, v)

    # Compute Jacobian of F
    J = derivative(F, u, du)

    solve(F == 0, u, bcs, J=J)

    file = File("displacement2.pvd");
    file << u;"""

    print "reaction force"
    print np.shape(rxn_force_trace)
    print rxn_force_trace
    if no_grow_mesh > 0: #rxn force not relevant when solving for u to grow mesh
        np.save("iter_"+str(iter_counter)+"/rxn_force.npy",rxn_force_trace)


    # Plot and hold solution
    #plot(u, mode = "displacement", interactive = True)
    Fmat = variable(Fmat)
    Fe = variable(Fe)

    P = diff(psi(Fe),Fe)
    #print project(P,TensorFunctionSpace(mesh,"DG",1)).vector().array()
    return P,Fe, u
