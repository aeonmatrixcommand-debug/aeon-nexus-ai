class NoScanNoMoveControl:

    def validate(self, movement):
        scanned = movement.get("scanned", False)

        return {
            "allowed": True if scanned else False
        }
