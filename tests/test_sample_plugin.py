import cadquery as cq
import plugins.sample_plugin as sp

def test_basic_operation():
    """
    Tests that the bare minimum functionality is working.
    """

    result = cq.Workplane().rect(50, 50, forConstruction=True).vertices().make_cubes(10)

    assert(result.solids().size() == 4)
