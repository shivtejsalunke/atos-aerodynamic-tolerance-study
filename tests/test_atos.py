import math,pytest
from atos.geometry import eccentric_offset
from atos.tolerance import tolerance_stack
from atos.aero import drag_force,drag_sensitivity

def test_eccentric_vectors():
 r=eccentric_offset(.25,.25,90); assert r['magnitude_mm']==pytest.approx(math.sqrt(2)*.25); assert r['theoretical_max_mm']==pytest.approx(.5); assert eccentric_offset(.2,.2,180)['magnitude_mm']==pytest.approx(0)
def test_tolerance_stack():
 r=tolerance_stack([.1,.15,.05]); assert r['worst_case_mm']==pytest.approx(.3); assert r['rss_mm']==pytest.approx(math.sqrt(.035))
def test_drag_sensitivity():
 b=drag_force(1.225,70,.025,12); r=drag_sensitivity(1.225,70,.025,12,-4.5); assert r['baseline_drag_n']==pytest.approx(b); assert r['scenario_drag_n']==pytest.approx(b*.955)
def test_invalid_inputs():
 with pytest.raises(ValueError): eccentric_offset(-1,0,0)
 with pytest.raises(ValueError): tolerance_stack([.1,-.2])
 with pytest.raises(ValueError): drag_force(0,10,.1,1)
