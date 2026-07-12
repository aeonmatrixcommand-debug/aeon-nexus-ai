from services.validation.kpi_validator import KPIValidator


validator = KPIValidator()


def test_validate_otif_success():
    errors = validator.validate_otif({
        "delivery_date": "2026-07-12",
        "order_qty": 10,
        "delivered_qty": 10,
    })

    assert errors == []


def test_validate_otif_missing_date():
    errors = validator.validate_otif({
        "order_qty": 10,
        "delivered_qty": 10,
    })

    assert "missing_delivery_date" in errors


def test_validate_otif_quantity_mismatch():
    errors = validator.validate_otif({
        "delivery_date": "2026-07-12",
        "order_qty": 10,
        "delivered_qty": 8,
    })

    assert "quantity_mismatch" in errors


def test_inventory_ok():
    errors = validator.validate_inventory_accuracy({
        "system_qty": 100,
        "physical_qty": 100,
    })

    assert errors == []


def test_inventory_difference():
    errors = validator.validate_inventory_accuracy({
        "system_qty": 100,
        "physical_qty": 95,
    })

    assert "inventory_difference" in errors
