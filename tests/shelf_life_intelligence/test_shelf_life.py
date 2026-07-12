from services.guardian.shelf_life_intelligence.runtime import ShelfLifeIntelligence


def test_shelf_life():
    assert ShelfLifeIntelligence().analyze(
        {"days_remaining": 2}
    )["risk"] == "critical"

    assert ShelfLifeIntelligence().analyze(
        {"days_remaining": 10}
    )["risk"] == "normal"
