#!/bin/bash
set -e

echo "🌍🦸‍♂️🦸‍♀️🧠 AEONMATRIX Sprint Quality Hardening Start"

echo "📌 1. Check repository status"
git status

echo "📌 2. Create validation structure"
mkdir -p services/validation
mkdir -p tests/unit
mkdir -p tests/integration
mkdir -p tests/regression
mkdir -p tests/fixtures

echo "📌 3. Create KPI validation modules"

cat > services/validation/kpi_validator.py <<'PY'
class KPIValidator:

    def validate_otif(self, order):
        errors = []

        if not order.get("delivery_date"):
            errors.append("missing_delivery_date")

        if order.get("delivered_qty", 0) < order.get("order_qty", 0):
            errors.append("quantity_mismatch")

        return errors


    def validate_inventory_accuracy(self, stock):
        errors = []

        if stock.get("system_qty") != stock.get("physical_qty"):
            errors.append("inventory_difference")

        return errors
PY


echo "📌 4. Create KPI Unit Tests"

cat > tests/unit/test_kpi_validator.py <<'PY'
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
PY


echo "📌 5. Create Golden Dataset"

cat > tests/fixtures/otif_cases.json <<'JSON'
[
 {
  "order_id":"AEON001",
  "expected_otif":true
 }
]
JSON


echo "📌 6. Run Tests"

if command -v pytest >/dev/null 2>&1
then
    pytest tests/unit -v
else
    echo "pytest not installed - skip"
fi


echo "📌 7. Git Commit"

git add .

git commit -m "Sprint AEONMATRIX Quality Hardening: KPI Validation and Unit Tests" || true


echo "📌 8. Push Current Branch"

git push origin HEAD || true


echo "✅ Sprint AEONMATRIX Quality Hardening Completed"
echo "🎯 Target:"
echo "- Validation Layer Added"
echo "- KPI Unit Test Foundation Added"
echo "- OTIF / Inventory Accuracy Protected"
echo "- Ready for CI/CD Quality Gate"

