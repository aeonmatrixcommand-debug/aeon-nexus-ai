from services.guardian.control_tower.control_tower import EnterpriseControlTower


def test_control_tower():

    tower = EnterpriseControlTower()

    result = tower.monitor(
        {
            "risk_score": 90,
            "action": "ALLOCATE_STOCK"
        }
    )

    assert result["risk"]["risk_level"] == "CRITICAL"
    assert result["governance"]["approved"] is True
