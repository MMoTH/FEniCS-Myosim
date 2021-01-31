import gmsh

gmsh.initialize()

gmsh.model.add('cylinder')

gmsh.logger.start()

gmsh.model.occ.addCylinder(0,0,0,1,0,0,1,1)
gmsh.model.occ.addCylinder(1,0,0,8,0,0,1,2)
gmsh.model.occ.addCylinder(9,0,0,1,0,0,1,3)
cyls = [(3,2),(3,3)]
ov, ovv = gmsh.model.occ.fragment([(3,1)],cyls)
print "fragment produced volumes:"
for e in ov:
    print e

print ov[-1][1]
gmsh.model.occ.synchronize()

gmsh.model.addPhysicalGroup(3,[ov[-1][1]],10)
lcar1 = 0.3
gmsh.model.mesh.setSize(gmsh.model.getEntities(0), lcar1)

gmsh.model.mesh.generate(3)

gmsh.write('cylinder.msh')

gmsh.fltk.run()

gmsh.finalize()
