from dolfin import *
import math
import numpy as np

class NSolver(object):


    def __init__(self, params):

        self.parameters = params
        self.isfirstiteration = 0;

    def default_parameters(self):
        return {"rel_tol" : 1e-7,
        "abs_tol" : 1e-7,
                "max_iter": 20}


    def solvenonlinear(self):

        abs_tol = self.default_parameters()["abs_tol"]
        rel_tol = self.default_parameters()["rel_tol"]
        maxiter = self.default_parameters()["max_iter"]
        mode = self.parameters["mode"]
        Jac = self.parameters["Jacobian"]
        #Jac1 = self.parameters["Jac1"]
        #Jac2 = self.parameters["Jac2"]
        #Jac3 = self.parameters["Jac3"]
        #Jac4 = self.parameters["Jac4"]
        Ftotal = self.parameters["F"]
        #F1 = self.parameters["F1"]
        #F2 = self.parameters["F2"]
        #F3 = self.parameters["F3"]
        #F4 = self.parameters["F4"]
        w = self.parameters["w"]
        bcs = self.parameters["boundary_conditions"]
        solvertype = self.parameters["Type"]

        mesh = self.parameters["mesh"]
        comm = w.function_space().mesh().mpi_comm()

    # DEBUGGING PURPOSES ############################# (Everytime at each time point, File handler will be destroyed and reconstructed - FIXME)
    #Q = FunctionSpace(mesh,'CG',1)
    #Quadelem = FiniteElement("Quadrature", mesh.ufl_cell(), degree=4, quad_scheme="default")
    #Quadelem._quad_scheme = 'default'
    #Quad = FunctionSpace(mesh, Quadelem)
    #Param1 = Function(Q)
    #Param1.rename("Param1", "Param1")
    #Param2 = Function(Q)
    #Param2.rename("Param2", "Param2")
    #Param3 = Function(Q)
    #Param3.rename("Param3", "Param3")
    #Param4 = Function(Q)
    #Param4.rename("Param4", "Param4")
    #Param1Quad = Function(Quad)


    #t_a = self.parameters["t_a"]
    #activeforms = self.parameters["ActiveForm"]
    ##################################################


        if(solvertype == 0):
            solve(Ftotal == 0, w, bcs, J = Jac, \
        #solver_parameters={"newton_solver":{"relative_tolerance":1e-9, "absolute_tolerance":1e-9, "maximum_iterations":maxiter, "linear_solver":"umfpack"}}#,\
            form_compiler_parameters={"representation":"uflacs"}
                )
        else:

            it = 0
            if(self.isfirstiteration  == 0):
                A, b = assemble_system(Jac, -Ftotal, bcs, \
                form_compiler_parameters={"representation":"uflacs"}\
                                                )
                resid0 = b.norm("l2")
                rel_res = b.norm("l2")/resid0
                res = resid0
                if(MPI.rank(comm) == 0 and mode > 0):
                    print ("Iteration: %d, Residual: %.3e, Relative residual: %.3e" %(it, res, rel_res))
                    solve(A, w.vector(), b)

            it += 1

            self.isfirstiteration = 1

            B = assemble(Ftotal,\
                        form_compiler_parameters={"representation":"uflacs"}\
                                    )
            for bc in bcs:
                bc.apply(B)

                rel_res = 1.0
                res = B.norm("l2")
                resid0 = res

                if(MPI.rank(comm) == 0 and mode > 0):
                    print ("Iteration: %d, Residual: %.3e, Relative residual: %.3e" %(it, res, rel_res))

                dww = w.copy(deepcopy=True)
                dww.vector()[:] = 0.0

                #while (rel_res > rel_tol and res > abs_tol) and it < maxiter:
                while (rel_res > rel_tol) and it < maxiter:
                        it += 1

                        A, b = assemble_system(Jac, -Ftotal, bcs, \
                                form_compiler_parameters={"representation":"uflacs"}\
                                    )
                        # Trying to assemble individual F terms
                        #print "checking F terms"
                        #f1_temp = assemble(F1, form_compiler_parameters={"representation":"uflacs"})
                        #f2_temp = assemble(F2, form_compiler_parameters={"representation":"uflacs"})
                        #f3_temp = assemble(F3, form_compiler_parameters={"representation":"uflacs"})
                        #f4_temp = assemble(F4, form_compiler_parameters={"representation":"uflacs"})

                        #print "checking nan"
                        #if np.isnan(f1_temp.array().astype(float)).any():
                    #        print "nan in f1"
                    #    if np.isnan(f2_temp.array().astype(float)).any():
                    #        print "nan in f2"
                    #    if np.isnan(f3_temp.array().astype(float)).any():
                    #        print "nan in f3"
                    #    if np.isnan(f4_temp.array().astype(float)).any():
                    #        print "nan in f4"
                        #print A.array(), b.array()
                        #if np.isnan(A.array().astype(float)).any():
                        #    print "nan found in A assembly"
                        #if np.isnan(b.array().astype(float)).any():
                    #        print "nan found in b (Ftotal) assembly"
                        solve(A, dww.vector(), b)
                        w.vector().axpy(1.0, dww.vector())

                # DEBUGGING PURPOSES #############################
                #if(t_a.t_a >= 170 and t_a.t_a <= 172):
                #    print "DEBUGGING"
                #    Param1.vector()[:] = project(activeforms.w1(), Q).vector().array()[:]
                #    self.parameters["FileHandler"][0] << Param1
                #    print >>self.parameters["FileHandler"][4], "w1", " max = ", max(project(activeforms.w1(), Quad).vector()[:]), " min  = ", min(project(activeforms.w1(), Quad).vector()[:])
                #    print >>self.parameters["FileHandler"][4], project(activeforms.w1(), Quad).vector().array()[:]
                #    print >>self.parameters["FileHandler"][4], project(activeforms.w1(), Q).vector().array()[:]

                #    Param2.vector()[:] = project(activeforms.w2(), Q).vector().array()[:]
                #    self.parameters["FileHandler"][1] << Param2
                #    print >>self.parameters["FileHandler"][4], "w2", " max = ", max(project(activeforms.w2(), Quad).vector()[:]), " min  = ", min(project(activeforms.w2(), Quad).vector()[:])
                #    print >>self.parameters["FileHandler"][4], project(activeforms.w2(), Quad).vector().array()[:]
                #    print >>self.parameters["FileHandler"][4], project(activeforms.w2(), Q).vector().array()[:]

                #    Param3.vector()[:] = project(activeforms.Ct(), Q).vector().array()[:]
                #    self.parameters["FileHandler"][2] << Param3
                #    print >>self.parameters["FileHandler"][4], "Ct", " max = ", max(project(activeforms.Ct(), Quad).vector()[:]), " min  = ", min(project(activeforms.Ct(), Quad).vector()[:])
                #    print >>self.parameters["FileHandler"][4], project(activeforms.Ct(), Quad).vector().array()[:]
                #    print >>self.parameters["FileHandler"][4], project(activeforms.Ct(), Q).vector().array()[:]

                #    Param4.vector()[:] = project(activeforms.tr(), Q).vector().array()[:]
                #    self.parameters["FileHandler"][3] << Param4
                #    print >>self.parameters["FileHandler"][4], "tr", " max = ", max(project(activeforms.tr(), Quad).vector()[:]), " min  = ", min(project(activeforms.tr(), Quad).vector()[:])

                #    print >>self.parameters["FileHandler"][4], project(activeforms.tr(), Quad).vector().array()[:]
                #    print >>self.parameters["FileHandler"][4], project(activeforms.tr(), Q).vector().array()[:]

                #    print >>self.parameters["FileHandler"][4], "lmbda*1.85" , " max = ", max(project(activeforms.lmbda()*1.85, Quad).vector()[:]), " min  = ", min(project(activeforms.lmbda()*1.85, Quad).vector()[:])
                #    print >>self.parameters["FileHandler"][4], project(activeforms.lmbda()*1.85, Quad).vector().array()[:]
                #    print >>self.parameters["FileHandler"][4], project(activeforms.lmbda()*1.85, Q).vector().array()[:]

                #    print >>self.parameters["FileHandler"][4], "ls_l0", " max = ", max(project(activeforms.ls_l0(), Quad).vector()[:]), " min  = ", min(project(activeforms.ls_l0(), Quad).vector()[:])

                #    print >>self.parameters["FileHandler"][4], project(activeforms.ls_l0(), Quad).vector().array()[:]
                #    print >>self.parameters["FileHandler"][4], project(activeforms.ls_l0(), Q).vector().array()[:]

                #    print >>self.parameters["FileHandler"][4], "ECa", " max = ", max(project(activeforms.ECa(), Quad).vector()[:]), " min  = ", min(project(activeforms.ECa(), Quad).vector()[:])
                #    print >>self.parameters["FileHandler"][4], project(activeforms.ECa(), Quad).vector().array()[:]
                #    print >>self.parameters["FileHandler"][4], project(activeforms.ECa(), Q).vector().array()[:]

                #    print >>self.parameters["FileHandler"][4], "PK1Stress", " max = ", max(project(activeforms.PK1Stress(), Quad).vector()[:]), " min  = ", min(project(activeforms.PK1Stress(), Quad).vector()[:])
                #    print >>self.parameters["FileHandler"][4], project(activeforms.PK1Stress(), Quad).vector().array()[:]
                #    print >>self.parameters["FileHandler"][4], project(activeforms.PK1Stress(), Q).vector().array()[:]



                ###################################################


                B = assemble(Ftotal, \
                         form_compiler_parameters={"representation":"uflacs"}\
                         )
                for bc in bcs:
                        bc.apply(B)
                #if np.isnan(B.array().astype(float)).any():
                #    print "nan found in B assembly after bcs"
                rel_res = B.norm("l2")/resid0
                res = B.norm("l2")

            if(MPI.rank(comm) == 0 and mode > 0):
                        print ("Iteration: %d, Residual: %.3e, Relative residual: %.3e" %(it, res, rel_res))

            if((rel_res > rel_tol and res > abs_tol) or  math.isnan(res)):
                #self.parameters["FileHandler"][4].close()
                raise RuntimeError("Failed Convergence")
