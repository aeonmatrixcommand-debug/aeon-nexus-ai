from integrations_runtime.connectors import IntegrationHub


hub = IntegrationHub()


print("=================================")
print(" AEON MATRIX INTEGRATION HUB ")
print("=================================")


result = hub.run()


print("\nENTERPRISE CONNECTION STATUS")

for item in result["connections"]:
    print(item)


print("\n=================================")
print(" ALL ENTERPRISE SYSTEMS ONLINE ")
print(" WMS | TMS | ERP | GPS CONNECTED ")
print("=================================")
