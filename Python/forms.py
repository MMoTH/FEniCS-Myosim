from dolfin import *
import sys

class Forms(object):

    def __init__(self, params):    # amir: sth like constructor

        self.parameters = self.default_parameters()
        self.parameters.update(params)

    def default_parameters(self):
        return {"bff"  : 29.0,
			"bfx"  : 13.3,
			"bxx"  : 26.6,
			"Kappa": 1e5,
			"incompressible" : True,
			};


    def Fmat(self):

        u = self.parameters["displacement_variable"]
        d = u.ufl_domain().geometric_dimension()
        I = Identity(d)
        F = I + grad(u)
        return F

    def Emat(self):

        u = self.parameters["displacement_variable"]
        d = u.ufl_domain().geometric_dimension()
        I = Identity(d)
        F = self.Fmat()
        return 0.5*(F.T*F-I)


    def J(self):
        F = self.Fmat()
        return det(F)


    def LVcavityvol(self):

        u = self.parameters["displacement_variable"]
        N = self.parameters["facet_normal"]
        mesh = self.parameters["mesh"]
        X = SpatialCoordinate(mesh)
        ds = dolfin.ds(subdomain_data = self.parameters["facetboundaries"])

        F = self.Fmat()

        vol_form = -Constant(1.0/3.0) * inner(det(F)*dot(inv(F).T, N), X + u)*ds(self.parameters["LVendoid"])

        return assemble(vol_form, form_compiler_parameters={"representation":"uflacs"})

    def RVcavityvol(self):

        u = self.parameters["displacement_variable"]
        N = self.parameters["facet_normal"]
        mesh = self.parameters["mesh"]
        X = SpatialCoordinate(mesh)
        ds = dolfin.ds(subdomain_data = self.parameters["facetboundaries"])

        F = self.Fmat()

        vol_form = -Constant(1.0/3.0) * inner(det(F)*dot(inv(F).T, N), X + u)*ds(self.parameters["RVendoid"])

        return assemble(vol_form, form_compiler_parameters={"representation":"uflacs"})


    def LVcavitypressure(self):

        W = self.parameters["mixedfunctionspace"]
        w = self.parameters["mixedfunction"]
        mesh = self.parameters["mesh"]

        comm = W.mesh().mpi_comm()
        dofmap =  W.sub(self.parameters["LVendo_comp"]).dofmap()
        val_dof = dofmap.cell_dofs(0)[0]

	    # the owner of the dof broadcasts the value
        own_range = dofmap.ownership_range()

        try:
            val_local = w.vector()[val_dof][0]
        except IndexError:
                val_local = 0.0


        pressure = MPI.sum(comm, val_local)

        return pressure



    def RVcavitypressure(self):

        W = self.parameters["mixedfunctionspace"]
        w = self.parameters["mixedfunction"]
        mesh = self.parameters["mesh"]

        comm = W.mesh().mpi_comm()
        dofmap =  W.sub(self.parameters["RVendo_comp"]).dofmap()
        val_dof = dofmap.cell_dofs(0)[0]

	    # the owner of the dof broadcasts the value
        own_range = dofmap.ownership_range()

        try:
            val_local = w.vector()[val_dof][0]
        except IndexError:
            val_local = 0.0


        pressure = MPI.sum(comm, val_local)

        return pressure


    def PassiveMatSEF(self):

        Ea = self.Emat()
        f0 = self.parameters["fiber"]
        s0 = self.parameters["sheet"]
        n0 = self.parameters["sheet-normal"]
        bff = self.parameters["bff"]
        bfx = self.parameters["bfx"]
        bxx = self.parameters["bxx"]
        Kappa = self.parameters["Kappa"]
        isincomp = self.parameters["incompressible"]

        if(isincomp):
            p = self.parameters["pressure_variable"]

        C = self.parameters["C_param"]


        Eff = inner(f0, Ea*f0)
        Ess = inner(s0, Ea*s0)
        Enn = inner(n0, Ea*n0)
        Efs = inner(f0, Ea*s0)
        Efn = inner(f0, Ea*n0)
        Ens = inner(n0, Ea*s0)


    		#QQ = bff*pow(Eff,2.0) + bfx*(pow(Ess,2.0)+ pow(Enn,2.0)+ 2.0*pow(Ens,2.0)) + bxx*(2.0*pow(Efs,2.0) + 2.0*pow(Efn,2.0))
        QQ = bff*Eff**2.0 + bfx*(Ess**2.0 + Enn**2.0 + 2.0*Ens**2.0) + bxx*(2.0*Efs**2.0 + 2.0*Efn**2.0)

        if(isincomp):
            Wp = C/2.0*(exp(QQ) -  1.0) - p*(self.J() - 1.0)
        else:
            Wp = C/2.0*(exp(QQ) -  1.0) + Kappa/2.0*(self.J() - 1.0)**2.0

        return Wp


    def LVV0constrainedE(self):


        mesh = self.parameters["mesh"]
        u = self.parameters["displacement_variable"]
        ds = dolfin.ds(subdomain_data = self.parameters["facetboundaries"])
        dsendo = ds(self.parameters["LVendoid"], domain = self.parameters["mesh"], subdomain_data = self.parameters["facetboundaries"])
        pendo = self.parameters["lv_volconst_variable"]
        V0= self.parameters["lv_constrained_vol"]

        X = SpatialCoordinate(mesh)
        x = u + X

        F = self.Fmat()
        N = self.parameters["facet_normal"]
        n = cofac(F)*N

        area = assemble(Constant(1.0) * dsendo, form_compiler_parameters={"representation":"uflacs"})
        V_u = - Constant(1.0/3.0) * inner(x, n)
        Wvol = (Constant(1.0/area) * pendo  * V0 * dsendo) - (pendo * V_u *dsendo)

        return Wvol


    def RVV0constrainedE(self):


        mesh = self.parameters["mesh"]
        self.parameters["displacement_variable"]
        ds = dolfin.ds(subdomain_data = self.parameters["facetboundaries"])
        dsendo = ds(self.parameters["RVendoid"], domain = self.parameters["mesh"], subdomain_data = self.parameters["facetboundaries"])
        pendo = self.parameters["rv_volconst_variable"]
        V0= self.parameters["rv_constrained_vol"]

        X = SpatialCoordinate(mesh)
        x = u + X

        F = self.Fmat()
        N = self.parameters["facet_normal"]
        n = cofac(F)*N

        area = assemble(Constant(1.0) * dsendo, form_compiler_parameters={"representation":"uflacs"})
        V_u = - Constant(1.0/3.0) * inner(x, n)
        Wvol = (Constant(1.0/area) * pendo  * V0 * dsendo) - (pendo * V_u *dsendo)

        return Wvol



    def stress(self):

        mesh = self.parameters["mesh"]
        
        e1 = Constant((1.0, 0.0, 0.0))
        e2 = Constant((0.0, 1.0, 0.0))
        e3 = Constant((0.0, 0.0, 1.0))
        
       
        f0 = self.parameters["fiber"]
        s0 = self.parameters["sheet"]
        n0 = self.parameters["sheet-normal"]
        
        C = self.parameters["C_param"]
        bff = self.parameters["bff"]
        bfx = self.parameters["bfx"]
        bxx = self.parameters["bxx"]
        isincomp = self.parameters["incompressible"]
        
        if(isincomp):
            p = self.parameters["pressure_variable"]
        u = self.parameters["displacement_variable"]
        d = u.ufl_domain().geometric_dimension()
        I = Identity(d)
        F = self.Fmat()
        J = self.J()
        Ea = self.Emat()
        
        
        # transform to local coordinates 
        Eff = inner(f0, Ea*f0)
        Enn = inner(n0, Ea*n0)
        Ess = inner(s0, Ea*s0)
        Efs = inner(f0, Ea*s0)
        Efn = inner(f0, Ea*n0)
        Ens = inner(n0, Ea*s0)
        
        
        eQ = (C/2.0)*exp(bff*Eff**2.0 + bfx*(Ess**2.0 + Enn**2.0 + 2.0*Ens**2.0) + bxx*(2.0*Efs**2.0 + 2.0*Efn**2.0))
        
        Sff = 2.0*bff*Eff*eQ
        Sss = 2.0*bfx*Ess*eQ
        Snn = 2.0*bfx*Enn*eQ
        Sfs = 2.0*bxx*Efs*eQ
        Sfn = 2.0*bxx*Efn*eQ
        Sns = 2.0*bfx*Ens*eQ
        
        
        S_local = as_tensor([[Sff, Sfs, Sfn], [Sfs, Sss, Sns], [Sfn, Sns, Snn]]) 
        
        TransMatrix = as_tensor(f0[i]*e1[j], (i,j)) + as_tensor(s0[i]*e2[j], (i,j)) + as_tensor(n0[i]*e3[j], (i,j))
        
        S_global = as_tensor(TransMatrix[i,k]*TransMatrix[j,l]*S_local[k,l],(i,j))
        
        S = S_global
        
        P = F*S - p*inv(F.T)

        T = F*S*F.T - p*I
        
        return  P,S,T