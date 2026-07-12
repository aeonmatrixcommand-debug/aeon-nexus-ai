from services.validation.kpi_validator import KPIValidator


def test_otif_validation():
    validator = KPIValidator()

    result = validator.validate_otif({
        "delivery_date": "2026-07-12",
        "order_qty": 100,
        "delivered_qty": 100
    })

    assert result == []


def test_inventory_accuracy():
    validator = KPIValidator()

    result = validator.validate_inventory_accuracy({
        "system_qty": 100,
        "physical_qty": 100
    })

    assert result == []
