from datetime import datetime


class WMSConnector:

    def sync(self):
        return {
            "system": "WMS",
            "status": "CONNECTED",
            "inventory": "SYNCED"
        }


class TMSConnector:

    def sync(self):
        return {
            "system": "TMS",
            "status": "CONNECTED",
            "transport": "OPTIMIZED"
        }


class ERPConnector:

    def sync(self):
        return {
            "system": "ERP",
            "status": "CONNECTED",
            "finance": "ALIGNED"
        }


class GPSConnector:

    def sync(self):
        return {
            "system": "GPS",
            "status": "CONNECTED",
            "fleet": "TRACKING"
        }


class IntegrationHub:

    def run(self):

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "connections": [
                WMSConnector().sync(),
                TMSConnector().sync(),
                ERPConnector().sync(),
                GPSConnector().sync()
            ]
        }
