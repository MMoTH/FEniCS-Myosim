import dolfin
import mshr 

x = 10.0
y = 0.0
z = 0.0

cyl_top = dolfin.Point(x,y,z)
cyl_bottom = dolfin.Point(0,0,0)
top_radius = 1.0
bottom_radius = 1.0
segments = 20.0

geometry = mshr.Cylinder(cyl_top,cyl_bottom,top_radius,bottom_radius,segments)
mesh = mshr.generate_mesh(geometry,20)

File('cylinder_3.pvd') << mesh


