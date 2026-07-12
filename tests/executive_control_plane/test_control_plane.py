from services.guardian.executive_control_plane.runtime import ExecutiveControlPlane

def test_control():
    assert ExecutiveControlPlane().evaluate({})["decision"] == "approved"
