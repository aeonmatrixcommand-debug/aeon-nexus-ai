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
