from fenics import *
import numpy as np

__all__ = [ "pick_endoring_bc" ]

_endoring_code = """
class EdgeTypeBC : public SubDomain
{
public:

  EdgeTypeBC(std::shared_ptr<MeshFunction<std::size_t> > rfun, std::size_t marker)
  {
    dolfin_assert(rfun->dim() == 1);
    const Mesh& mesh = *rfun->mesh();
    dolfin_assert(mesh.topology().dim()==3);
    const std::vector<double>& mesh_coords = mesh.coordinates();

    std::size_t edge_no = 0;
    for (SubsetIterator edge(*rfun, marker); !edge.end(); ++edge)
    {
      std::vector<Point> edge_coords(0);
      edge_coords.push_back(Point(3, &mesh_coords[edge->entities(0)[0]*3]));
      edge_coords.push_back(Point(3, &mesh_coords[edge->entities(0)[1]*3]));
      edges.push_back(edge_coords);
      const double dist = edge_coords[0].distance(edge_coords[1]);
      distances.push_back(dist);
      log(DBG, \"Edge %3d, [%.3f,%.3f,%.3f], [%.3f,%.3f,%.3f] |%.3f|\", edge_no++,
          edge_coords[0][0], edge_coords[0][1], edge_coords[0][2],
          edge_coords[1][0], edge_coords[1][1], edge_coords[1][2], dist);
    }
  
  }

  /// Return true for points inside the sub domain
  bool inside(const Array<double>& x, bool on_boundary) const
  {
      Point test(3, x.data());
      for (std::size_t i=0; i<edges.size(); i++)
      {
        if ((test.distance(edges[i][0])+test.distance(edges[i][1])-distances[i])<DOLFIN_EPS)
       {
          log(DBG, \"Found dof on edge: %d\", i);
          return true;
       }
      }
      return false;
  }

  private:
    std::vector<std::vector<Point> > edges;
    std::vector<double> distances;

};

"""

class _EdgeTypeBC(SubDomain) :
    def __init__(self, rfun, marker) :
        super(EdgeTypeBC, self).__init__()

        # marked edges
        eids = np.where(rfun.array() == marker)[0]
        mesh = rfun.mesh()

        # points for each edge
        mesh.init(1, 0)
        topo = mesh.topology()(1, 0)
        self._coords = [ mesh.coordinates()[topo(e)] for e in eids ]

    def inside(self, x, on_boundary) :
        for pts in self._coords :
            v1 = pts[0, :]
            v2 = pts[1, :]
            if self._is_between(v1, x, v2) :
                return True
        return False

    def _is_between(self, a, c, b) :
        distance = lambda v1, v2 : np.linalg.norm(v1 - v2)
        return distance(a, c) + distance(c, b) - distance(a, b) < DOLFIN_EPS

def pick_endoring_bc(method = "cpp") :
    if method == "cpp" :
        module = compile_extension_module(\
            _endoring_code, additional_system_headers=[\
                "dolfin/mesh/SubsetIterator.h"])
        return module.EdgeTypeBC
    else :
        return _EdgeTypeBC

if __name__ == "__main__" :

    set_log_level(DBG)

    ndiv = 8
    mesh = UnitCubeMesh(ndiv, ndiv, ndiv)
    rfun = MeshFunction("size_t", mesh, 1)
    rfun.set_all(0)

    bl = CompiledSubDomain("near(x[0], 0.0) && near(x[1], 0.0)")
    bl.mark(rfun, 10)

    endoring = pick_endoring_bc()(rfun, 10)

    V = FunctionSpace(mesh, "CG", 2)
    u, v = TrialFunction(V), TestFunction(V)
    a = inner(grad(u), grad(v)) * dx

    A = assemble(a)

    bc = DirichletBC(V, Constant(0.0), endoring, method = "pointwise")
    bc.apply(A)
