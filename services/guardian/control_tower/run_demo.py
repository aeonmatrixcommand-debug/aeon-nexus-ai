from services.guardian.control_tower.control_tower import EnterpriseControlTower


tower = EnterpriseControlTower()

print(
    tower.monitor(
        {
            "OTIF": 96,
            "risk_score": 35,
            "action": "ALLOCATE_STOCK"
        }
    )
)
